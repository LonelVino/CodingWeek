import matplotlib.pyplot as plt
import matplotlib.animation as anim
from generation import *
from seeds import *
from implantation_graine import *

def animation_paramétrée(universe_size, seed, seed_position, cmap, n_generations, interval, save):
    universe = implantation_graine(universe_size, seed, seed_position)
    fig = plt.figure()
    im = plt.imshow(universe, cmap=cmap, animated = True)
    def update(i):
        universe = im.get_array()
        im.set_array(etape_jeu_de_la_vie(universe))
        return im,
    ani = anim.FuncAnimation(fig, update, frames=n_generations, interval=interval, blit=save)
    plt.show()

"""
animation_paramétrée((12,12), seeds['block_switch_engine'], (2,2), 'Reds', 3, 300, True)
"""
