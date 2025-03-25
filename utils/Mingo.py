import random
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import pyqtSignal

class SecondGame(QWidget):
    return_to_menu_signal = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Mingo")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.round = 1
        self.rounds_completed = 0
        self.number_pool_1_4 = [10, 9, 8 ,7]
        self.number_pool_5_7 = [6, 5, 4]
        self.number_pool_8_10 = [3, 2]
        self.selected_numbers = []
        
        self.number_label = QLabel("Press Start to Begin", self)
        self.layout.addWidget(self.number_label)
        
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)
        
        self.return_button = QPushButton("Return to Menu", self)
        self.return_button.setEnabled(False)
        self.return_button.clicked.connect(self.return_to_menu)
        self.layout.addWidget(self.return_button)
        
    def start_game(self):
        
        if self.round <= 4:
            
            if len(self.number_pool_1_4) == 0:
                self.number_pool_1_4 = [10, 9, 8, 7]
                self.selected_numbers = []
            available_numbers = [num for num in self.number_pool_1_4 if num not in self.selected_numbers]
            if available_numbers:
                num = random.choice(available_numbers)
                self.selected_numbers.append(num)
                self.number_pool_1_4.remove(num)
        elif self.round <= 7:
            
            if len(self.number_pool_5_7) == 0:
                self.number_pool_5_7 = [6, 5, 4]
                self.selected_numbers = []
            available_numbers = [num for num in self.number_pool_5_7 if num not in self.selected_numbers]
            if available_numbers:
                num = random.choice(available_numbers)
                self.selected_numbers.append(num)
                self.number_pool_5_7.remove(num)
        else:
            
            num = random.choice(self.number_pool_8_10)
        

        if self.rounds_completed > 9:
            self.number_label.setText("Game Complete")
            self.end_game()
        else:
            self.number_label.setText(f"Round {self.round}: {num}")
        
        self.round += 1
        self.rounds_completed += 1

    
    def end_game(self):
        self.start_button.setEnabled(False)
        self.return_button.setEnabled(True)
    
    def return_to_menu(self):
        self.return_to_menu_signal.emit()

            
            
        
    