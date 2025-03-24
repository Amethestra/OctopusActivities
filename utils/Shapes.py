import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication
from PyQt5.QtCore import Qt, QTimer

class FirstGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Shapes")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        
        self.rules_label = QLabel("Rules:")
        self.rules_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.rules_label)
        
        self.start_button = QPushButton("Start Game", self)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 60
        
        self.timer_display = QLabel("01:00", self)
        self.timer_display.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.timer_display)
        
        self.return_button = QPushButton("Return to Menu", self)
        self.return_button.clicked.connect(self.return_to_menu)
        self.return_button.setVisible(False)
        self.layout.addWidget(self.return_button)
    
    def start_game(self):
        self.start_button.setVisible(False)
        self.time_left = 60
        self.update_timer_display()
        self.timer.start(1000)
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer_display()
        else:
            self.timer.stop()
            self.show_return_button()
    
    def update_timer_display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_string = f"{minutes:02}:{seconds:02}"
        self.timer_display.setText(time_string)
        
    
    def show_return_button(self):
        self.return_button.setVisible(True)
    
    def return_to_menu(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirstGame()
    window.show()
    sys.exit(app.exec_())
    
    