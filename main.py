from tkinter import *
import random

pressed_button = None
starting_point = None
obstacle_list = None
destination_point = None

def gui():
    root = Tk()
    root.title('QLearning Algorithm')
    root.geometry('600x600')
    root.resizable(width = FALSE, height = FALSE)
    count = 0                                           # for identifying each button/vertex and passing unique parameters
    
    root_size = 10                                

    # Matrix for algorithm
    matrix = [[0 for i in range(root_size)] for j in range(root_size)]

    # Matrix For Buttons painting
    button_matrix = [[0 for i in range(root_size)] for j in range(root_size)]

    frame_up = Label(root)
    frame_down = Label(root)

    frame_up.pack()
    frame_down.pack()

    global pressed_button                               # for differentiating b/w starting, ending & obstacles point
    pressed_button = 0
    global starting_point                               # starting_point is starting point
    starting_point = 0
    global destination_point                            # final destination variable
    dest = 1000

    f = open("Obstacle_list.txt", "w")

    def button_mode(mode):                              # input field by user starting/obstacles/destination point
        global pressed_button
        pressed_button = mode

    def button_click(but_no):                                   # clicked buttons in path
        global pressed_button

        second_number = int(but_no % 10)
        first_number = int(but_no / 10)

        if pressed_button == 1:                                # for starting point when pressed_button = 1
            button_matrix[first_number][second_number].config(bg = 'Aqua')
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
    destination_button = Button(frame_up, text = 'Select Destination', command = lambda: button_mode(2))

    start_button.grid(row = 0, column = 0, padx = 10)
    destination_button.grid(row = 0, column = 1)

    for i in range(root_size):
        for j in range(root_size):
            random_number = random.randint(1,9)
            button_matrix[i][j] = Button(frame_down, text = f'{random_number}', padx = 5, pady = 5, command = lambda x=count: button_click(x), height = 0, width = 0)
            button_matrix[i][j].grid(row = i, column = j, sticky = "ew")
            matrix[i][j] = random_number
            count += 1

    ''' # algorithm script is called
    def Run():                                         
 
    
    run_button = Button(frame_up, text = 'Run', command = Run)
    run_button.grid(row = 0, column = 2, padx = 10, pady = 5)
'''

   # Restarting Gui
    def restart():           
        root.destroy()
        gui()
        
    restart_button = Button(frame_up, text='Restart', command = restart)
    restart_button.grid(row = 0, column = 3, padx = 10, pady = 5)

    # Creating obstacles that random place
    def setting_obstacles(): 
        b = int((root_size**2)*(0.3))  # 30 percent of the matrix is obstacle 

        for a in range(b): 
            random_numbers_x = random.randint(0, 9)
            random_numbers_y = random.randint(0, 9)
            
            while matrix[random_numbers_x][random_numbers_y] == 0: # If there is random number in obstacle list generate new random number
                random_numbers_x = random.randint(0, 9)
                random_numbers_y = random.randint(0, 9)

            matrix[random_numbers_x][random_numbers_y] = 0

            button_matrix[random_numbers_x][random_numbers_y].config(bg = 'Red')
        
        for i in range (root_size):
            for j in range (root_size):
                if(matrix[i][j] == 0):
                    f.write(str(i) + ", " + str(j) + ", " + "K" + "\n") # K Obstacle
                else:
                    f.write(str(i) + ", " + str(j) + ", " + "B" + "\n") # B Not Obstacle

    obstacle_button = Button(frame_up, text = 'Set Obstacles', command = setting_obstacles)
    obstacle_button.grid(row = 0, column = 4, padx = 10, pady = 5)

    mainloop()
gui()