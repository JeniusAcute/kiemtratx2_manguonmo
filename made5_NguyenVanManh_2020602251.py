'''-----------------------
thiết kế giao diện cho phần mềm
truy cập file trong máy
thêm các chức năng mới: làm sáng, làm tối, lật ảnh theo trục ox, lật ảnh theo trục oy
-----------------------
các hàm sẽ sử dụng:
thiết kế giao diện: sử dụng thư viện tkinter với các thành phần: Button, Label
các chức năng ảnh được xử lý và đảm nhận bởi các nút riêng biệt
truy cập file: sử dụng hàm filedialog.askopenfilename()
làm sáng, làm tối: cv2.convertScaleAbs()
lật ảnh theo trục Ox, Oy: cv2.flip()
-----------------------'''

import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Entry, filedialog

def open_file():
    global file_path
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png')])
        if file_path:
            label.config(text=file_path)
            print(file_path)
    except Exception as e:
        print(e)

def process_image(i):
    try:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
        bigger = cv2.resize(img, (1050, 1610))
        stretch_near = cv2.resize(img, (780, 540), interpolation = cv2.INTER_LINEAR)
        bright = cv2.convertScaleAbs(img, alpha=1.5, beta=100)
        dark = cv2.convertScaleAbs(img, alpha=1.5, beta=-100)
        flip_lr = cv2.flip(img, 1)  # Flip horizontally
        flip_ud = cv2.flip(img, 0)  # Flip vertically

        Titles = ["Original", "Half", "Bigger", "Interpolation Nearest", "Bright", "Dark", "Flip Left-Right", "Flip Up-Down"]
        images = [img, half, bigger, stretch_near, bright, dark, flip_lr, flip_ud]

        print(f"Anh duoc xu ly voi chuc nang {Titles[i]}")
        plt.title(Titles[i])
        plt.imshow(images[i])
        plt.show()

    except Exception as e:
        label.config(text="Chưa có hình ảnh. Không thể tạo file. Mời chọn ảnh")
        print("Chua co anh tai day")

def set_path():
    global file_path
    file_path = path_entry.get()
    label.config(text=file_path)

root = Tk()
root.geometry("500x500")

file_path = ''
#file_path = input()  #nhap tu cua so lenh khi do comment cau lenh ngay dang truoc

T = ["Original", "Half", "Bigger", "Interpolation Nearest", "Bright", "Dark", "Flip Left-Right", "Flip Up-Down"]

button1 = Button(root, text='Chọn hình ảnh PNG', command=open_file)
button1.pack()

path_entry = Entry(root)
path_entry.pack()

path_button = Button(root, text='Nhập đường dẫn', command=set_path)
path_button.pack()

for i in range(len(T)):
    button = Button(root, text=f'Xử lý {T[i]}', command=lambda i=i: process_image(i))
    button.pack()

label = Label(root, text='')
label.pack()

root.mainloop()
