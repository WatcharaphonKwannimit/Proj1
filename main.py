from tkinter import *
from camera_module import Camera  # นำเข้าคลาส Camera
from tkinter import filedialog
from PIL import Image, ImageTk  # เพิ่มการใช้งาน PIL สำหรับการเปิดรูปภาพ

app = Tk()
app.bind('<Escape>', lambda e: app.quit())
app.geometry('1200x750')

# สร้าง Label สำหรับแสดงผลกล้องหรือภาพ
label_widget1 = Label(app)
label_widget1.pack(side=LEFT)
label_widget1.place(x=250, y=80)

# ตัวแปรสำหรับกล้อง
camera1 = None
is_camera_running = False

def open_camera1():
    global camera1, is_camera_running
    close_image()  # ปิดภาพที่อัปโหลดเมื่อเปิดกล้อง

    # สร้างกล้องใหม่หากยังไม่มีหรือเคยปิดไปแล้ว
    if camera1 is None or not camera1.cap.isOpened():
        camera1 = Camera(cam_index=0)  # สร้างวัตถุ Camera ใหม่

    is_camera_running = True

    def update_camera():
        if is_camera_running:
            photo_image1, frame1 = camera1.read_frame()  # รับทั้ง photo_image1 และ frame1
            if photo_image1:
                label_widget1.photo_image = photo_image1
                label_widget1.configure(image=photo_image1)
            
            # เรียกฟังก์ชันซ้ำทุก 10 มิลลิวินาที
            label_widget1.after(10, update_camera)

    update_camera()

def close_camera():
    global is_camera_running, camera1
    is_camera_running = False  # หยุดการอัปเดตภาพจากกล้อง
    if camera1 is not None:
        camera1.release()  # ปล่อยกล้อง
        camera1 = None  # ตั้งค่าให้ None เพื่อใช้ในการเปิดใหม่

def close_image():
    label_widget1.configure(image='')  # ลบภาพออกจาก Label

def capture_image1():
    if camera1 is not None:
        _, frame1 = camera1.read_frame()
        if frame1 is not None:
            # บันทึกภาพเป็นไฟล์ jpg
            camera1.capture_image(frame1, file_format='jpg')

def import_file():
    close_camera()  # หยุดกล้องก่อนโหลดไฟล์
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("image files", "*.png *.jpg"), ("All files", "*.*")])
    if file_path:
        # เปิดรูปภาพโดยใช้ PIL
        img = Image.open(file_path)
        img = img.resize((500, 400))  # ปรับขนาดตามต้องการ
        photo = ImageTk.PhotoImage(img)
        label_widget1.photo_image = photo  # เก็บภาพไว้ไม่ให้ garbage collected
        label_widget1.configure(image=photo)

# สร้างปุ่มเพื่อเปิดกล้อง
button1 = Button(app, text="Open Camera 1", command=open_camera1)
button1.pack(side=LEFT)

button2 = Button(app, text="Load", command=import_file)
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
if camera1 is not None:
    camera1.release()
