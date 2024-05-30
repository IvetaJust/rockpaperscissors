I. Justaite Vilnius University Data Science Masters Student
Big Data Module
Individual Task 2 
2024

# Game: Rock, Paper, Scissors

This is a simple command-line game Rock, Paper, Scissors. In this version of the game, we play against the computer in a best-of-three format, where tie rounds do not count towards the score.

* Rock crushes Scissors.
* Scissors cuts Paper.
* Paper covers Rock.

## Prerequisites & Other Information

* Docker must be installed on the computer.
* Docker Image Tag is ````ivjust/rockpaperscissors:latest```` and if needed, can be pulled with command ```docker pull ivjust/rockpaperscissors:latest```.
* Mac was used for development, other environments not tested.
* No dependencies on external libraries, thus, requirements.txt file is empty and not included in the Dockerfile.

## Playing the Game

### Preparation

1. Ensure the right directory is set, example code below. Adjust it based on the location of this file in computer:

```cd ~/Desktop/Masters\ Semester\ 2/Big\ Data/Big\ Data\ Task\ 2/RockPaperScissors```

2. Run this command to build the new docker image from the Dockerfile:

```docker build -t rockpaperscissors .```

#### Optional | Testing the Docker 

* List all available Docker images, run ```docker images``` 
* List rockpaperscissors image, run ````docker images rockpaperscissors````



### Starting the Game

Run this code and get ready to play:

```docker run -it rockpaperscissors```

After running the code above, you are prompted to enter your choice: rock, paper, or scissors. 

Once you submit your choice, a countdown from 3 to 1 begins, culminating in "SHOOT!" where the computer randomly selects its choice. 

Both your choice and the computer's choice are displayed with corresponding visual. 

The game then compares the choices to determine the winner of the round, announcing whether it’s a tie, you win, or the computer wins. 

The game keeps track of the score, ignoring tie rounds, and continues until either you or the computer wins two non-tie rounds, declaring the overall winner and ending the game.

Press ```Enter``` to play again. 
