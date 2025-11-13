# 📚 Library Management System (Basic Console Version)

This is a simple **Python-based Library Management System** that lets users open learning resources for various programming languages directly from the console using their web browser.

## 🚀 Features

- Console-based interface.
- Lets users choose between four programming languages:
  - **C**
  - **Java**
  - **Python**
  - **C++**
- Opens the selected language's learning page from **W3Schools** in the default browser.
- Simple and beginner-friendly script demonstrating:
  - User input handling
  - Conditional statements
  - Function usage
  - Integration with the `webbrowser` module

---

## 🧩 How It Works

1. The program welcomes the user and prompts for an initial choice:
   - **0** → Exit the program  
   - **1** → Continue to select a language

2. If the user chooses to continue:
   - They are presented with a list of programming languages.
   - After choosing one (1–4), the script automatically opens the corresponding **W3Schools** learning page in their default web browser.

3. After completion, the program thanks the user and exits.

---

## 💻 Example Run

Welcome to Library Management System!!!!!!!
Choose 0 for exit and 1 for continue
Enter your choice : 1
1 = C
2 = Java
3 = Python
4 = C++
Enter number from 1-4 : 3
(Automatically opens W3Schools Python page)
Thanks for Visiting!!!!

yaml
Copy code

---

## 🛠️ Requirements

- Python 3.x
- Internet connection (to open web pages)
- No external libraries needed — uses built-in Python modules only.

---

## 🧠 Modules Used

- **webbrowser** → Opens the selected W3Schools page in the default browser.

---

## 🧾 Code Structure

89e869dd-f21b-4ebd-91be-2259a30209ec.py
│
├── print() # Display welcome message
├── input() # Take user choice
├── choice(choice) # Handle main choice (exit or continue)
│ ├── book(n) # Handle book/language selection
│ └── webbrowser.open() # Open W3Schools link
└── quit() # Exit program

yaml
Copy code

---

## ⚡ Usage

To run the program:
```bash
python 89e869dd-f21b-4ebd-91be-2259a30209ec.py
📄 License
This project is free to use for educational and personal purposes.

👨‍💻 Author
Yash Kumar
