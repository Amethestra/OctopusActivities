import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from utils.SettingsMenu import Settings
from utils.Shapes import FirstGame
from utils.Mingo import SecondGame
from utils.RLGL import ThirdGame
from utils.RopePull import FourthGame

class Menu(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        
        self.stacked_widget = stacked_widget
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.add_game_button("Shapes", FirstGame)
        self.add_game_button("Mingo", SecondGame)
        self.add_game_button("Green Means Go", ThirdGame)
        self.add_game_button("Rope Pull", FourthGame)
        
        self.add_navigation_button("Settings", Settings)
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.quit_game)
        layout.addWidget(self.quit_button)
        
    def add_game_button(self, text, game_class):
        """Add a button to the layout that will switch to the game when clicked."""
        button = QPushButton(text)
        button.clicked.connect(lambda: self.start_game(game_class))
        self.layout().addWidget(button)
        
    def start_game(self, game_class):
        """Switch to the game."""
        game_instance = game_class(self.stacked_widget)
            
        self.stacked_widget.addWidget(game_instance)
        self.stacked_widget.setCurrentWidget(game_instance)
        
        if hasattr(game_instance, "return_to_menu_signal"):
            game_instance.return_to_menu_signal.connect(self.show_menu)
        
    def add_navigation_button(self, name, screen_class):
        
        button = QPushButton(name)
        button.clicked.connect(lambda: self.navigate_to(screen_class))
        self.layout().addWidget(button)
        
    def navigate_to(self, screen_class):
        
        screen_instance = screen_class(self.stacked_widget)
        self.stacked_widget.addWidget(screen_instance)
        self.stacked_widget.setCurrentWidget(screen_instance)
        
    def show_menu(self):
        self.stacked_widget.setCurrentWidget(self)
    
    def quit_game(self):
        QApplication.quit()