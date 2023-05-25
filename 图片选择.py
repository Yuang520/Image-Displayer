from asyncio import events
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("图片查看器")
        self.master.geometry("500x500")
        self.master.resizable(True, True)

        self.image_path = None
        self.image = None
        self.image_label = None
        self.keep_on_top = False

        # 创建菜单栏
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        
        set_menu = Menu(menubar,tearoff=False)
        set_menu.add_command(label="打开文件", command=self.open_image)# 创建文件菜单
        set_menu.add_command(label="窗口置顶", command=self.toggle_keep_on_top)# 创建视图菜单
        menubar.add_cascade(label="设置", menu=set_menu)

        # 创建图片标签
        self.image_label = Label(self.master)
        self.image_label.pack(fill=BOTH, expand=YES)

        # 监听窗口大小变化
        self.master.bind("<Configure>", self.resize_image)

    def open_image(self):
        # 选择图片文件
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_path:
            self.image_path = file_path
            self.load_image()

    def load_image(self):
        # 加载图片并显示
        self.image = Image.open(self.image_path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.image_tk)

    def resize_image(self, event):
        # 重新计算图片大小以适应窗口大小
        if self.image and event.width > 0 and event.height > 0:
            width, height = self.image.size
            ratio = min(event.width / width, event.height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            self.resized_image = self.image.resize((new_width, new_height))
            self.resized_image_tk = ImageTk.PhotoImage(self.resized_image)
            self.image_label.config(image=self.resized_image_tk)

    def toggle_keep_on_top(self):
        # 切换窗口是否置顶
        if not self.keep_on_top:
            self.master.attributes("-topmost", True)
            self.keep_on_top = True
        else:
            self.master.attributes("-topmost", False)
            self.keep_on_top = False

if __name__ == "__main__":
    root = Tk()
    app = ImageWindow(root)
    root.mainloop()
