import frame_source
import scene_modeler as sm

def run():
    frame_directory = "data/boats"
    fs = frame_source.create_frame_source(frame_directory)
    modeler = sm.SceneModeler(fs)
    modeler.run()
        
if __name__ == '__main__':
    run()
