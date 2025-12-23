#Final_Project
#GIF

import imageio.v3 as iio

filenames = ['lego-flower1.png', 'lego-flower2.png', 'lego-flower3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('legoflower.gif', images, duration = 500, loop = 0)

