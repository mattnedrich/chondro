
class SceneModeler(object):
    def __init__(self, frame_source):
        self.frame_source = frame_source

    def run(self):
        for frame in self.frame_source.frames():
            print "processing frame..."
