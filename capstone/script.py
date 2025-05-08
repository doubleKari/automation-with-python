#!/usr/bin/env python3


# This script opens an image file, 
# rotate it 90 degrees clockwise, resizes it
# and then save it with a .jpeg file extension


import os
from PIL import Image

for file in os.listdir("./images"):
    im = Image.open(f"./images/{file}")
    im = im.rotate(90).resize((128, 128))
    rgb_im = im.convert("RGB")  # Convert before saving
    rgb_im.save(f"{file}.jpeg")

