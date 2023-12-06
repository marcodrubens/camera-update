import os
filename = input("What will you call this image? No .jpg extension")
os.system("libcamera-still -t 5000 -n -o ../images/output/"+filename+".jpg")

