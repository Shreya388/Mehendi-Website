from PIL import Image
import os

# Set the desired width and height
width = 936
height = 922

# Loop through all files in the current directory
for filename in os.listdir('.'):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.webp'):
        # Open the image using Pillow
        with Image.open(filename) as img:
            # Resize the image
            img = img.resize((width, height))
            # Save the resized image with a new filename
            img.save('./Resized/' + filename)
