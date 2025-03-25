from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

class FourthGame(QWidget):
    return_to_menu_signal = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        self.rules_label = QLabel(self)
        self.rules_label.setText("""
                                 Welcome to tug of war!
                                 """)
        self.rules_label.setAlignment(Qt.AlignCenter)
        self.rules_label.setWordWrap(True)
        
        self.layout.addWidget(self.rules_label)
        
        self.return_button = QPushButton("Return to menu", self)
        self.return_button.clicked.connect(self.return_to_menu)
        self.layout.addWidget(self.return_button)
        
    def return_to_menu(self):
        self.return_to_menu_signal.emit()

        