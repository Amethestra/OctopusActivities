from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class ThirdGame(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Green Means Go")
        layout.addWidget(label)
        
        back_button = QPushButton("Menu")
        back_button.clicked.connect(self.return_to_menu)
        layout.addWidget(back_button)
        
    def return_to_menu(self):
        self.stacked_widget.setCurrentIndex(0)
    