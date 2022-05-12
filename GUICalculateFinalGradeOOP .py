'''
Purpose: Use a GUI OOP to get 2 test scores and display their average
Programmer: Jae Bird 
Date: 4/27/22
'''

# Import modules needed in this project
import tkinter

# Declare a Class called CalculateTestAverage
class CalculateTestAverage:
    # Define and code the __init__function that starts automatically
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x300')
        self.main_window.title('Calculate average + Programmer: Jae Bird')
        # Create the frames used in this project
        self.first_name_frame = tkinter.Frame(self.main_window)
        self.last_name_frame = tkinter.Frame(self.main_window)
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.average_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        # Create and pack the labels for student last name and first name
        self.first_name_label = tkinter.Label (self.first_name_frame,
                                               text = 'Enter Student First Name: ',
                                               font = ('arial', 20, 'bold') )
        self.first_name_entry = tkinter.Entry (self.first_name_frame,width = 20,
                                               font = ('arial', 20, 'bold') )
        self.last_name_label = tkinter.Label (self.last_name_frame,
                                              text = 'Enter Student Last Name: ',
                                              font = ('arial',20,'bold'))
        self.last_name_entry = tkinter.Entry (self.last_name_frame, width = 20,
                                              font = ('arial', 20, 'bold'))
        self.first_name_label.pack (side = 'left')
        self.first_name_entry.pack (side = 'left')
        self.last_name_label.pack (side = 'left')
        self.last_name_entry.pack (side = 'left')
        
        # Create and pack the Labels and Entry widgets for test 1
        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Enter the score for Test 1: ',
                                         font = ('arial',20,'bold'))
        self.test1_entry = tkinter.Entry(self.test1_frame, width = 10,
                                         font = ('arial',20,'bold'))
        self.test1_label.pack(side = 'left')
        self.test1_entry.pack(side = 'left')
        # Create and pack the Labels and Entry Widgets for test2
        self.test2_label = tkinter.Label(self.test2_frame,
                                         text = 'Enter the score for Test 2: ',
                                         font = ('arial',20,'bold'))
        self.test2_entry = tkinter.Entry(self.test2_frame, width = 10,
                                         font = ('Arial',20,'bold'))
        self.test2_label.pack(side = 'left')
        self.test2_entry.pack(side = 'left')
        # Create and pack the widgets for the average
        self.result_label = tkinter.Label(self.average_frame,
                                          text='Tests Average: ',
                                          font = ('arial',20,'bold'))
        self.average = tkinter.StringVar() #To update average_label
        self.average_label = tkinter.Label(self.average_frame,
                                           textvariable = self.average,
                                           font = ('arial',20,'bold'))
        self.result_label.pack(side='left')
        self.average_label.pack(side='left')
        # Create and pack the button widgets
        self.calc_button = tkinter.Button(self.button_frame,
                                         text = 'Calculate Average',
                                         command = self.calculate_average,
                                         font = ('arial',20,'bold'))
        self.quit_button = tkinter.Button (self.button_frame,
                                           text = 'Quit',
                                           command = self.main_window.destroy,
                                           font = ('arial', 20, 'bold'))
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        # Pack the frames
        self.first_name_frame.pack()
        self.last_name_frame.pack()
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.average_frame.pack()
        self.button_frame.pack()
        # Start the main loop
        tkinter.mainloop()
        #---------------------------------------------------------
    # The calculate_average method is the callback funtion for the
    # calculate_button widget
    def calculate_average(self):
        # Get the two test scores and store them in variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        # Calculate the average
        self.average_result = (self.test1 + self.test2)/2.0
        # Format the average result
        self.average_result = '{:.2f}'.format(self.average_result)
        # Update the average_label widget by storing the value of self.average
        # in the string var object reference by average
        self.average.set(self.average_result)
        self.average_result = float (self.average_result)
        if self.average_result >= 90:
            self.final_grade = 'A'
        elif self.average_result >= 80:
            self.final_grade = 'B'
        elif self.average_result >= 70:
            self.final_grade = 'C'
        elif self.average_result >= 60:
            self.final_grade = 'D'
        elif self.average_result >= 50:
            self.final_grade = 'F'
        self.average.set(str(self.average_result) + ' ' + 'Grade is: ' +
                         str (self.final_grade))
#---------------------------------------------------------------------------
# Create an instance onject of the test average class
calc_test_average = CalculateTestAverage()
        
        
