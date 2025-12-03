from src.ica.helpers.dummyWindow import *

file_path = pickAFile()
image = Picture(file_path)
image.show()

pic1 = Picture("../SampleImages/butterfly.jpg")
pic1.show()

pic2 = Picture("../SampleImages/mightyMidway.jpg")
pic2.show()

pic3 = Picture("../SampleImages/bryceCanyon.jpg")
pic3.show()

def draw_something():
    ...


def main():
    drawing = draw_something()
    drawing.show()

    keep_windows_open()


if __name__ == "__main__":
    main()
