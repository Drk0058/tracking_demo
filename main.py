
import pickle
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3


def updatelines(num, data, lines):
    for dat, line in zip(data, lines):
        line.set_data(dat[0:2, :num])
        line.set_3d_properties(dat[2, :num])

    return lines
def tmpballtracking():
    og_ball = pickle.load(open('og_ball.fig.pickle', 'rb'))
    save = False
    el = 10
    azi = -97
    il = 10
    xl = (0, 1280)
    yl = (0, 1280)
    zl = (min(og_ball[2]), 720)
    mx = min(len(og_ball[0]), len(og_ball[1]), len(og_ball[2]))
    frames = mx
    data = np.array([og_ball])
    fig = plt.figure()
    bcam = p3.Axes3D(fig)
    bcam.set_xlim(xl)
    bcam.set_ylim(yl)
    bcam.set_zlim(zl)
    bcam.view_init(elev=el, azim=azi)
    lines = [bcam.plot(dat[0, 0:2], dat[1, 0:2], dat[2, 0:2])[0] for dat in data]
    tracer = animation.FuncAnimation(fig, updatelines, frames, fargs=(data, lines), interval=il, blit=True)
    plt.show()
    pickle.dump(og_ball, open('og_ball.fig.pickle', 'wb'))
    if save:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=24, metadata=dict(artist='drk'), bitrate=1000)
        tracer.save('spin_vision_animate.mp4', writer=writer)

def tmpspinvision():
    og_ball = pickle.load(open('og_ball.fig.pickle', 'rb'))
    save = False
    el = 10
    azi = -97
    il = 10
    xl = (0, 1280)
    yl = (0, 1280)
    zl = (min(og_ball[2]), 720)
    mx = min(len(og_ball[0]), len(og_ball[1]), len(og_ball[2]))
    frames = mx
    # data = np.array([og_ball])
    straight_ball = pickle.load(open('straight_ball.fig.pickle', 'rb'))
    data = np.array([og_ball,straight_ball])
    fig = plt.figure()
    bcam = p3.Axes3D(fig)
    bcam.set_xlim(xl)
    bcam.set_ylim(yl)
    bcam.set_zlim(zl)
    bcam.view_init(elev=el, azim=azi)
    lines = [bcam.plot(dat[0, 0:2], dat[1, 0:2], dat[2, 0:2])[0] for dat in data]
    tracer = animation.FuncAnimation(fig, updatelines, frames, fargs=(data, lines), interval=il, blit=True)
    plt.show()
    pickle.dump(og_ball, open('og_ball.fig.pickle', 'wb'))
    if save:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=24, metadata=dict(artist='drk'), bitrate=1000)
        tracer.save('spin_vision_animate.mp4', writer=writer)

if __name__ == '__main__':
    tmpballtracking()
    tmpspinvision()
