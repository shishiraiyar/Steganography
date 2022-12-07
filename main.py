from PIL import Image #pillow
import numpy as np

def msgconv(msg):
    pairs = []
    for i in msg:
        s = f"{ord(i):08b}"
        pairs += [s[j:j+2] for j in range(0,8,2)]
    return pairs


with open("beescript.txt") as file:
    msg = file.read()

# msg = "hiii"

inputImg = "flower.png"
outputImg = "output.png"

pairs = []

msglen = f"{len(msg):032b}"
pairs += [msglen[j:j+2] for j in range(0,32,2)]

print("Length: ", len(msg))

pairs += msgconv(msg)
n = len(pairs)

image = np.asarray(Image.open(inputImg))
# print(image.flags)
image = image.copy()         #to make the image writable
print(np.shape(image))
i = 0
for row in image:
    for pixel in row:
        s = f"{pixel[0]:08b}"
        # print(s)

        t = s[0:-2] + pairs[i] 

        pixel[0] = int(t, 2)

        i += 1

        if i == n:
            break
    if i == n:
        break


Image.fromarray(image).save("output.png")






