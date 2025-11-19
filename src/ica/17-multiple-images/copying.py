from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def copy_pic_into(small_pic, large_pic, start_x, start_y):
    new_pic = small_pic.copy()


green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_into(green_turtle, scene, 25, 25)
copy_pic_into(green_turtle, scene, 200, 200)
copy_pic_into(green_turtle, scene, 400, 200)
scene.show()

keep_windows_open()