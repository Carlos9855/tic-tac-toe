
# run_tic_tac_toe.py

import pygame
import sys
from tic_tac_toe_4_x_4 import *
from ai_4_x_4 import *
import time

pygame.init()

print("\nWelcome to Tic-Tac-Toe!\n")

def main4():
    while True:
        
        window = open_window() # open window
        create_board(window) # create board
        state = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"] # initialize board state
        terminal_state = False # initialize terminal state

        ai = choose_ai() # choose ai: random, minimax, full alpha-beta
        player = choose_player()

        if(player == "X"):
            ai_mark = "O"
            turn = True
        else:
            ai_mark = "X"
            turn = False
        
        # look for pygame events until terminal state occurs
        while not terminal_state:
            
            for event in pygame.event.get():
                
                # if quit event
                if event.type == pygame.QUIT: 
                    sys.exit(0) # close window     
                    
                # if mouse click event
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    
                    # human player goes
                    if( turn == True):
                    
                        pos = pygame.mouse.get_pos() # get mouse click position
                        region = map_to_grid(pos)  # map mouse click position to board region 0 - 8
                        empty_regions = find_empty_regions(state) # find empty regions
                                        
                        # if clicked region is empty  
                        if str(region) in empty_regions:
                            place_on_grid(window, region, player) # place marker on window
                            state[region] = player # update board state
                            empty_regions = find_empty_regions(state) # find empty regions
                            game_over = terminal_test(state, player) # check for terminal state
                            # if terminal state is found
                            if game_over:
                                pygame.event.get()
                                terminal_state = play_again()
                                
                    # ai player goes

                    start = time.process_time()
                    # randomly place ai
                    if ai == 1:
                        ai_region = random_ai(empty_regions) # call ai() to find best position

                    # minimax to place ai
                    if ai == 2:
                        my_state = state[:] # create copy of state list for scope
                        best = minimax(my_state, ai_mark)
                        ai_region = int(best[0])

                    # alphabeta to place ai
                    if ai == 3:
                        my_state = state[:] # create copy of state list for scope
                        best = alphabeta(my_state, -float("inf"), float("inf"), ai_mark)
                        ai_region = int(best[0])

                    if ai == 4:
                        my_state = state[:]  # create copy of state list for scope
                        best = alphabeta_cutoff(my_state, -float("inf"), float("inf"), 0, ai_mark)
                        ai_region = int(best[0])


                    place_on_grid(window, ai_region, ai_mark)  # place ai marker on window
                    state[ai_region] = ai_mark # update board state

                    stop = time.process_time()
                    elapsed = stop - start
                    print("AI time: " + str(elapsed))

                    game_over = terminal_test(state,ai_mark) # check for terminal state
                    turn = True

                    # terminal state is found
                    if game_over:
                        pygame.event.get()
                        terminal_state = play_again()

        # repeat game robustness - handle Yes No Y N ... or pop up?
        
    pygame.quit()