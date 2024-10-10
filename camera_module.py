import cv2
from PIL import Image, ImageTk

class Camera:
    def __init__(self, cam_index, width=800, height=600):
        self.cap = cv2.VideoCapture(cam_index)
        if not self.cap.isOpened():
            print(f"Error: Could not open camera {cam_index}.")
            exit()
        
        self.width = width
        self.height = height
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        
        # สร้าง VideoWriter สำหรับบันทึกวิดีโอ
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(f'camera{cam_index}_output.avi', fourcc, 20.0, (self.width, self.height))

    def read_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # บันทึกเฟรมลงไฟล์วิดีโอ
            self.out.write(frame)
            
            # แปลงสี
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            return ImageTk.PhotoImage(image=captured_image)
        return None

    def release(self):
        self.cap.release()
        self.out.release()
