import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from utils.SettingsMenu import Settings
from utils.Shapes import FirstGame
from utils.Mingo import SecondGame
from utils.RLGL import ThirdGame
from utils.RopePull import FourthGame

class Menu(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        
        self.stacked_widget = stacked_widget
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.setGeometry(100, 100, 1600, 900)
        self.setMinimumSize(800, 600)
        
        self.setWindowTitle("Game Hub Menu")
        
        self.show_menu()
        
    def show_menu(self):
        
        self.clear_layout()
        
        self.Welcome_Label = QLabel(self)
        self.Welcome_Label.setText("""Welcome!
                                   """)
        self.Welcome_Label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.Welcome_Label)
        
        button_layout = QHBoxLayout()
        
        self.add_game_button("Shapes", FirstGame, button_layout)
        self.add_game_button("Mingo", SecondGame, button_layout)
        self.add_game_button("Green Means Go", ThirdGame, button_layout)
        self.add_game_button("Rope Pull", FourthGame, button_layout)
        
        self.layout.addLayout(button_layout)
        
        self.add_navigation_button("Settings", Settings)
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.quit_game)
        self.layout.addWidget(self.quit_button)
        
    def add_game_button(self, text, game_class, button_layout):
        """Add a button to the layout that will switch to the game when clicked."""
        button = QPushButton(text)
        button.clicked.connect(lambda: self.start_game(game_class))
        button_layout.addWidget(button)
        
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
        self.layout.addWidget(button)
        
    def navigate_to(self, screen_class):
        
        screen_instance = screen_class(self.stacked_widget)
        self.stacked_widget.addWidget(screen_instance)
        self.stacked_widget.setCurrentWidget(screen_instance)
    
    def quit_game(self):
        QApplication.quit()
        
    def clear_layout(self):
        
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()