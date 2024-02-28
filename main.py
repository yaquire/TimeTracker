border = '~'
baseRate = 11

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
    print('~CLOCK IN & OUT ahs been chosen~')
    while True:
        clockIn1 = input('Clock In (24hr): ')
        try:
            clockIn1 = int(clockIn1)
            break
        except:
            ValueError()
            print('Please Enter a number (integer)')
    
    while True:
        clockOut = input('Clock Out (24hr): ')
        try:
            clockOut = int(clockOut)
            break
        except:
            ValueError()
            print('Please Enter a number (integer)')

    while True:
        breakTime = input('Break (hrs): ')
        try:
            breakTime = float(breakTime)
            break
        except:
            ValueError()
            print('Please Enter a number (decimal/integer)')

    clockIn1 = str(clockIn1)
    clockOut = str(clockOut)

    clockOutMinutes = int(clockOut[-2]+clockOut[-1])/60
    clockIn1Minutes = int(clockIn1[-2]+clockIn1[-1])/60

    print(clockOutMinutes ,clockIn1Minutes)



    totalHours = ()
    
             

def PayChecker():
    print()



def main():
    chosenFunctofstartUp = startUp()
    if chosenFunctofstartUp == 1:
        TimeClocker()
    else:
        PayChecker()


main()