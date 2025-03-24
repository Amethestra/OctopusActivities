
class Game:
    def __init__(self, parent=None):
        self.parent = parent
        self.is_running = False
        self.is_paused = False
        
    def start_game(self):
        self.is_running = True
        self.is_paused = False
        self.setup_game()
        
    def setup_game(self):
        raise NotImplementedError("You must implement the setup_game method.")
    
    def end_game(self):
        self.is_running = False
        self.return_to_menu()
        
    def pause_game(self):
        if self.is_running and not self.is_paused:
            self.is_paused = True

    def resume_game(self):
        if self.is_running and self.is_paused:
            self.is_paused = False
    
    def update_game_state(self):
        
        if not self.is_paused:
            pass
    
    def render_game(self):
        pass
    
    def return_to_menu(self):
        self.parent.show_main_menu()
