from tkinter import *
import random

pressed_button = None
starting_point = None
obstacle_list = None
destination_point = None

def gui():
    root = Tk()
    root.title('QLearning Algorithm')
    root.geometry('500x500')
    root.resizable(width = FALSE, height = FALSE)
    count = 0                                           # for identifying each button/vertex and passing unique parameters
    button_list = []                                    # stores button created during runtime

    # Matrix for algorithm
    matrix = [[0 for i in range(10)] for j in range(10)]

    # Matrix For Buttons painting
    button_matrix = [[0 for i in range(10)] for j in range(10)]

    frame_up = Label(root)
    frame_down = Label(root)

    frame_up.pack()
    frame_down.pack()

    global pressed_button                               # for differentiating b/w starting, ending & obstacles point
    pressed_button = 0
    global starting_point                               # starting_point is starting point
    starting_point = 0
    global obstacle_list                                # stores the obstacles when pressed_button is 2
    obstacle_list = []
    global destination_point                            # final destination variable
    dest = 1000

    f = open("Coordinates.txt", "w")

    def button_mode(mode):                              # input field by user starting/obstacles/destination point
        global pressed_button
        pressed_button = mode

    def button_click(but_no):                                   # clicked buttons in path
        global pressed_button

        second_number = int(but_no % 10)
        first_number = int(but_no / 10)

        if pressed_button == 1:                                # for starting point when pressed_button = 1
            button_matrix[first_number][second_number].config(bg = '#ffe525')
            global starting_point
            starting_point = but_no
            start_button['state'] = DISABLED                    # Disable button after press
            pressed_button = 0

        if pressed_button == 2:                                # for destination when pressed_button = 2
            button_matrix[first_number][second_number].config(bg = '#7dcf21')
            global destination_point
            destination_point = but_no
            destination_button['state'] = DISABLED              # Disable button after press
            pressed_button = 0

    start_button = Button(frame_up, text = 'Select Start Point', command = lambda: button_mode(1))
    destination_button = Button(frame_up, text = 'Select Destination', command=lambda: button_mode(2))

    start_button.grid(row = 0, column = 0, padx = 10)
    destination_button.grid(row = 0, column = 1)

    for i in range(10):
        for j in range(10):
            random_number = random.randint(1,9)
            button_matrix[i][j] = Button(frame_down, text = f'{random_number}', padx = 5, pady = 5, command = lambda x=count: button_click(x))
            button_matrix[i][j].grid(row = i, column = j, sticky = "ew")
            matrix[i][j] = random_number
            count += 1

    # algorithm script is called
    def Run():                                         
        parent = algorithm.backened(starting_point, obstacle_list, destination_point)
        for value in parent:
            button_list[value].config(bg = '#33fff0')         # path color is turned blue
        button_list[starting_point].config(bg = '#ffe525')               # starting pt color is turned back yellow
    
    run_button = Button(frame_up, text = 'Run', command = Run)
    run_button.grid(row = 0, column = 2, padx = 10, pady = 5)

   # Restarting Gui
    def restart():           
        root.destroy()
        gui()
        
    restart_button = Button(frame_up, text='Restart', command = restart)
    restart_button.grid(row = 0, column = 3, padx = 10, pady = 5)

    # Creating obstacles that random place
    def setting_obstacles(): 
        for a in range(30): 
            random_numbers_x = random.randint(0, 9)
            random_numbers_y = random.randint(0, 9)
            
            while matrix[random_numbers_x][random_numbers_y] == 0: # If there is random number in obstacle list generate new random number
                random_numbers_x = random.randint(0, 9)
                random_numbers_y = random.randint(0, 9)

            matrix[random_numbers_x][random_numbers_y] = 0

            button_matrix[random_numbers_x][random_numbers_y].config(bg = '#ff8a33')
        
        for i in range (10):
            for j in range (10):
                if(matrix[i][j] == 0):
                    f.write(str(i) + ", " + str(j) + ", " + "K" + "\n")
                else:
                    f.write(str(i) + ", " + str(j) + ", " + "B" + "\n")

    obstacle_button = Button(frame_up, text = 'Set Obstacles', command = setting_obstacles)
    obstacle_button.grid(row = 0, column = 4, padx = 10, pady = 5)

    mainloop()
gui()