from tkinter import *
import cv2
from PIL import Image, ImageTk

# สร้าง VideoCapture สำหรับกล้องตัวที่ 0 และ 1
cap1 = cv2.VideoCapture(0) 

# ตรวจสอบว่ากล้องเปิดอยู่หรือไม่
if not cap1.isOpened():
    print("Error: Could not open one or both cameras.")
    exit()

width, height = 800, 600
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

app = Tk()
app.bind('<Escape>', lambda e: app.quit())

# สร้าง Label สำหรับกล้องสองตัว
label_widget1 = Label(app)
label_widget1.pack(side=LEFT)

def open_camera1(): 
    ret, frame1 = cap1.read()
    if ret:
        # แปลงสี
        opencv_image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        captured_image1 = Image.fromarray(opencv_image1)
        photo_image1 = ImageTk.PhotoImage(image=captured_image1)
        
        label_widget1.photo_image = photo_image1
        label_widget1.configure(image=photo_image1)

    # เรียกฟังก์ชันซ้ำทุก 10 มิลลิวินาที
    label_widget1.after(10, open_camera1)

# สร้างปุ่มเพื่อเปิดกล้อง
button1 = Button(app, text="Open Camera 1", command=open_camera1)
button1.pack(side=LEFT)



# สร้างลูปไม่รู้จบเพื่อแสดงแอปในหน้าจอ
app.mainloop()

# ปล่อยการเชื่อมต่อกล้องเมื่อปิดโปรแกรม
cap1.release()
