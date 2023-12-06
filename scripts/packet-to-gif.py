#takes a packet (defined as a directory containing the four quadrants of a split image)
#iterates through the contents of said package, and turns the selected images into a gif
#which is output in the .gif dir
from PIL import Image
import os
packet_name = input("file name no jpg ") 

def packet_to_gif(packet_name):
    #returns a gif file that is saved in images/gif/
    # first loop initializing packet array for specific file, second descending to add bouncing loop effect
    # this will be customized later for expansion on gif types & prioritized frames (keyframes)
    packet = []
    packet_list = os.listdir("../images/packets/"+packet_name)
    for i in range(0,len(packet_list)):
        
        packet.append(Image.open(("../images/packets/"+packet_name+"/"+packet_list[i])));
        #print(packet[i])
        print("i:"+str(i))
    
    for j in range(3,-1,-1):
        packet.append(Image.open(("../images/packets/"+packet_name+"/"+packet_list[j])))
        print("j:"+str(j))

    packet[0].save("../images/gif/"+packet_name+".gif", save_all = True, append_images = packet[1:],duration = 300, loop = True)    
packet_to_gif(packet_name)
