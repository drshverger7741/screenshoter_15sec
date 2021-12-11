# screenshot
from PIL import ImageGrab
import datetime
import time
import os

my_project_path = 'C:\\basket'
if not os.path.isdir(my_project_path):
    os.mkdir(my_project_path)

while 1:
    img = ImageGrab.grab()
    my_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = my_project_path + "\\screenshot_" + my_time + ".jpg"
    img.save(file_name, "JPEG")
    time.sleep(1)

    print(file_name)
    time.sleep(14)
