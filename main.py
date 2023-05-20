import cv2
import psutil
from utils import *
import time

MAIN_WALLPAPER_PATH = 'wallpaper/wp.jpg'
FINAL_WALLPAPER_PATH = 'wallpaper/toset.jpg'
#COLOR = (B,G,R)
GREEN = (0,255,0)
WHITE = (255,255,255)
day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
try:
    while True:
        battery = psutil.sensors_battery()
        t = time.localtime()
        text_to_pass = str(battery.percent)+'%'+'\n'+str(t.tm_hour)+':'+str(t.tm_min)+'\n'+str(day[t.tm_wday])+'\n'+str(t.tm_mday)+'/'+str(t.tm_mon)
        try:
            image = cv2.imread(MAIN_WALLPAPER_PATH)
        except:
            print('main image not found on specified path')
            break
        if battery.power_plugged:
            image = write_on_image(image,text_to_pass,1800,200,color=GREEN)
        else:
            image = write_on_image(image,text_to_pass,1800,200,color=WHITE)
        cv2.imwrite(FINAL_WALLPAPER_PATH,image)
        set_image_to_homescreen(FINAL_WALLPAPER_PATH)
        time.sleep(2)
except:
    set_image_to_homescreen(MAIN_WALLPAPER_PATH)
    print('loop_breaked')