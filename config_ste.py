# Configuration file.

import arenas

# general -- first three parameters can be overwritten with command-line arguments (cf. "python tetracomposibot.py --help")

display_mode = 0
arena = 3
position = False 
max_iterations = 3000 #401*500

# affichage

display_welcome_message = False
verbose_minimal_progress = True # display iterations
display_robot_stats = False
display_team_stats = False
display_tournament_results = False
display_time_stats = True

# initialization : create and place robots at initial positions (returns a list containing the robots)

import robot_subsomption, robot_braitenberg_avoider, robot_braitenberg_loveBot

def initialize_robots(arena_size=-1, particle_box=-1): # particle_box: size of the robot enclosed in a square
    #x_center = arena_size // 2 - particle_box / 2
    y_center = arena_size // 2 - particle_box / 2
    robots = []
    #for i in range(3):
        #robots.append(robot_braitenberg_avoider.Robot_player(4, arena_size//2-16+i*8, 0, name="My Robot"+str(i), team="A"))
    robots.append(robot_braitenberg_loveBot.Robot_player(8, arena_size//2-16+4*8, 0, name="My Robot love", team="A"))
    robots.append(robot_braitenberg_avoider.Robot_player(12, arena_size//2-16+4*8, 0, name="My Robot", team="A"))
    return robots
