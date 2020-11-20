from animation import *


### Full Test ###
if __name__=='__main__':
    #beacon_gif()

    # infinite
    #animate((20,20),"infinite",(7,7),'Greys',n_generations=30,interval=50,save=True)

    # boat
    #animate((20,20),"boat",(7,7),'Greys',n_generations=30,interval=50,save=True)

    # r_pentomino
    #animate((20,20),"r_pentomino",(7,7),'Greys',n_generations=50,interval=50,save=True)

    # planeur
    #animate((20,20),'line_3',(8,8),'Greys',save=True)

    # planeur gliding from bottom right to top left; DISPLAY, NOT SAVED
    animate((20,20),"planeur",(15,15),'Greys',n_generations=400,interval=10,save=False)

    print('Finished, check working directory for saved gif file if save is set to true!')