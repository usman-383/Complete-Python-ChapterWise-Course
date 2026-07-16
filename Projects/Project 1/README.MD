# Snake-Water-Gun Game

## Overview
A Python Flask web application that lets you play Snake-Water-Gun against the computer with GUI, sounds, and animations.

## Features
- Interactive browser-based GUI
- Automatic browser launch when running `app.py`
- Sound effects (win, lose, click)
- Simple game logic: Snake > Water > Gun > Snake

## Folder Structure
project_1/
│
├── app.py
├── templates/
│ └── index.html
├── static/
│ ├── style.css
│ ├── script.js
│ ├── images/
│ └── sounds/


## How to Run
1. Install required packages:
```bash
pip install flask


2. Run the application
python app.py

3. Browser opens automatically at localhost:5000

4. Select Snake, Water, or Gun

5. Result is displayed immediately with sound effect

6. Play again as many times as you like

## Tools Used

.) Python 3.x

.) Flask

.) HTML, CSS, JavaScript


## How it works:

1. I created a Python Flask application for the game.
2. The game interface uses HTML, CSS, and JavaScript.
3. Images and sounds are stored in the 'static' folder.
4. When user runs 'python app.py', the Flask server starts.
5. The browser opens automatically at 'localhost:5000' to show the game interface.
6. User selects Snake, Water, or Gun.
7. Backend calculates computer choice and decides Win / Lose / Draw.
8. Result is displayed instantly, with sound effects.
9. User can play multiple rounds without restarting the server.

## Key points:

.) The game demonstrates knowledge of Flask, GUI, sound integration, and web-based interactivity.
.) This version runs directly with Python.
