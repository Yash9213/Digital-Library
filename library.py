import webbrowser
print("Welcome to Library Management System!!!!!!!")
print("Choose 0 for exit and 1 for continue")
a = int(input("Enter your choice : "))
def choice(choice):
    if choice == 0:
        print("Thanks for visiting!!!")
        quit()
    elif choice == 1:
        pass
        print("1 = C")
        print("2 = Java")
        print("3 = Python")
        print("4 = C++")
        b = int(input("Enter number from 1-4 : "))
        def book(n):
            if n == 1:
                webbrowser.open("https://www.w3schools.com/c/index.php")
            elif n == 2:
                webbrowser.open("https://www.w3schools.com/java/default.asp")
            elif n == 3:
                webbrowser.open("https://www.w3schools.com/python/default.asp")
            elif n == 4:
                webbrowser.open("https://www.w3schools.com/cpp/default.asp")
            else:
                print("Invalid choice choosen")
        book(b)
        print()
        print("Thanks for Visiting!!!!")
    else:
        print("invalid choice")
        quit()
choice(a)
