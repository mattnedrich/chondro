import numpy as np

class SceneModeler(object):
    def __init__(self, frame_source):
        self.frame_source = frame_source

    def run(self):
        total_frame = None
        frame_count = 0
        for frame in self.frame_source.frames():
            if total_frame == None:
                total_frame = np.zeros(frame.shape, dtype=np.float)
            total_frame = np.add(total_frame, frame)
            frame_count += 1
        total_frame = np.divide(total_frame, frame_count)
        self.model_frame = total_frame

    def find_foreground(self, input_frame):
        temp_frame = np.subtract(self.model_frame, input_frame)
        ignore_indices = temp_frame < 50
        keep_indices = temp_frame >= 50
        temp_frame[ignore_indices] = 0
        temp_frame[keep_indices] = 1 
        return temp_frame
