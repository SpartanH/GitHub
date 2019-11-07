print("This program checks if two words are anagrams.")
#Initiate variable.
still_checking = True
while still_checking:
#Set a variable to user's input for first/second word. 
    word1 = input('Enter the first word: ')
    word2 = input('Enter the second word: ')
#Set a variable for the list of characters in the user's input.
    word1_list = list(word1)
    word2_list = list(word2)
#Set a variable for the sorted list of characters in the user's input. 
    word1_list_sorted = sorted(word1_list)
    word2_list_sorted = sorted(word2_list)
#If the sorted words are not equal, the words are not anagrams. 
    if (word1_list_sorted != word2_list_sorted) or (word1 == word2):
        print('These words are not anagrams.')
#If the words are the same when sorted in order, they are anagrams.  
    elif word1_list_sorted == word2_list_sorted :
        print('These are anagrams, good work!')
    #Initiate variable
    take2 = True
    while take2:
        try_again = input('Would you like to try again? (y/n): ')
        #If the user outputs 'n,' end the program.
        if try_again == ('n') :
            still_checking = False
            take2 = False
        #If the user outputs 'y,' repeat the program or the big loop.
        elif try_again == ('y') :
            take2 = False
        #If the user enters something other than 'y' or 'n', then ask them to try again.
        else:
            take2 = True
            print("Please enter 'y' or 'n'")
#End the program by saying thanks. 
print('Thanks for using this program.')
