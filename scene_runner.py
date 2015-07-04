import frame_source as fs
import scene_modeler as sm
import matplotlib.pyplot as plt

def run():
    frame_directory = "data/boats"
    frame_source = fs.create_frame_source(frame_directory, grayscale = True)
    modeler = sm.SceneModeler(frame_source)
    modeler.run() # we have a model now
    # iterate over frames and grab foregrounds out
    frame_num = 0
    for frame in frame_source.frames():
        plt.axis('off')
        framename = "%03d.png" % frame_num
        foreground = modeler.find_foreground(frame)
        plt.imshow(foreground, aspect='normal', cmap=plt.get_cmap('gray'))
        plt.savefig(framename)
        frame_num += 1
        

if __name__ == '__main__':
    run()
