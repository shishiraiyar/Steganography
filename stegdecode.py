from PIL import Image
import numpy as np

image = np.asarray(Image.open("output.png"))

msg = ""
temp = ""

msgChars = 0

for pixel in image[0][0:16]: 
    s = f"{pixel[0]:08b}"
    t = s[-2:]
    temp += t
    if len(temp) == 32:
        msgChars = int(temp, 2)
        print("Length: ",msgChars)
        temp = ""

pixelCount = 0
for i in range(0, len(image)):
    for j in range(0, len(image[i])):
        if (i==0 and j<16):         #16 coz first 4 bytes are msg length
            continue
        pixel = image[i][j]         
        s = f"{pixel[0]:08b}"
        t = s[-2:]
        temp += t
        pixelCount +=1
        
        if len(temp) == 8:
            msg += chr(int(temp, 2))
            temp = ""

        if pixelCount == msgChars*4:
            break
    if pixelCount == msgChars*4:
        break


print(msg)