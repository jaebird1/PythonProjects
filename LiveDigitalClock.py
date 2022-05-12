'''
Purpose: Display a live Digital Clock on screen 
Programmer: Jae Bird
Date: 5/2/22
'''
# Import modules
from tkinter import *
from time import strftime
# Create & construct an object called window from Tk module
window = Tk()
# Add a title to the window screen
window.title('Live Digital Clock + Programmer: Jae Bird')
# Change window geometry
window.geometry('520x160')
# Assign text font properties
text_font = ('garamond',70,'bold')
# Assign background color
background = 'black'
# Assign foreground color
foreground = 'magenta'
# Assign border width
border_width = 30
# Declare clock label
clock_label = Label (window,font=text_font,
bg=background,
fg=foreground,
bd=border_width)
clock_label.grid(row=0,column=0)
#---------------------------------------------------
def run_digital_clock():
  # Assign the formatted strftime to time_live
  # using military format 
  # Hours:Minutes:Seconds
  time_live = strftime('%I:%M:%S %p')
  clock_label.config(text = time_live)
  # Call run_digital_clock tp run every 1000 milliseconds
  clock_label.after(1000,run_digital_clock)
# Call run digital clocl function to start running the clock
run_digital_clock()
# Inform window to loop and display the window on screen
window.mainloop()