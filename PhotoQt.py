from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QListWidget, QComboBox, QVBoxLayout, QHBoxLayout, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageEnhance, ImageFilter
import sys
import os


working_directory = ""
class Widget(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("PhotoQt")
        self.resize(900, 700)

        # Widgets
        self.btn_folder = QPushButton("Folder")
        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.mirror = QPushButton("Mirror")
        self.sharpness = QPushButton("Sharpen")
        self.gray = QPushButton("B/W")
        self.saturation = QPushButton("Color")
        self.contrast = QPushButton("Contrast")
        self.blur = QPushButton("Blur")

        self.picture_box = QLabel("Image will appear here")

        self.file_list = QListWidget()

        # Composition of classes using ONE widget instance
        self.editor = Editor(self) 


        # Combo Box
        items = ["Original","Left", "Right", "Mirror","Sharpen", "B/W", "Color", "Contrast", "Blur"]
        self.filter_box = QComboBox()
        self.filter_box.addItems(items)

        # Events
        self.btn_folder.clicked.connect(self.getWorkDirectory)
        self.file_list.currentRowChanged.connect(self.displayImage)

        self.btn_left.clicked.connect(lambda: self.editor.transformImage('Left'))
        self.btn_right.clicked.connect(lambda: self.editor.transformImage('Right'))
        self.mirror.clicked.connect(lambda: self.editor.transformImage('Mirror'))
        self.sharpness.clicked.connect(lambda: self.editor.transformImage('Sharpen'))
        self.gray.clicked.connect(lambda: self.editor.transformImage('B/W'))
        self.saturation.clicked.connect(lambda: self.editor.transformImage('Color'))
        self.contrast.clicked.connect(lambda: self.editor.transformImage('Contrast'))
        self.blur.clicked.connect(lambda: self.editor.transformImage('Blur'))

        self.filter_box.currentTextChanged.connect(self.editor.handle_filter)

        self.initUI()



    # Display the image selected from the List Widget
    def displayImage(self):
        if self.file_list.currentRow() >= 0:
            filename = self.file_list.currentItem().text()
            self.editor.load_image(filename)
            path = os.path.join(working_directory, filename)
            self.editor.show_image(path)


    # Setting global working directory
    def getWorkDirectory(self):
        global working_directory
        working_directory = QFileDialog.getExistingDirectory(caption="Choose a folder")

        # If user chooses to exit out of FileDialog
        if not working_directory:
            return

        extensions = [".png", ".jpg", ".svg", "jpeg"]
        filenames = self.filter(os.listdir(working_directory), extensions)
        self.file_list.clear()
        for filename in filenames:
            self.file_list.addItem(filename)

    @staticmethod
    def filter(files, extensions):
        results = []
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results


    def initUI(self):
        master_layout = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()


        col1.addWidget(self.btn_folder)
        col1.addWidget(self.file_list)
        col1.addWidget(self.filter_box)
        col1.addWidget(self.btn_left)
        col1.addWidget(self.btn_right)
        col1.addWidget(self.mirror)
        col1.addWidget(self.sharpness)
        col1.addWidget(self.gray)
        col1.addWidget(self.saturation)
        col1.addWidget(self.contrast)
        col1.addWidget(self.blur)

        col2.addWidget(self.picture_box)

        master_layout.addLayout(col1, 20) 
        master_layout.addLayout(col2, 80)

        self.setLayout(master_layout)


class Editor:
    def __init__(self, widget):
        # Stores reference to UI upon initialization
        self.widget = widget 
      
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_directory, self.filename)
        self.image = Image.open(fullname) 
        self.original = self.image.copy()


    # Saves the attribute "image" to directory
    def save_image(self):
        path = os.path.join(working_directory, self.save_folder)
        if not os.path.isdir(path):
            os.mkdir(path)

        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        self.widget.picture_box.hide()
        image = QPixmap(path)
        w, h = self.widget.picture_box.width(), self.widget.picture_box.height()
        image = image.scaled(w,h, Qt.KeepAspectRatio)
        self.widget.picture_box.setPixmap(image)
        self.widget.picture_box.show()


    def transformImage(self, transformation):
        transformations = {
            "B/W": lambda image: image.convert("L"),
            "Left": lambda image: image.transpose(Image.Transpose.ROTATE_90),
            "Right": lambda image: image.transpose(Image.Transpose.ROTATE_270),
            "Mirror": lambda image: image.transpose(Image.Transpose.FLIP_LEFT_RIGHT),
            "Blur": lambda image: image.filter(ImageFilter.BLUR),
            "Sharpen": lambda image: image.filter(ImageFilter.SHARPEN),
            "Color": lambda image: ImageEnhance.Color(image).enhance(1.2),
            "Contrast": lambda image: ImageEnhance.Contrast(image).enhance(1.2)
        }

        transform_function = transformations.get(transformation)
        if transform_function:
            self.image = transform_function(self.image)

        self.save_image()
        image_path = os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)


    def apply_filter(self, filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
            self.save_image()
            image_path = os.path.join(working_directory, self.save_folder, self.filename)
            self.show_image(image_path)
        else:
            filter_dict = {
                "B/W": lambda image: image.convert("L"),
                "Left": lambda image: image.transpose(Image.Transpose.ROTATE_90),
                "Right": lambda image: image.transpose(Image.Transpose.ROTATE_270),
                "Mirror": lambda image: image.transpose(Image.Transpose.FLIP_LEFT_RIGHT),
                "Blur": lambda image: image.filter(ImageFilter.BLUR),
                "Sharpen": lambda image: image.filter(ImageFilter.SHARPEN),
                "Color": lambda image: ImageEnhance.Color(image).enhance(1.2),
                "Contrast": lambda image: ImageEnhance.Contrast(image).enhance(1.2)
            }

            filter_func = filter_dict.get(filter_name)
            if filter_func:
                self.image = filter_func(self.image)

        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def handle_filter(self):
        if self.widget.file_list.currentRow() >= 0:
            select_filter = self.widget.filter_box.currentText()
            self.apply_filter(select_filter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec_())
