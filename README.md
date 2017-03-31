# HangmanGame
For the Intro to Python Programming course at CS @ Illinois SAIL 2017.

## Program Structure
Each line of pseudocode will have this structure:
```
Line of pseudocode [topics covered]
```

```
Import string of lowercase letters from "string" module [modules]

Ask for player's name [input]
Ask for number of attempts, make sure it is positive and less than 26 [input, casting, decomposition, exceptions]
Open words file & select random word [file I/O, lists, modules, scalability (if there is time remaining)]

While there are attempts or letters remaining [While loop]
    Print the current state of game [for loop]
    Ask for next letter, make it lower(), make sure input is a single letter that hasn't been guessed before [input, decomposition, exceptions, sets]
    If letter is in the word [sets]
        Notify user that the letter is in the word [string interpolation]
    Else
        Decrement attempt counter [Decrement operator]
        Notify user that the letter is not in the word [String interpolation]

If word is solved
    Notify user of win
Else
    Notify user of loss

Give player the option to try again
```
