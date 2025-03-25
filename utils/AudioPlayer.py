from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class AudioPlayer:
    def __init__(self, parent=None):
        super().__init__()
        
        self.player = QMediaPlayer()
        self.parent = parent
    
    def load_audio(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
    
    def play(self):
        
        if self.player.mediaStatus == QMediaPlayer.NoMedia:
            print("No Audio Loaded")
            
        else:
            self.player.play()
    
    def pause(self):
        
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            print("No Audio is playing")
            
    def stop(self):
        
        if self.player.state() != QMediaPlayer.StoppedState:
            self.player.stop()
        else:
            print("Audio already stopped")
    
    def set_volume(self, volume):
        
        volume = max(0, min(100, volume))
        self.player.setVolume(volume)
        