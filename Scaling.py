from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from jes4py import *
app = QApplication([])


def scaleUp():

    scaleUpButton.hide()
    scaleDownButton.hide()
    textLabel.hide()

    textLabel2.show()
    scaleDownButton3.show()
    scaleDownButton4.show()

def scaleUp2():

  textLabel2.hide()
  scaleDownButton3.hide()
  scaleDownButton4.hide()

  textLabel1 = QLabel("Please choose the percentage that you want to scale up with")
  textLabel1.setAlignment(Qt.AlignCenter)
  layout.addWidget(textLabel1)

  slider.show()
  valueLabel.show()

  scaleDownButton5 = QPushButton("Perform Scale Up")
  scaleDownButton5.clicked.connect(percentageScaleUp)
  buttonLayout.addWidget(scaleDownButton5, alignment=Qt.AlignCenter)

  timer.start(100)

def percentageScaleUp(): 
    scale_percentage = slider.value()
    src = makePicture("./Photos/squared.png")
    src_width = getWidth(src)
    src_height = getHeight(src)
    target_width = int(src_width * (1 + scale_percentage / 100))
    target_height = int(src_height * (1 + scale_percentage / 100))
    canvas = makeEmptyPicture(target_width, target_height)

    scaling_factor_x = src_width / target_width
    scaling_factor_y = src_height / target_height

    for target_x in range(target_width):
        for target_y in range(target_height):
            source_x = int(target_x * scaling_factor_x)
            source_y = int(target_y * scaling_factor_y)
            color = getColor(getPixel(src, source_x, source_y))
            setColor(getPixel(canvas, target_x, target_y), color)

    save_path = "./Photos/scaled_canvas.png"  # Replace with the desired save path
    writePictureTo(canvas, save_path)

    
    pixmap = QPixmap(save_path)
    photoLabel.setPixmap(pixmap)
    
    photoLabel.setAlignment(Qt.AlignCenter)



def scaleUp3():
  textLabel2.hide()
  scaleDownButton3.hide()
  scaleDownButton4.hide()


  textLabel3 = QLabel("Please enter the number of times you want to scale up with")
  textLabel3.setAlignment(Qt.AlignCenter)
  layout.addWidget(textLabel3)

  textBox.show()

  scaleDownButton6 = QPushButton("Perform Scale up")
  scaleDownButton6.clicked.connect(multipleScaleUp)
  buttonLayout.addWidget(scaleDownButton6, alignment=Qt.AlignCenter)

def multipleScaleUp(): 
    input = textBox.text()
    if input.strip() != "":
       input = int(input)
    print(input)
    scale_percentage = input * 100
    src = makePicture("./Photos/squared.png")
    src_width = getWidth(src)
    src_height = getHeight(src)
    target_width = int(src_width * (1 + scale_percentage / 100))
    target_height = int(src_height * (1 + scale_percentage / 100))
    canvas = makeEmptyPicture(target_width, target_height)


    scaling_factor_x = src_width / target_width
    scaling_factor_y = src_height / target_height


    for target_x in range(target_width):
        for target_y in range(target_height):
            source_x = int(target_x * scaling_factor_x)
            source_y = int(target_y * scaling_factor_y)
            color = getColor(getPixel(src, source_x, source_y))
            setColor(getPixel(canvas, target_x, target_y), color)

    save_path = "./Photos/scaled_canvas.png"  
    writePictureTo(canvas, save_path)

    pixmap = QPixmap(save_path)
    photoLabel.setPixmap(pixmap)
    photoLabel.setAlignment(Qt.AlignCenter)


def scaleDown():

    scaleUpButton.hide()
    scaleDownButton.hide()
    textLabel.hide()

    slider.show()
    valueLabel.show()
    textLabel1 = QLabel("Please choose the percentage that you want to scale down with")
    textLabel1.setAlignment(Qt.AlignCenter)
    layout.addWidget(textLabel1)

    scaleDownButton2 = QPushButton("Perform Scale Down")
    scaleDownButton2.clicked.connect(scaleDown2)
    buttonLayout.addWidget(scaleDownButton2, alignment=Qt.AlignCenter)

    timer.start(100)


def scaleDown2():
    
    percentage = slider.value()
    src = makePicture("./Photos/squared.png")
    src_width = getWidth(src)
    src_height = getHeight(src)
    target_width = int(src_width * (1 - percentage / 100))
    target_height = int(src_height * (1 - percentage / 100))
    canvas = makeEmptyPicture(target_width, target_height)

    scaling_factor_x = src_width / target_width
    scaling_factor_y = src_height / target_height

    for target_x in range(target_width):
        for target_y in range(target_height):
            source_x = int(target_x * scaling_factor_x)
            source_y = int(target_y * scaling_factor_y)
            color = getColor(getPixel(src, source_x, source_y))
            setColor(getPixel(canvas, target_x, target_y), color)

    save_path = "./Photos/scaled_canvas.png"  
    writePictureTo(canvas, save_path)

    
    pixmap = QPixmap(save_path)
    photoLabel.setPixmap(pixmap)

    photoLabel.setAlignment(Qt.AlignCenter)


def updateValue():
    
    valueLabel.setText(f"Selected Value: {slider.value()}")


window = QWidget()
window.setWindowTitle("Scaling")
window.resize(500, 500)  

layout = QVBoxLayout()

photoLabel = QLabel()
photoLabel.setAlignment(Qt.AlignCenter)

image_path = "./Photos/squared.png"  


pixmap = QPixmap(image_path)
photoLabel.setPixmap(pixmap)


layout.addWidget(photoLabel)

textLabel = QLabel("This is the original image, please choose the opreation that you want to perform")
textLabel.setAlignment(Qt.AlignCenter)


layout.addWidget(textLabel)


buttonLayout = QHBoxLayout()

scaleUpButton = QPushButton("Scale Up")
scaleUpButton.clicked.connect(scaleUp)
buttonLayout.addWidget(scaleUpButton, alignment=Qt.AlignLeft)


scaleDownButton = QPushButton("Scale Down")
scaleDownButton.clicked.connect(scaleDown)
buttonLayout.addWidget(scaleDownButton, alignment=Qt.AlignRight)


slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.hide()


layout.addLayout(buttonLayout)
layout.addWidget(slider)


valueLabel = QLabel("Selected Value: ")
valueLabel.setAlignment(Qt.AlignCenter)
layout.addWidget(valueLabel)
valueLabel.hide()

textLabel2 = QLabel("Please choose if you want to scale up by percentage or number of times")
textLabel2.setAlignment(Qt.AlignCenter)
layout.addWidget(textLabel2)
textLabel2.hide()

scaleDownButton3 = QPushButton("Percentage")
scaleDownButton3.clicked.connect(scaleUp2)
buttonLayout.addWidget(scaleDownButton3, alignment=Qt.AlignCenter)
scaleDownButton3.hide()

scaleDownButton4 = QPushButton("Multiple times")
scaleDownButton4.clicked.connect(scaleUp3)
buttonLayout.addWidget(scaleDownButton4, alignment=Qt.AlignCenter)
scaleDownButton4.hide()

textBox = QLineEdit()
layout.addWidget(textBox)
textBox.hide()

window.setLayout(layout)

timer = QTimer()
timer.timeout.connect(updateValue)

window.show()

app.exec_()