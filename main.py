from tkinter import *
from camera_module import *

app = Tk()
app.bind('<Escape>', lambda e: app.quit())

# สร้างวัตถุ Camera สำหรับกล้องตัวที่ 0
camera1 = Camera(cam_index=0)

# สร้าง Label สำหรับแสดงผลกล้อง
label_widget1 = Label(app)
label_widget1.pack(side=LEFT)

def open_camera1():
    photo_image1 = camera1.read_frame()
    if photo_image1:
        label_widget1.photo_image = photo_image1
        label_widget1.configure(image=photo_image1)
    
    # เรียกฟังก์ชันซ้ำทุก 10 มิลลิวินาที
    label_widget1.after(10, open_camera1)

# สร้างปุ่มเพื่อเปิดกล้อง
button1 = Button(app, text="Open Camera 1", command=open_camera1)
button1.pack(side=LEFT)

button2 = Button(app, text="Lord")
button2.pack(side=LEFT)


button1.place(x=10, y=20)
button2.place(x=10, y=60, width=80)


# สร้างลูปไม่รู้จบเพื่อแสดงแอปในหน้าจอ
app.mainloop()

# ปล่อยการเชื่อมต่อกล้องเมื่อปิดโปรแกรม
camera1.release()
