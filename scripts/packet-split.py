##takes a file as a parameter(output from driver call) and uses split-image() into four
import split_image as split
import os
from PIL import Image

packet_name = "photo"
file = packet_name+".jpg"
def quad_split(file,packet_name):
   # os.mkdir("/images/packets/"+packet_name)
    split.split_image(file, 2, 2, False,False,False,packet_name)
    print("Done. Packet found at "+ packet_name)

def center(file,packet_name):
    photo1 = Image.open(r"photo/photo_0.jpg")
    photo2 = Image.open(r"photo/photo_1.jpg")
    photo3 = Image.open(r"photo/photo_2.jpg")
    photo4 = Image.open(r"photo/photo_3.jpg")

    width, height = photo1.size

    photo1.crop((0,0,width,height))
    print("img 1 cropped")
    photo2.crop((0,70,width-24,height))
    print("img 2 cropped")
    photo3.crop((0,35,width-135,height))
    print("img 3 cropped")
    photo4.crop((0,100,width-105,height))
    print("img 4 cropped")

quad_split(file,packet_name)
center(file,packet_name)
