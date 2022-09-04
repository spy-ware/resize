import glob
import os
from PIL import Image

# file type to search for (example: png)
filetype = "JPG"

# desired width - height
size = [1920, 1080]

# get folder that the script is running in (current working directory, CWD)
cwd = os.path.dirname(os.path.realpath(__file__))

# get all images in current folder with the desired file type
images = glob.glob(f"{cwd}/*.{filetype}")

# check if output folder doesn't already exist
if not os.path.isdir(f"{cwd}/output"):

    # create output folder
    os.mkdir(f"{cwd}/output")

# go through every image that was found
for img in images:

    # open image
    temp_img = Image.open(img)

    # resize image (size[0] -> width, size[1] -> height)
    out = temp_img.resize((size[0], size[1]))

    # splits the full path based on backslashes to the image and gets the last item, getting the image name
    # example:
    #          c:\users\me\images\picture1.png
    #          c: users me images picture1.png
    #          picture1.png
    file_name = img.split("\\")
    file_name = file_name[-1]

    # save image to output folder
    out.save(f"{cwd}/output/{file_name}")
