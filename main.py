import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from utils.Menu import Menu

def main():
    app = QApplication(sys.argv)
    
    stacked_widget = QStackedWidget()
    
    menu_screen = Menu(stacked_widget)
    stacked_widget.addWidget(menu_screen)
    
    stacked_widget.setCurrentWidget(menu_screen)
    stacked_widget.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()