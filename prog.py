import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
from random import randint
import os


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.but.clicked.connect(self.paint)
        self.size = (0, 75)


    def paint(self):
        a = "yellow"
        im = Image.new("RGB", (591, 431), (255, 255, 255))
        im1 = Image.new("RGB", (130, 130), (255, 255, 255))
        im2 = Image.new("RGB", (130, 130), (255, 255, 255))
        im3 = Image.new("RGB", (130, 130), (255, 255, 255))
        im4 = Image.new("RGB", (130, 130), (255, 255, 255))
        im5 = Image.new("RGB", (130, 130), (255, 255, 255))
        im6 = Image.new("RGB", (130, 130), (255, 255, 255))
        size1 = randint(0, 65)
        size2 = randint(0, 65)
        size3 = randint(0, 65)
        size4 = randint(0, 65)
        size5 = randint(0, 65)
        size6 = randint(0, 65)
        draw1 = ImageDraw.Draw(im1)
        draw2 = ImageDraw.Draw(im2)
        draw3 = ImageDraw.Draw(im3)
        draw4 = ImageDraw.Draw(im4)
        draw5 = ImageDraw.Draw(im5)
        draw6 = ImageDraw.Draw(im6)
        draw1.ellipse((65 - size1, 65 - size1, 65 + size1, 65 + size1), fill=a)
        draw2.ellipse((65 - size2, 65 - size2, 65 + size2, 65 + size2), fill=a)
        draw3.ellipse((65 - size3, 65 - size3, 65 + size3, 65 + size3), fill=a)
        draw4.ellipse((65 - size4, 65 - size4, 65 + size4, 65 + size4), fill=a)
        draw5.ellipse((65 - size5, 65 - size5, 65 + size5, 65 + size5), fill=a)
        draw6.ellipse((65 - size6, 65 - size6, 65 + size6, 65 + size6), fill=a)
        im.save("res.jpg")
        im1.save("res1.jpg")
        im2.save("res2.jpg")
        im3.save("res3.jpg")
        im4.save("res4.jpg")
        im5.save("res5.jpg")
        im6.save("res6.jpg")
        PM = QPixmap("res.jpg")
        self.label.setPixmap(PM)
        PM1 = QPixmap("res1.jpg")
        self.lab_1.setPixmap(PM1)
        PM2 = QPixmap("res2.jpg")
        self.lab_2.setPixmap(PM2)
        PM3 = QPixmap("res3.jpg")
        self.lab_3.setPixmap(PM3)
        PM4 = QPixmap("res4.jpg")
        self.lab_4.setPixmap(PM4)
        PM5 = QPixmap("res5.jpg")
        self.lab_5.setPixmap(PM5)
        PM6 = QPixmap("res6.jpg")
        self.lab_6.setPixmap(PM6)
        os.remove("res.jpg")
        os.remove("res1.jpg")
        os.remove("res2.jpg")
        os.remove("res3.jpg")
        os.remove("res4.jpg")
        os.remove("res5.jpg")
        os.remove("res6.jpg")

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
