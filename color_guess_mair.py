import random
import sys
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox

class ColorChooser(QWidget):
    def __init__(self):
        super().__init__()

        # Create a combo box to choose the difficulty level
        self.difficulty_box = QComboBox()
        self.difficulty_box.addItems(['Easy', 'Medium', 'Hard'])
        self.difficulty_box.currentIndexChanged.connect(self.choose_difficulty)

        # Create a label to display the number of attempts
        self.attempts_label = QLabel('Attempts: 0')

        # Create a layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.difficulty_box)
        layout.addWidget(self.attempts_label)
        self.setLayout(layout)

        # Set the window properties
        self.setWindowTitle('Color Chooser')
        self.setGeometry(500, 300, 300, 300)

    def choose_difficulty(self):
        # Remove any existing buttons
        for i in range(self.layout().count() - 2):
            widget = self.layout().itemAt(2).widget()
            self.layout().removeWidget(widget)
            widget.deleteLater()

        difficulty = self.difficulty_box.currentIndex() + 1

        # Create a list of colors based on the difficulty level
        if difficulty == 1:
            self.colors = {'Red': QColor('red'), 'Green': QColor('green'), 'Blue': QColor('blue')}
        elif difficulty == 2:
            self.colors = {'Red': QColor('red'), 'Green': QColor('green'), 'Blue': QColor('blue'), 'Yellow': QColor('yellow')}
        elif difficulty == 3:
            self.colors = {'Red': QColor('red'), 'Green': QColor('green'), 'Blue': QColor('blue'), 'Yellow': QColor('yellow'), 'Purple': QColor('purple')}

        # Choose a random color as the correct answer
        self.answer = random.choice(list(self.colors.keys()))

        # Create buttons for each color
        self.buttons = []
        for color_name, color in self.colors.items():
            button = QPushButton(color_name)
            button.setStyleSheet(f'background-color: {color.name()}; color: white;')
            button.clicked.connect(self.check_answer)
            self.buttons.append(button)
            self.layout().addWidget(button)
    #Check button click if it's correct the game ends, if not it's counting the attempts
    def check_answer(self):
        sender = self.sender()
        if sender.text() == self.answer:
            sender.setEnabled(False)
            for button in self.buttons:
                if button != sender:
                    button.setEnabled(False)
            self.attempts_label.setText('Correct! The game ends pls restart, if u want to play Again!')
            
        else:
            attempts = int(self.attempts_label.text().split(':')[1]) + 1
            self.attempts_label.setText(f'Attempts: {attempts}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooser = ColorChooser()
    chooser.show()
    sys.exit(app.exec())