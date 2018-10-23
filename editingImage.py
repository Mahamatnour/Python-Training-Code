# this code for editing an images

import Pillow 
image = Image.open("cat.jpg") # open the image with the given name
size = image.size # set size to the image
newImage = image


for x in range(0, size[0]): # for each number in the range of width

    for y in range(0, size[1]): # for each number in the range of height

        color = image.getpixel((x,y)) # get the color at the given pixel
        newColor = (255 - color[0], 255 - color[1], 255 - color[3]) #create a new colors

        position = (x, y)

        newImage.putpixel(position, newColor) # put the pixel at the position, to the invested new colors

        newImage.show() # show the image

        newImage.save("new.jpg")




