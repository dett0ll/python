name = input ("Enter Name")

match name:
    case "Max" | "checo":
        print("RB")
    case "charles" | "sainz":
        print("Fer")
    case "lewis" | "George":
        print ("MAMG")
    case _:
        print("No information")
