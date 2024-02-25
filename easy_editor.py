from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget, QFileDialog
import os
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

app = QApplication([])
win = QWidget()
win.resize(700, 400)
win.setWindowTitle('Easy Editor')
btn_dir = QPushButton("Папка")
pic = QLabel('Картинка')

btn1 = QPushButton("Лево")
btn2 = QPushButton("Право")
btn3 = QPushButton("Зеркало")
btn4 = QPushButton("Резкость")
btn5 = QPushButton("Ч/Б")

list_pic = QListWidget()

v_label1 = QVBoxLayout()
v_label1.addWidget(btn_dir)
v_label1.addWidget(list_pic)

v_label2 = QVBoxLayout()
v_label2.addWidget(pic)

h_label1 = QHBoxLayout()
h_label1.addWidget(btn1)
h_label1.addWidget(btn2)
h_label1.addWidget(btn3)
h_label1.addWidget(btn4)
h_label1.addWidget(btn5)

v_label2.addLayout(h_label1)

h_label2 = QHBoxLayout()
h_label2.addLayout(v_label1)
h_label2.addLayout(v_label2)
win.setLayout(h_label2)

def filter(files, extensions):
  result = []
  for filename in files:
     for extension in extensions:
        if extension in filename:
            result.append(filename)
  return result


def showFilenamesList():
  global workdir = QFileDialog.getExistingDirectory()  # путь к папке
  files = os.listdir(workdir) # имена файлов в этой папке
  extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
  filtered_files = filter(files, extensions)
  list_pic.clear()
  for f in filtered_files:
     list_pic.addItem(f)

btn_dir.clicked.connect(showFilenamesList)


class ImageProcessor():
   def __init__(self):
      self.image = None
      self.filename = None
      self.folder = "Modified/"

   def loadImage(self, filename):
      self.filename = filename
      file_path = os.path.join(workdir, filename)
      cur_image = Image.open(file_path)
      self.image = cur_image

   def showImage(self, path):
      pic.hide()
      pixmapimage = QPixmap(path)
      width, height = pic.width(), pic.height()
      pixmapimage = pixmapimage.scaled(width, height, Qt.KeepAspectRatio)
      pic.setPixmap(pixmapimage)
      pic.show()
   def do_bw(self):
      self.image = self.image.convert("L")
      self.saveImage()
      image_path = os.path.join(workdir, self.folder, self.filename)
      self.showImage(image_path)

   def saveImage(self):
     path = os.path.join(workdir, self.folder)
     if not(os.path.exists(path) or os.path.isdir(path)):
         os.mkdir(path)
     image_path = os.path.join(path, self.filename)
     self.image.save(image_path)

workimage = ImageProcessor()
def showChosenImage():
   if list_pic.currentRow() >= 0:
       filename = list_pic.currentItem().text()
       workimage.loadImage(filename)
       image_path = os.path.join(workdir, workimage.filename)
       workimage.showImage(image_path)

list_pic.currentRowChanged.connect(showChosenImage)
btn5.clicked.connect(workimage.do_bw)

win.show()
app.exec()
