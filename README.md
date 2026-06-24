# CLI Password Generator

## Overview

This project is a Command Line Interface (CLI) Password Generator built with Python. The application allows users to generate random passwords of a custom length and choose whether to include uppercase letters, numbers, and special characters. The main goal of this project was to practice Python fundamentals such as functions, loops, input validation, exception handling, modules, and program organization while building a practical tool.

## Features

* Generate random passwords of a user-defined length.
* Include or exclude uppercase letters.
* Include or exclude numbers.
* Include or exclude special characters.
* Input validation for password length.
* Input validation for yes/no user choices.
* Uses Python's `secrets` module for secure random password generation.
* Organized using multiple functions for better readability and maintainability.

## How It Works

When the program starts, the user is asked to enter the desired password length. The program validates the input and ensures the length is at least four characters. After that, the user is asked whether uppercase letters, numbers, and special characters should be included in the generated password.

Based on the user's selections, a character set is created using constants provided by Python's `string` module. The program then randomly selects characters from the chosen character set using the `secrets.choice()` function and builds a password of the requested length. Finally, the generated password is displayed in the terminal.

## Technologies Used

* Python 3
* `secrets` module
* `string` module

## Challenges Faced

One of the first challenges I faced was validating user input. Initially, invalid inputs would cause errors or restart larger parts of the program. To solve this, I used `while` loops and `try-except` blocks to repeatedly prompt the user until valid input was provided.

Another challenge was handling multiple yes/no questions. My first implementation used separate functions for each question, which resulted in repetitive code. After recognizing this repetition, I refactored the program and created a single reusable validation function that accepts a prompt as an argument. This reduced duplication and made the code easier to maintain.

I also learned about secure random password generation. At first, I was unaware of the difference between the `random` and `secrets` modules. After researching password generation best practices, I chose the `secrets` module because it is designed for security-sensitive tasks such as password generation.

Later, I experimented with ensuring that generated passwords contained at least one character from selected categories such as uppercase letters, numbers, and special characters. While implementing this feature, I encountered design questions related to passing data between functions and avoiding global variables. Although my first solution used a global variable, I recognized that a better design would involve passing information directly between functions. This is an area I plan to improve in a future version of the project.

## What I Learned

Through this project, I practiced:

* Function design
* Input validation
* Exception handling
* Loops and conditionals
* String manipulation
* Using Python standard library modules
* Reducing code duplication
* Basic software design principles
* Thinking algorithmically when solving problems

Most importantly, I learned how to break a problem into smaller pieces and solve it step by step rather than trying to build everything at once.

## Future Improvements

Planned improvements for Version 2:

* Guarantee at least one character from each selected category.
* Remove the use of global variables.
* Improve password generation logic.
* Add a menu system.
* Generate multiple passwords at once.
* Add password strength feedback.
* Save generated passwords to a file.

## Project Structure

```text
password-generator/
│
├── main.py
└── README.md
```

## Running the Program

```bash
python password_generator.py
```

Follow the prompts in the terminal to generate a password.

## Author
Md. Sazid Al Mafi <br>
Built as a beginner Python project to practice programming fundamentals and CLI application development.
