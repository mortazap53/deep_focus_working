# Deep Focus Working – Pomodoro Timer (Tkinter)

A minimal desktop Pomodoro timer built with Python and Tkinter to structure focused work sessions and breaks using the famous Pomodoro Technique.

---

## Overview

Deep Focus Working is a lightweight GUI-based productivity timer that automates structured work and break intervals. It provides a simple interface to help maintain deep focus through timed sessions and scheduled rest periods.

The application cycles automatically between work sessions, short breaks, and long breaks while visually tracking progress using checkmarks.

---

## Features

- Automated work / break session switching
- Short break after every work session
- Long break after 4 work sessions
- Countdown timer in MM:SS format
- Visual checkmarks for completed work sessions
- Reset functionality
- Clean and minimal interface
- No external dependencies

---

## Pomodoro Cycle Logic

The timer follows this sequence:

1. Work  
2. Short Break  
3. Work  
4. Short Break  
5. Work  
6. Short Break  
7. Work  
8. Long Break  

Rules:

- Odd repetitions → Work session  
- Even repetitions → Short break  
- Every 8th repetition → Long break  

A checkmark is displayed after each completed work session. 

---

## Technologies Used

- Python 3
- Tkinter (built-in GUI library)
- Math module

---

## Project Structure

deep-focus-working/  
│  
├── main.py  
├── tomato.png  
└── README.md  

---

## Requirements

- Python 3.7+
- Tkinter (included with standard Python installation)

---

## Installation
How can you download it, and work with it.

1. Clone the repository:

git clone https://github.com/your-username/deep-focus-working.git  
cd deep-focus-working  

2. Ensure `tomato.png` is located in the same directory as `main.py`.

---

## Running the Application

python main.py

The GUI window will launch.

---

## Configuration

Timer durations are defined in the source code:

WORK_MIN = 25 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20  

---

## Core Functions

starting_timer()  
Controls session flow and determines whether to start work, short break, or long break.

count_down(count)  
Handles countdown logic using window.after() to update every second.

reset()  
Stops the timer, resets repetition count, clears checkmarks, and restores the UI.

---

## Possible Improvements

- Add pause and resume functionality
- Add sound alerts when sessions end
- Add session statistics tracking
- Add dark mode
- Allow user-configurable durations from the UI
- Package using PyInstaller for distribution

---

## Educational Value

This project demonstrates:

- Event-driven programming
- GUI development with Tkinter
- Recursive countdown logic
- State management using global variables
- Basic modular function organization

It serves as a solid intermediate Python GUI application.
