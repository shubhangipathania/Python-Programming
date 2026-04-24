#match case statements 
day=int(input("Enter the no of day of the week:"))
match day:

    case 1:
        print("SUNDAY")
        print("Enjoy your holiday")

    case 2:
        print("MONDAY")
        print("It is the starting of the week.")

    case 3:
        print("Tuesday")
        print("JAI BAJRANG BALI")

    case 4:
        print("WEDNESDAY")
        print("It is a working day")

    case 5:
        print("THURSDAY")
        print("You are pushing well through your week")

    case 6:
        print("FRIDAY")
        print("It is going to be the weekend.")

    case 7:
        print("SATURDAY")
        print("It is finally weekend.")

    case _:
        print("Invalid choice")