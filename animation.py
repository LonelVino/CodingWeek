import matplotlib.pyplot as plt
import matplotlib.animation as anim
from generate_universe import *
from simulation import *


def beacon_gif():

    # Generation of universe
    universe = generate_universe(size=(6, 6))
    seed = create_seed(type_seed = "beacon")
    universe = add_seed_to_universe(seed,universe,x_start=1,y_start=1)

    # Initialisation
    fig = plt.figure()
    im = plt.imshow(universe, cmap='Greys', animated=True)

    # Update formula
    def update(i):
        im.set_array(game_life_simulate(universe,i,universe_dict))
        return im,
    
    # Animating beacon for 24 frames
    ani = anim.FuncAnimation(fig, update, frames=24, interval=500, blit = True)
    plt.show()

    # Saving gif
    ani.save('./gif/beacon.gif', writer='imagemagick')

    # Reset universe_dict
    reset_universe_dict(universe_dict)


def animate(universe_size,seed,seed_position,cmap='Greys',n_generations=30,interval=300,save=False,writer='ffmpeg'):
    '''
   Basic animation of game_of_life

    Parameters
    --------
    universe_size: 
        Tuple (int, int) dimensions of the universe
    seed: 
        (str) seed to be added
    seed_position: 
        (tuple (int, int)) coordinates where the top-left corner of the seed array should be pinned
    cmap
        (str) the matplotlib cmap that should be used
    n_generations
        (int) number of universe iterations, defaults to 30
    interval
        (int )time interval between updates (milliseconds), defaults to 300ms
    save
        (bool) whether the animation should be saved, defaults to False
    writer
        (str) the writer of video, defaults to 'ffmpeg'
    '''

    # Generation of universe
    universe = generate_universe(size=universe_size)
    universe = add_seed_to_universe(create_seed(seed),universe,x_start=seed_position[1],y_start=seed_position[0])
    
    # Initialisation
    fig = plt.figure()
    im = plt.imshow(universe, cmap=cmap, animated = True)

    #Update formula
    def update(i):
        im.set_array(game_life_simulate(universe,i,universe_dict))
        return im,
    
    # Animating universe
    ani = anim.FuncAnimation(fig, update, frames=n_generations, interval=interval, blit=True)
    
    # Saving gif, or showing it
    if save:
        name_of_gif = './gif/' + seed + '_universe_' + str(universe_size[0]) + '-' + str(universe_size[1]) + '_generations_' + str(n_generations) + '_interval_' + str(interval)+ '.gif'
        ani.save(name_of_gif, writer=writer) # To be changed to imagemagick if necessairy
    else:
        plt.show()
        
    # Reset universe_dict
    reset_universe_dict(universe_dict)