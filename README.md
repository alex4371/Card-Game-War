# Card-Game-War
This is a project fucused on understanding the mathematics behind the card game war.
This is for a research co-op program.

The main goal is to understand why the game ends in even or odd lenghts at different frequencies based on small changes in the rules.

The file "War MultiSystem.py" does the majority of the processing.

If there are any errors in a single game the program "Debugging Hands of War.py" steps through the hands of that game to reveal where and error is coming from. You must manually change the variables hand1, hand2, and game order to get the correct step through.

The terms WF, LF and RF mean "Winner First", "Loser First", and "Random First"
This refers to the order in which the cards are returned to the bottom of the deck after each hand.
The random first means that each hand the order is randomly chosen between Winner and Loser First.
