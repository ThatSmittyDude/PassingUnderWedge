#   PassingUnderWedgeGUIv1.1
#   Unix Timestamp: 1703910051

#   Author: Ausin Smith
#   ThatSmittyDude@outlook.com
#   github.com/ThatSmittyDude

#   passingunderyellow.com
#   puyinside.com

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

class WedgeCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.LF_label = QLabel('LF corner weight:')
        self.LF_entry = QLineEdit()
        self.LF_entry.returnPressed.connect(self.focus_next)

        self.LR_label = QLabel('LR corner weight:')
        self.LR_entry = QLineEdit()
        self.LR_entry.returnPressed.connect(self.focus_next)

        self.RF_label = QLabel('RF corner weight: ')
        self.RF_entry = QLineEdit()
        self.RF_entry.returnPressed.connect(self.focus_next)
        
        self.RR_label = QLabel('RR corner weight:')
        self.RR_entry = QLineEdit()
        self.RR_entry.returnPressed.connect(self.focus_next)
        
        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_Wedge)

        self.result_label = QLabel('')

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.LF_label)
        layout.addWidget(self.LF_entry)
        layout.addWidget(self.LR_label)
        layout.addWidget(self.LR_entry)
        layout.addWidget(self.RF_label)
        layout.addWidget(self.RF_entry)
        layout.addWidget(self.RR_label)
        layout.addWidget(self.RR_entry)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Set up the main window
        self.setWindowTitle('PassingUnderWedge')

        # Set black background color
        self.setAutoFillBackground(True)
        self.setPalette(self.get_dark_palette())

    def calculate_Wedge(self):
        LF = float(input("LF corner weight: "))
        LR = float(input("LR corner weight: "))
        RF = float(input("RF corner weight: "))
        RR = float(input("RR corner weight: "))
        Total = LF + LR + RF+ RR
        Wedge = ((RF + LR) / Total) * 100

        self.result_label.setText(f'Total weight: {Total}\nWedge: {Wedge}')

    def focus_next(self):
        # Move focus to the next input box
        current_widget = self.focusWidget()
        next_widget = current_widget.tabOrder()
        if next_widget:
            next_widget.setFocus()

    def get_dark_palette(self):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

        return dark_palette

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Set Fusion style for dark mode appearance
    calculator = WedgeCalculator()
    calculator.show()
    sys.exit(app.exec_())