import argparse
from animation import animate


if __name__ == '__main__':
    gameoflife = argparse.ArgumentParser(description='Start a game of life')
    
    # universe_size
    gameoflife.add_argument('universe_size_y', metavar='uY', type=int, help='Size of y-dimension of universe')
    gameoflife.add_argument('universe_size_x', metavar='uX', type=int, help='Size of x-dimension of universe')
    
    # seed
    gameoflife.add_argument('seed', metavar='s', type=str, help='Seed to be placed')
    
    # seed_position
    gameoflife.add_argument('seed_position_y', metavar='sY', type=int, help='Row number of the upper left box of the seed')
    gameoflife.add_argument('seed_position_x', metavar='sX', type=int, help='Column number of the upper left box of the seed')

    # cmap
    gameoflife.add_argument('-c', '--cmap', metavar='cmap', dest='cmap', type=str, help='Colormap for animated gif, default to Greys', default='Greys' )

    # n_generations
    gameoflife.add_argument('-g','--generations', metavar='n_generations', dest='n_generations', type=int, default=30, help='Number of iterations for game, default to 30')

    # interval
    gameoflife.add_argument('-i','--interval', metavar='interval', dest='interval',type=int, default=300, help='Time interval between updates in milliseconds, default to 300')

    # save
    gameoflife.add_argument('-s','--save', dest='save', action='store_true', default=False, help='Store the gif file, default to False')

    # writer
    gameoflife.add_argument('-w','--writer', metavar='writer', dest='writer',type=str, default='ffmpeg', help='Writer of the animation, default to ffmpeg')

    args = gameoflife.parse_args()
    animate((args.universe_size_y,args.universe_size_x),args.seed,(args.seed_position_y,args.seed_position_x),args.cmap,args.n_generations,args.interval,args.save,args.writer)