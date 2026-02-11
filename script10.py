#lab3 Question 4
color=(input("enter a color name:red,yellow,green"))
if color=='' :
    print("you have to enter a color")
match color:
        case "red" :
            print("stop")
        case "yellow" :
            print("ready")
        case "green" :
            print("go")


