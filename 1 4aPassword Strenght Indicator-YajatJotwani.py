import re
from string import punctuation


def check_a_password(the_password):
    result = 'example classification'

    return result

def checking_password_list(a_password_list):
    """ Test the strengths of the passwords in the list above.
        pre-condition: a list of example passwords
        post-condition: returns whether the password is very weak, weak, strong, or very strong.
    """
    for each_password in a_password_list:
        classification = check_a_password(each_password)
        print(classification)




## Main Program
#State that the program will test your PW (password) strength.
print('This program will test your password strength.')
#Loop code for 999 times.
password_list = [ 'abc', '123',  'abc123',  'abcdefgh',  'abcd1234',  'abcd1234!', '1234']

checking_password_list(password_list)

""" OLD CODE -------

    #Assign variable special to all special characters
    letter = "[a-z]"
    number = "[0-9]"
    
    special = '[' + punctuation + ']'



    #If the password length is less than 8 characters, then the PW is either weak or very-weak depending on if it uses letters, numbers, both, or special characters. 

    if len(user_password)< 8:
        #If the PW is just composed of numbers, then it is very weak. 
        if str(user_password).isdigit():
            print('Your password is very weak. Try adding some letters and special characters and increase the length of your password to atleast 8 characters!')
        #If the PW is just composed of letters, then it is just weak.
        elif str(user_password).isalpha():
            print('Your password is weak. Try making you password longer and include special characters as well as numbers.')
        #If the PW has special characters or both numbers and letters, then it is weak.
        else:
            print('Your password is weak. Try making your password longer and adding different sorts of characters.')

    #If the password is greater than 8 characters in length, then the PW is either mediocre, strong, or very-strong based upon the combination of numbers, letters, and special characters.        

    else:
        #If a password only has numbers, it will say its mediocre.   
        if str(user_password).isdigit():
            print('Your password is mediocre. Try to additonally use letters and special characters rather than just numbers.')
        #If a password only has letters, it was also say that its mediocre.  
        elif str(user_password).isalpha():
            print('Your password is mediocre. Try to additonally use numbers and special characters rather than just letters.')
        #If a password has atleast 1 number and atleast 1 letter, then it will print that the PW is strong. 
        elif len(re.findall(letter,str(user_password)))>= 1 and len(re.findall(number,str(user_password)))>= 1 and len(re.findall(special,str(user_password)))== 0:
            print("Your password is strong, but try to add some special characters.")
        #If a password has atleast one letter, number, and special character, then it is a very good password.
        else:
            print('This is a very good password!')
"""
