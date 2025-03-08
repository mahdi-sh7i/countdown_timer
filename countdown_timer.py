from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QSpinBox
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import sys
import pygame  # Import pygame for audio playback

class UI(QMainWindow):
    def __init__(self):  
        super(UI, self).__init__()
        uic.loadUi("countdown_timer.ui", self)

        self.setWindowTitle("Countdown Timer")

        # Find UI elements
        self.button_reset = self.findChild(QPushButton, "btn_reset")
        self.button_start = self.findChild(QPushButton, "btn_start")
        self.button_pause = self.findChild(QPushButton, "btn_pause")
        self.label_countdown = self.findChild(QLabel, "label_countdown")
        self.spinbox_hours = self.findChild(QSpinBox, "spinbox_hours")
        self.spinbox_mins = self.findChild(QSpinBox, "spinbox_mins")
        self.spinbox_secs = self.findChild(QSpinBox, "spinbox_secs")
        
        # Connect buttons to functions
        self.button_reset.clicked.connect(self.reset_btn)
        self.button_start.clicked.connect(self.start_btn)
        self.button_pause.clicked.connect(self.pause_btn)

        # Initialize timer
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.display)
        
        # Initialize time variables
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self._flag = 0

        # Initialize Pygame mixer
        pygame.mixer.init()
        
        # Show the UI
        self.show()

    def reset_btn(self):
        """Reset the countdown timer."""
        self.countdown_timer.stop()
        self.button_start.setEnabled(True)
        self.button_pause.setEnabled(False)
        self.spinbox_hours.setEnabled(True)
        self.spinbox_mins.setEnabled(True)
        self.spinbox_secs.setEnabled(True)
        
        # Reset spinboxes and labels
        self.spinbox_hours.setValue(0)
        self.spinbox_mins.setValue(0)
        self.spinbox_secs.setValue(0)
        self.label_countdown.setText("00:00:00")

    def start_btn(self):
        """Start the countdown timer."""
        self.hours = self.spinbox_hours.value()
        self.mins = self.spinbox_mins.value()
        self.secs = self.spinbox_secs.value()
        
        self.button_pause.setEnabled(True)
        self.button_start.setEnabled(False)
        self.spinbox_hours.setEnabled(False)
        self.spinbox_mins.setEnabled(False)
        self.spinbox_secs.setEnabled(False)

        # Start the timer
        self.countdown_timer.start(1000)  # Update every second


    def pause_btn(self):
        """Pause the countdown timer."""
        self.button_start.setEnabled(True)
        self.button_pause.setEnabled(False)
        
        # Enable spinboxes for user input
        self.spinbox_hours.setEnabled(True)
        self.spinbox_mins.setEnabled(True)
        self.spinbox_secs.setEnabled(True)

        # Stop the timer
        self.countdown_timer.stop()

        # Stop the timer
        pygame.mixer.music.stop()

    def display(self):
        """Update the countdown display."""
        if self.secs > 0:
            self.secs -= 1
        elif self.mins > 0:
            self.mins -= 1
            self.secs = 59
        elif self.hours > 0:
            self.hours -= 1
            self.mins = 59
            self.secs = 59
        else:
            # Time's up
            self.run_out_of_time()

            # Load and play music
            #pygame.mixer.music.load("/home/mahdi/project/musix/Raftiazyadam.mp3")  # Replace with your music file path
            #pygame.mixer.music.play()
            #pygame.mixer.music.stop()
            return
        
        # Update label
        fmt = '{:02d}:{:02d}:{:02d}'
        self.label_countdown.setText(fmt.format(self.hours, self.mins, self.secs))

    def run_out_of_time(self):
        """Actions to take when the countdown reaches zero."""
        self.countdown_timer.stop()
        # Optionally play sound or show message box here
        print("Time's up!")
        self.label_countdown.setText("Time's up")
        pygame.mixer.music.load("/home/mahdi/all_pro/countdown_timer/count/music/Raftiazyadam.mp3")  # Replace with your music file path
        pygame.mixer.music.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
