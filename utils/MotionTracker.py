import cv2
from PyQt5.QtCore import QObject, QTimer, pyqtSignal

class MotionTracker(QObject):
    motion_detected_signal = pyqtSignal(bool)
    
    def __init__(self, camera_index = 0, sensitivity = 50, detection_interval = 100):
        super().__init__()
        
        self.camera_index = camera_index
        self.sensitivity = sensitivity
        self.prev_frame = None
        self.motion_detected = False
        
        self.capture = cv2.VideoCapture(camera_index)
        if not self.capture.isOpened():
            print("Error: Could not open camera.")
            return
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_frame)
        self.timer.start(detection_interval)
        
    def start(self):
        self.timer.start(100)
        
    def process_frame(self):
        ret, frame = self.capture.read()
        if not ret:
            print("Error: Could not read frame.")
            return
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        
        if self.prev_frame is None:
            self.prev_frame = gray
            return

        frame_delta = cv2.absdiff(self.prev_frame, gray)
        _, thresh = cv2.threshold(frame_delta, self.sensitivity, 255, cv2.THRESH_BINARY)
        
        thresh = cv2.dilate(thresh, None, iterations = 2)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        motion_detected = any(cv2.contourArea(contour) > 500 for contour in contours)
        
        if motion_detected != self.motion_detected:
            self.motion_detected = motion_detected
            self.motion_detected_signal.emit(motion_detected)
        
        self.prev_frame = gray
    
    def set_sensitivity(self, sensitivity):
        self.sensitivity = sensitivity
    
    def stop(self):
        self.timer.stop()
        if self.capture.isOpened():
            self.capture.release()

    
    

