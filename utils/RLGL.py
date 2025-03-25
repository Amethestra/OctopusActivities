from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from utils.MotionTracker import MotionTracker

class ThirdGame(QWidget):
    return_to_menu_signal = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.rules_label = QLabel(self)
        self.rules_label.setText("""
                                 Welcome to Green Means Go!
                                 """)
        self.rules_label.setAlignment(Qt.AlignCenter)
        self.rules_label.setWordWrap(True)
        self.layout.addWidget(self.rules_label)
        
        self.start_game_button = QPushButton("Start Game", self)
        self.start_game_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_game_button)
        
        self.stop_game_button = QPushButton("Stop Game", self)
        self.stop_game_button.clicked.connect(self.stop_game)
        self.stop_game_button.setEnabled(False)
        self.layout.addWidget(self.stop_game_button)
        
        self.return_button = QPushButton("Return to menu", self)
        self.return_button.clicked.connect(self.return_to_menu)
        self.layout.addWidget(self.return_button)
        
        self.is_game_running = False
        self.is_green_light = False
        self.motion_tracker = MotionTracker()
        self.motion_tracker.motion_detected_signal.connect(self.on_motion_detected)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.toggle_light)
        
    def start_game(self):
        self.is_game_running = True
        self.start_game_button.setEnabled(False)
        self.stop_game_button.setEnabled(True)
        
        self.motion_tracker.start()
        
        self.timer.start(2000)
        self.toggle_light()
    
    def stop_game(self):
        self.is_game_running = False
        self.timer.stop()
        self.motion_tracker.stop()
        self.rules_label.setText("Game Stopped")
        self.start_game_button.setEnabled(True)
        self.stop_game_button.setEnabled(False)
    
    def toggle_light(self):
        
        if not self.is_game_running:
            return

        if self.is_green_light:
            self.is_green_light = False
            self.rules_label.setText("Red Light")
        else:
            self.is_green_light = True
            self.rules_label.setText("Green Light")
        
        self.motion_tracker.motion_detected = False
        
    def on_motion_detected(self, motion_detected):
        if not self.is_green_light and motion_detected:
            self.rules_label.setText("Movement Detected")
            
    def return_to_menu(self):
        self.return_to_menu_signal.emit()
        