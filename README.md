# README
Quickly-made Chrome Dinosaur running game used to anticipate challenges and workload when tutoring!

Made with `pygame` (and some nostalgia :relaxed:)

# Quickstart
1. [Install Python](https://www.python.org/downloads/) if you don't have it on your computer; you'll need this to run the game.
2. Download the code: if you have `git` on your computer, clone the repo (see command below). Otherwise, download the code by clicking on `Code` and `Download ZIP`, and then extract the code by unzipping the `.zip` file. If you've chosen to clone the repo, you can use the command `git clone https://github.com/srcoulombe/dino_runner.git`.
3. Create a virtual environment to make sure installing `pygame` in `step 5` won't affect any other `pygame` project you might have. To do this, open the command line, navigate to the folder called `dino_runner` (or the name you specified when cloning/downloading/extracting the repo), and use the command `python3 -m venv dino_runner_venv`. 
**NOTE** if you get an error running this command, try `python -m venv dino_runner_venv`. If you still have problems, open a new `Issue` in the `GitHub` repo to explain what you did (please include the error message you got).
4. Activate the virtual environment: open the command line, navigate to the folder called `dino_runner` (or the name you specified when cloning/downloading/extracting the repo), and use `source dino_runner_venv/bin/activate` if you're using MacOS or Linux as your operating system, or `.\dino_runner_venv\Scripts\activate` if you're using Windows.
5. Install `pygame` (you'll need this to run the game) in your virtual environment by using `pip install pygame`. Alternatively, you can use `pip install -r requirements.txt`.
6. You can now run the game by entering the following in your command line: `python3 main.py` (or `python main.py`).

# Extending this Codebase
Feel free to fork this repo if you'd like to use this codebase as a starting point!

# Tutoring Notes
## Recurring Challenges:
I noticed the following were frequent topics that either led to insightful discussions or to problems in the codebase:

- When to compartmentalize functionality in classes or outside classes
  (e.g., if the collision detection functionality should be defined in the `DinoAvatar`
  class or as a stand-alone function in the `main.py` file).
- `pygame`'s coordinate system places the origin `(0,0)` at the top-left corner.
- Reading code is tougher than writing code! Documentation, commenting, and journaling helps!

## What Now?
Completing the base game seemed to be satisfying and led to a feeling of accomplishment, 
but the question of "What now?" kept popping up. In anticipation of different tutorees' 
interests and preferences, I've identified the following as possible areas for continuing
work:

- Adding advanced jumping functionality (to improve general Python programming and game development skills)
  - Prolonging jumping (high jumps and low jumps)
  - Ducking in mid-air stopping the jump
- Adding a leaderboard (to learn about serialization and JSON)
- Adding `C H A O S \t M O D E` (to improve general Python programming and game development skills)
  - Inverting the game screen
  - Inverting keyboard commands
  - Inverting obstacle-generation logic (floating cacti, walking bird)
  - Reversing the game (stop, and move from right -> left rather than left -> right)
