from tkinter import * 
from camera_module import *

app = Tk()
app.bind('<Escape>', lambda e: app.quit())
app.geometry('1200x750')

# สร้างวัตถุ Camera สำหรับกล้องตัวที่ 0
camera1 = Camera(cam_index=0)

# สร้าง Label สำหรับแสดงผลกล้อง
label_widget1 = Label(app)
label_widget1.pack(side=LEFT)
label_widget1.place(x=250, y=80)

def open_camera1():
    photo_image1, frame1 = camera1.read_frame()  # รับทั้ง photo_image1 และ frame1
    if photo_image1:
        label_widget1.photo_image = photo_image1
        label_widget1.configure(image=photo_image1)
    
    # เรียกฟังก์ชันซ้ำทุก 10 มิลลิวินาที
    label_widget1.after(10, open_camera1)

def capture_image1():
    _, frame1 = camera1.read_frame()
    if frame1 is not None:
        # บันทึกภาพเป็นไฟล์ jpg
        camera1.capture_image(frame1, file_format='jpg')

# สร้างปุ่มเพื่อเปิดกล้อง
button1 = Button(app, text="Open Camera 1", command=open_camera1)
button1.pack(side=LEFT)

button2 = Button(app, text="Load")
button2.pack(side=LEFT)

button3 = Button(app, text="Capture", command=capture_image1)
button3.pack(side=LEFT)

# จัดวางปุ่ม
button1.place(x=10, y=300)
button2.place(x=10, y=350, width=80)
button3.place(x=1000, y=350, width=100)

# สร้างลูปไม่รู้จบเพื่อแสดงแอปในหน้าจอ
app.mainloop()

# ปล่อยการเชื่อมต่อกล้องเมื่อปิดโปรแกรม
camera1.release()
