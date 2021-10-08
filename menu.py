
import os
from run_tic_tac_toe_3_x_3 import main
from run_tic_tac_toe_4_x_4 import main4
from run_tic_tac_toe_5_x_5 import main5

if (__name__ == '__main__'):
    
    option = 0
    number_of_states = 0

    while(option != 4):
        print("Choose the difficult: \n")
        print("1. Easy (3X3) \n")
        print("2. Medium (4X4) \n")
        print("3. Hard (5X5) \n")
        option = input()

        if option == "1":
            print("-- Easy mode --")
            main()
            count_states(number_of_states)
            os.system("pause")
        if option == "2":
            print("-- Medium mode --")
            main4()
        if option == "3":
            print("-- Hard mode --")
            main5()