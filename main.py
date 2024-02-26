border = '~'

def startUp():
    print("This is the main menu please choose what you would like to do: ")
    print('1) Add clockIn & Out\n2) Check month pay')
    while True: 
        choice = input('Please Enter 1/2 ONLY!' )
        if choice == '1' or choice == '2':
            break
        elif choice.isdigit():
            print(border*50)
            print('!Enter a valid integer (1/2)!')
        else: 
            print(border*50)
            print('!Please Enter an Number (1/2)!')

    return int(choice)


def TimeClocker():
    print()

def PayChecker():
    print()



def main():
    chosenFunctofstartUp = startUp()
    if chosenFunctofstartUp == 1:
        TimeClocker()
    else:
        PayChecker()


main()