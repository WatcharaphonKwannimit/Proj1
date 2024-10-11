import cv2
from PIL import Image, ImageTk
import os
class Camera:
    def __init__(self, cam_index, width=800, height=600, save_dir="captures"):
        self.cap = cv2.VideoCapture(cam_index)
        if not self.cap.isOpened():
            print(f"Error: Could not open camera {cam_index}.")
            exit()
        
        self.width = width
        self.height = height
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        # สร้างไดเรกทอรีสำหรับบันทึกภาพถ้าไม่มี
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        self.image_counter = 0  # ตัวนับสำหรับชื่อไฟล์ภาพ
    def read_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # แปลงสีสำหรับแสดงใน Tkinter
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            return ImageTk.PhotoImage(image=captured_image), frame
        return None, None
    def capture_image(self, frame, file_format='jpg'):
        # สร้างชื่อไฟล์สำหรับภาพที่จะบันทึก
        file_name = os.path.join(self.save_dir, f"capture_{self.image_counter}.{file_format}")
        # บันทึกภาพเป็นไฟล์ PNG หรือ JPG
        cv2.imwrite(file_name, frame)
        print(f"Captured {file_name}")
        self.image_counter += 1
    def release(self):
        self.cap.release()
