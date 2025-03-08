# countdown_timer
Sure! Here’s a README.md template that briefly explains how your countdown timer code works. You can customize it based on the specific details of your implementation.

# Countdown Timer

This repository contains a simple countdown timer application built using PyQt5 and Pygame. The application allows users to set a countdown time and provides visual feedback as the timer counts down. When the timer reaches zero, a sound notification is played.

## Overview

The countdown timer consists of the following main components:

1. **User Interface**: 
   - The UI is created using PyQt5, featuring spin boxes for inputting hours, minutes, and seconds.
   - Buttons are provided to start, pause, and reset the timer.
   - A label displays the remaining time in HH:MM:SS format.

2. **Timer Functionality**:
   - The countdown is managed by a QTimer that triggers every second.
   - The remaining time is updated accordingly, decrementing seconds, minutes, and hours as necessary.
   - When the timer reaches zero, a notification sound is played.

3. **Sound Notification**:
   - The application uses the Pygame library to play a sound when the countdown ends.
   - Ensure you have a sound file (e.g., Raftiazyadam.mp3) available in the specified path for notifications.

## How It Works

### Code Structure

- **Main Application**:
  - The main application class initializes the UI and connects buttons to their respective functions.
  
- **Timer Logic**:
  - The start_timer method initiates the countdown by starting the QTimer.
  - The display method updates the UI with the remaining time and handles the countdown logic.
  - The run_out_of_time method stops the timer and plays the notification sound when the countdown reaches zero.

### Example Code Snippet

Here’s a brief snippet demonstrating how the timer is updated:

python
def display(self):
    if self.remaining_time > 0:
        self.remaining_time -= 1  # Decrement the timer
        hours, remainder = divmod(self.remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
    else:
        self.runoutof_time()

## Requirements

To run this application, you need Python installed along with the following libraries:

- PyQt5
- Pygame

You can install these libraries using pip:

bash
pip install PyQt5 pygame

## Usage

1. Clone this repository to your local machine:

   bash
   git clone https://github.com/mahdi-sh7i/countdown_timer.git
   cd countdown_timer
   
2. Ensure you have a sound file (e.g., Raftiazyadam.mp3) in the specified path within the code.

3. Run the application:

   bash
   python countdown_timer.py
   
4. Set your desired time using the spin boxes and click "Start" to begin the countdown. You can pause or reset the timer as needed.




