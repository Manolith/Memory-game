import random
#import time

NUM_PAIRS = 3

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    lst = []
    for i in range(NUM_PAIRS):
        lst.append(i)
        lst.append(i)
    #print(lst)
    random.shuffle(lst)
    #print(lst)

    display_lst = []
    for i in range(NUM_PAIRS):
        display_lst.append("*")      
        display_lst.append("*")      
    #print(display_lst)

    valid_index(display_lst,lst)

def valid_index(display_lst,lst):
    
    while display_lst != lst:
        lst_index=[]
        print(display_lst)
        while len(lst_index) < 2:
            try:
                index = int(input("Enter an index: "))
                if index < 0 or  index > len(display_lst)-1:
                    print("Invalid index. Try again. ")
                else:
                    lst_index.append(index)   
            except ValueError:
                print("Not a number. Try again.")
            
            
        if lst_index[0] == lst_index[1]:
            print("You entered the same index twice. Try again.")
        else:   
            
            if lst[lst_index[0]] != lst[lst_index[1]]:
                print(f"Value at index {lst_index[0]} is {lst[lst_index[0]]}")
                print(f"Value at index {lst_index[1]} is {lst[lst_index[1]]}")
                print("No match. Try again.")
                input("Press Enter to continue...")
            else:
                print("Match!")
                
                display_lst[lst_index[0]] = lst[lst_index[0]]
                display_lst[lst_index[1]] = lst[lst_index[1]]
                #print(display_lst) 
        #time.sleep(1)
        clear_terminal()

    print(display_lst)
    print("Congratulations! You won!")


def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()