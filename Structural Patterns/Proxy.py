import time
class Video:
    def __init__(self,filename):
        self.filename = filename
        self.loadVideo()
    
    def loadVideo(self):
        print(f"Loading video: {self.filename}... (Takes time)")
        time.sleep(2)  # Simulating heavy loading

    def play(self):
        print(f"playing video {self.filename}")

class VideoProxy:
    def __init__(self,filename):
        self.filename = filename
        self._video = None
    
    def play(self):
        if self._video is None:
            self._video = Video(self.filename)

        self._video.play()

proxy_video = VideoProxy("funny_cat_video.mp4")

proxy_video.play()

proxy_video.play()

        