from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class SecondGame(QWidget):
    def __init__(self, stacked_widget, parent = None):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Mingo")
        layout.addWidget(label)
        
        back_button = QPushButton("Menu")
        back_button.clicked.connect(self.return_to_menu)
        layout.addWidget(back_button)
        
        self.parent = parent
        self.is_running = False
        self.is_paused = False
        
    def start_game(self):
        
        self.is_running = True
        self.is_paused = False
        self.setup_game()
        
    def setup_game(self):
        pass
    
    def end_game(self):
        self.is_running = False
        self.is_paused = False
        self.return_to_menu()
        
    def pause_game(self):
        if self.is_running and not self.is_paused:
            self.is_paused = True
            
    def resume_game(self):
        if self.is_running and self.is_paused:
            self.is_paused = False
    
    
        
        
    def return_to_menu(self):
        self.stacked_widget.setCurrentIndex(0)
        
    