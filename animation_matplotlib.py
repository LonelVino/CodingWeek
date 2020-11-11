import matplotlib.pyplot as plt
import matplotlib.animation as anim
from generation import *
from seeds import *

def animation_jeu_de_la_vie(universe):
    fig = plt.figure()
    im = plt.imshow(universe, cmap='Greys', animated = True)
    def update(i):
        universe = im.get_array()
        im.set_array(etape_jeu_de_la_vie(universe))
        return im,
    ani = anim.FuncAnimation(fig, update, frames=15, interval = 500, blit=True)
    plt.show()

animation_jeu_de_la_vie(seeds["beacon"])




