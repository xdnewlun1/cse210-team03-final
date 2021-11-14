# Game Design Document
---

**Team Name:**


Team 03

**Team Members:**

Anita Woodford  –  Configuration Manager, Project Manager, Game Designer

Lazaro Felizardo Matola - Game Designer, Programmer, Assistant Tester/ Debugger

Xander Newlun – Lead Programmer, Game Designer, Testing/Debugger

Zach Robker - Assistant Project Manager, Game Designer, Programmer, Animator

**Game Title:**

Break the Scale

**Game Mockup:**

See Mockup File in Documentation Folder

**Game Description:**

Break the Scale is a 2d style game for the computer terminal based on the movie Cloudy with a Chance of Meatballs.

**Game Mode(s):**

Single-player

**Target Audience:**

Age 5 -10

**Goal:**

The game’s goal is to avoid the food as long as possible. The timer will continually count up, and when you eventually lose, it will save your time and check to see if you made the leaderboard. Your secondary goal is to make the leaderboard on the hard difficulty.

**Technical Software:**

We will be using Google Docs, Google Spreadsheets, Visual Code Studios, Arcade Library, Arcade Library camera first person, and GUI Camera from Arcade Library, photoshop for images,  and Python.

# Gameplay
---
**Objective:**

Food will appear from the sky and move down the screen. The food frequency will depend on the level chosen by the user.

Weight Points gained by consuming food the weight will be at the top of the screen

Destructive: Avoid unhealthy food choices. Eating unhealthy food will cause you to gain more weight. 

Helpful: Eat healthy food choices to gain the least amount of weight

Health recovery: Collect Pepto(change to exercise) / Exercise to lose weight

**Game characters:**

There is one main character in this game. In addition, the user may choose a male or female character.

**Game controls:**

Left arrow

Right arrow

Esc button

Keyboard presses to enter initials

Mouse presses to select a character, levels, and ring bell

**Gameplay mode:**

There are three different game levels, Easy, Medium, and Hard. At the Easy level, the player will be able to play effortlessly while healthy and unhealthy foods fall from the sky at a slower pace, while the rate of speed will increase in the medium and hard levels.

**Summary of Game Options:**

A tutorial will appear on the menu option during the initial startup of the game. The rules will show up on the Options menu too. This feature will always be in the menu if the player forgets any controls and regulations. As of now, there aren’t any different game modes, but the player can increase or decrease the game’s difficulty. 

A leader board will appear with the top ten scores in hard difficulty. The game’s rating system is the amount of time the player went before they hit the max amount of weight. 

**Audio Direction:**

Predesigned audio,  downloaded from the free website. There will be chomping or eating noises, a bell ringing, popping noises for explosions, and background music.

# Play Flow
---
**Featured List**

**Main Scene:**

* Sprite: Table - for the start of the game (2)
* Add a background of diner or restaurant (2)
* Sprite: Dinner Menu:  For menu items  (1)
  * Play game (1)
    * Easy (2)
    * Medium (2)
    * Hard (2)
  * Select Game Level (2)
  * Options button (2)
  * Help Instructions (1)
    * Leader board (2)
  * Select Character Male / Female (3)
  * Exit button (2)

**Game Scene:**

* The game screen opens on chosen level (1)
  * Easy (2)
    * Healthy/ unhealthy foods fall (1)
    * slower pace (2)
    * The player reaches max weight limit scale breaks & the game ends (2)
    * The game ends at 600 lbs (3)
  * Medium (2)
    * A mix of Healthy and unhealthy food falls (2)
    * medium pace (2)
    * The player reaches max weight limit scale breaks and game ends (2)
    * The game ends at 500 (3)
  * Hard (2)
    * Unhealthy food falls less healthy food falls (2)
    * Fast Pace (2)
    * When the player reaches max weight (2)
    * The game ends at 400 (3)

**Game Scene Continue:**

* Draw Background (1)
  * Red Lobster in the background (3)
* Draw Sprite: Ground for main gameplay (1)
* Draw Sprite: Sky for main gameplay (1)
* Draw sprites Trees - main gameplay (2)
* Draw/ load Sprites Player (1)
* Players interact with the dinner bell to start the game (2)
  * The dinner bell is shown (2)
  * The dinner bell rings (3)
  * Dinner bell disappears (2)
* The game begins (1)
* Load Scale/ score (1)
  * Start the weight at 150 (2)
* Load timer at the top in the middle (1)
* User-controlled paddle (1)
  * left or right (1)
* Food Falls from the sky (1)
  * hamburger, candy, donut, apple, carrots, pizza (2)
* Collision detection (1)
* Player eats food (1)
  * Play a crunch sound (3)
  * Unhealthy choices you gain weight (1)
    * 20 - 50 lbs (2)
  * Load person getting heavier as they eat food (3)
  * Healthy choices and you gain less ­(1)
    * The same goes for healthy food (1)
    * 5 lbs (2)
* Pepto (1)
  * Load player sprite losing weight (3)
  * Takes weight off by 10 for easy (2)
* Exit / ESC button bottom right  (1)

**Help Scene:**

* Load sprites (1)
* Table background, players (2)
  * Food menu (1)

**Help Scene Continue:**

* Help text – instruction to play (1)
* Exit button or back button returns to the main menu (1)
* Bell to start gameplay (2)

**Leaderboard:**

* Draw Table (2)
* Draw dinner menu used to display (1)
* Draw Café background (3)
* Top 10 winners (2)
  * Get input from the user of three-letter initial (2)
* Exit button (1)
* Back button return main menu (1)

**Lose Scene:**

* Person explodes when they hit the max limit for level (3)
  * Pop sound (3)
  * Words flashing heart attack (3)
  * Groan (3)
* Announcement -  you lose (1)
* Restart button (1)
* Quit button (1)
* Main Menu (1)
