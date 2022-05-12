'''
Purpose: To check if a user entered string is a 
palindrome or not
Programmer: Jae Bird
Date: 5/2/22
'''
# Declare global variables
original_string = ''
def main():
  # Initialize answer to Y
  answer = 'Y'
  print_headings()
  while answer == 'Y' or answer == 'y':
    prompt_user_to_enter_the_string()
    answer = input('Would you like to continue? (Y/N): ')
  else:
    print_footings()
#------------------------------------------------------
def print_headings():
  print('******************************')
  print('***** Palindrome Checker *****')
  print('******************************')
#----------------------------------------------------
def prompt_user_to_enter_the_string():
  global original_string
  # Prompt user to enter string
  original_string = input('Please, Enter the String to check if it is a palindrome: ')
  # Convert string to lower case
  original_string = original_string.lower()
  # Call check if string is palindrome function
  check_if_string_palindrome(original_string)
#-----------------------------------------------------
def check_if_string_palindrome(original_string):
  # Declare low variable to hold index of first character in string
  low = 0
  # Declare high variable to hold index of last character in string
  high = len(original_string) - 1
  # Declare a variable called is palindrom, set value to True
  is_palindrome = True
  # Use while statement to loop entire string 
  # While entire string is NOT checked and is_palindrom is True
  while((low < high) and (is_palindrome == True)):
    # Check if the character position low is equal to 
    # character position high
    if (original_string[low] == original_string[high]):
      is_palindrome = True
      break
    else:
      is_palindrome = False
    # Increment the low value by 1
    low += 1
    # Decrement the high value by 1
    high -= 1
  # end of while statement
  # Check if the is_palindrom is True
  if (is_palindrome == True):
    print(f"The String '{original_string}' is a Palindrome.")
  else:
    print(f"The String '{original_string}' is NOT a Palindrome.")
#----------------------------------------------------------------
def print_footings():
  print('\n********************************')
  print('****** End of the Program ******')
  print('**** Programmer: Jason Bird ****')
  print('********************************')
#-------------------------------------------------------
main()