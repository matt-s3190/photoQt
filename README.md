# Project Title: PhotoQT
A simple photo-editing GUI (Guided User Interface) made in Python using PyQt5 and PIL (Python Imaging Library). 

# Project Overview
This application allows users to import images with these extensions (.jpg, .jpeg, .png, and .svg) and customize them through event-driven controls such as buttons and drop-down menus. These transformations include mirroring, rotating, blurring, and manipulation of the image's contrast, saturation, tone and texture. These changes are all fully adjustable by the user. When a change gets applied to the image, the edited image is updated in real time for immediate preview. \
If the image isn't up to the user's standards, there is an undo feature that reverses the modifications.

## Dependencies

This project requires the following Python libraries:

- Python 3.9 or newer
- PyQt5
- Pillow (PIL)

All required dependencies are listed in the `requirements.txt` file.


# Challenges I've faced
This was my first time experiementing with an image processing library (PIL) and it was a strenous process to decide what classes and functions are needed for my certain build. I got to explore Pillow's offical documentation, break apart and piece together a foundational knowledge about  the library all together.
When testing out certain transformations, specifically the "rotate" features, on images that have a high resoultion size (>=1280×720), there is a ramp-up delay in previewing the images.


# What I've learned
Things that I learned:
Composition of Classes (Editor Instance within Widget Class)
os Methods
Incorporation of the PIL Library
Using Lambda functions as values in key

Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

How to Install and Run the Project
- downalod `requirement.txt

References



