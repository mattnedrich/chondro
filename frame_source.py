import cv2
import glob

def create_frame_source(frame_directory, grayscale = False):
    frame_source = FileFrameSource(frame_directory, grayscale)
    return frame_source

class FrameSource(object):
    def frames(self):
        raise NotImplementedException("abstract method")

class FileFrameSource(FrameSource):
    def __init__(self, frame_directory, grayscale = False):
        self._use_grayscale = grayscale
        self._frame_directory = frame_directory
        self._images = glob.glob("%s/*.jpg" % frame_directory)

    def frames(self):
        for frame in self._images:
            frame = cv2.imread(frame)
            if self._use_grayscale:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            yield frame 
