import cv2
import ctypes
import os

def show(image):
    cv2.imshow('image',image)
    cv2.waitKey(0)

def write_on_image(image,text,x,y,color=(255,255,255),fontscale=2,thickness=2,line_params=(50,30)):
    d0,dy = line_params[0],line_params[1] #50,30
    for i, line in enumerate(text.split('\n')):
        y = d0+i*dy
        image = cv2.putText(image,text=line,org=(x,y),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=fontscale,color=color,thickness=thickness,lineType=cv2.LINE_8)
    return image


def set_image_to_homescreen(image_relative_path):
    path = os.path.abspath(image_relative_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0,str(path), 0)
