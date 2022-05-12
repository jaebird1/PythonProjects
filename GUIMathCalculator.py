'''
Purpose: A simple calculator that does addition,
multiplication, subtraction, and division
Programmer: Jae Bird
Date: 5/4/22
'''
from tkinter import *
# Declare global variables
operator = ''
# Construct a window
window = Tk()
window.geometry('430x550')
window.title('Standard Calculator + Programmer: Jae Bird')
# Call stringvar function to assign the value to input_text variable
input_text = StringVar()
#----------------------------------------------------
# Define/code click function and pass parameter num to it
def click(num):
  global operator
  operator = operator + str(num)
  input_text.set(operator)
#--------------------------------------------------------
def evaluate():
  global operator
  output = str(eval(operator))
  input_text.set(output)
#------------------------------------------------------
def clear_display():
  global operator
  operator = ''
  input_text.set(operator)
#---------------------------------------------------
# Add the input display entry widget to the grid
input_display = Entry (window,
                       font = ('arial',40,'bold'),
                       bg='lightgreen',
                       bd=10,width=13,justify='right',
                       insertwidth=4,
                       textvariable=input_text)
input_display.grid(columnspan=10)
# Add the numbers buttons 7,8,9, and + sign to grid row 1
# BUTTON 7 
btn7 = Button(window, font=('arial',32,'bold'),
              command=lambda:click(7),
              bg='silver',text='7',
              bd=5,padx=15,pady=5)
btn7.grid(row=1,column=0)
# BUTTON 8
btn8 = Button(window, font=('arial',32,'bold'),
              command=lambda:click(8),
              bg='silver',text='8',
              bd=5,padx=15,pady=5)
btn8.grid(row=1,column=1)
# BUTTON 9 
btn9 = Button(window, font=('arial',32,'bold'),
              command=lambda:click(9),
              bg='silver',text='9',
              bd=5,padx=15,pady=5)
btn9.grid(row=1,column=2)
# ADD BUTTON
add = Button(window, font=('arial',32,'bold'),
             command=lambda:click('+'),
             bg='violet', text='+',
             bd=5,padx=15,pady=10)
add.grid(row=1,column=3)
# Add the number buttons 4,5,6 and - sign to grid row 2
# BUTTON 4
btn4 = Button(window,font=('arial',32,'bold'),
              command=lambda:click(4),
              bg='silver',text='4',
              bd=5,padx=15,pady=10)
btn4.grid(row=2,column=0)
# BUTTON 5
btn5 = Button(window,font=('arial',32,'bold'),
              command=lambda:click(5),
              bg='silver',text='5',
              bd=5,padx=15,pady=10)
btn5.grid(row=2,column=1)
# BUTTON 6
btn6 = Button(window,font=('arial',32,'bold'),
              command=lambda:click(6),
              bg='silver',text='6',
              bd=5,padx=15,pady=10)
btn6.grid(row=2,column=2)
# SUBTRACT BUTTON
subtract = Button(window,font=('arial',32,'bold'),
                  command=lambda:click('-'),
                  bg = 'violet',text='-',
                  bd=5,padx=15,pady=10)
subtract.grid (row=2,column=3)
# Add the number buttons 1,2,3 and * sign to grid row 3
# BUTTON 1 
btn1 = Button(window, font = ('arial',32,'bold'),
              command=lambda:click(1),
              bg='silver', text='1',
              bd=5,padx=15,pady=10)
btn1.grid(row=3,column=0)
# BUTTON 2
btn2 = Button(window, font=('arial',32,'bold'),
              command = lambda:click(2),
              bg='silver',text='2',
              bd=5,padx=15,pady=10)
btn2.grid (row = 3, column = 1)
# BUTTON 3
btn3 = Button(window,font=('arial',32,'bold'),
              command=lambda:click(3),
              bg='silver',text='3',
              bd=5,padx=15,pady=10)
btn3.grid (row = 3, column = 2)
# MULTIPLY BUTTON
multiply = Button(window,font=('arial',32,'bold'),
                  command=lambda:click('*'), 
                  bg='violet',text='*',
                  bd=5,padx=15,pady=10)
multiply.grid (row = 3, column = 3)
# Add the buttons 0, Clr, = and / sign to grid row 4
# BUTTON 0 
btn0 = Button(window,font=('arial',32,'bold'),
              command=lambda:click(0),
              bg='silver',text='0',
              bd=5,padx=15,pady=10)
btn0.grid (row = 4, column = 0)
# CLEAR BUTTON
btnClear = Button(window,font=('arial',32,'bold'),
                  command = clear_display, 
                  bg = 'lightblue',text = 'Clr',
                  bd = 5, padx = 15,pady=10)
btnClear.grid (row = 4, column = 1)
# EQUAL BUTTON
equal = Button (window, font = ('arial',32,'bold'),
                command = evaluate, 
                bg='blue', text = '=',
                bd=5, padx=15, pady=10)
equal.grid (row = 4, column = 2)
# DIVISION BUTTON
division = Button(window,font=('arial',32,'bold'),
                  command=lambda:click('/'), 
                  bg = 'violet',text='/',
                  bd=5, padx=15, pady=10)
division.grid (row = 4,column = 3)

# Call the window.mainloop() function so the program will
# start executing
window.mainloop()



