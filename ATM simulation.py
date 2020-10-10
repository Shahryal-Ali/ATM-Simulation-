print("Welcome to BMO")
restart = 'Y'
actual_pin = 1234
balance = 100
chance = 3

while chance >=0:
    if restart in ('No','NO','no','n','N','noo','Noo'):
        break
    else:
        pin = int(input("Please enter your 4 digit pin: "))
        if pin == actual_pin:
            print("You've entered correct pin\n")
            while restart not in ('No','NO','no','n','N','noo','Noo'):
                print('Please enter 1 to check your balance')
                print('Please enter 2 to make a withdrawal')
                print('Please enter 3 to make a deposit')
                print('Please enter 4 to get the card back\n')
                option = int(input("what would you like to do today? "))
                if option == 1:
                    print("your balance is $",balance)
                    restart = input("would you like to do anything else?")
                    if restart in ('No','NO','no','n','N','noo','Noo'):
                        print("Thank you for stopping by")
                        break
                elif option == 2:
                    withdraw = float(input("How much would you like to withdraw today?"))
                    if withdraw > balance:
                        print("insufficient balance")
                    else:
                        balance = balance - withdraw
                        print("your balance after withdrawal is $",balance)
                        restart = input("would you like to do anything else?")
                        if restart in ('No', 'NO', 'no', 'n', 'N', 'noo', 'Noo'):
                            print("Thank you for stopping by")
                            break
                elif option == 3:
                    deposit = float(input("How much would you like to deposit today?"))
                    balance = balance + deposit
                    print("your balance after deposit is $", balance)
                    restart = input("would you like to do anything else?")
                    if restart in ('No', 'NO', 'no', 'n', 'N', 'noo', 'Noo'):
                        print("Thank you for stopping by")
                        break
                elif option == 4:
                    print("your card has been returned\n")
                    print("Thank you for stopping by")
                    break
                else:
                    print("Please enter the correct number")
                    restart = 'Y'
        elif pin != actual_pin:
            print("Incorrect pin\n")
            chance = chance -1
            if chance > 1:
                print("you only have ",chance," chances remaining")
            elif chance == 1:
                print("you only have ",chance," chance remaining")
            elif chance == 0:
                print("No more chances available")
                break


