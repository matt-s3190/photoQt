# Project Title: PhotoQT
A simple photo-editing GUI (Graphical User Interface) made in Python using PyQt5 and PIL (Python Imaging Library). 

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
This project marked my first experience working with an image processing library Pillow (PIL) and with that brought new challenges. One of them being classifying which classes and functions were necessary for the scope of this application. To address this, I spent significant time exploring Pillow’s official documentation and breaking down its functionality to build a solid foundational understanding of the library.

Another challenge arose when applying certain transformations, particularly image rotation, to high-resolution images (≥1280×720). In these cases, there is a noticeable ramp-up delay when these edits get previewed in real time. This highlighted performance considerations when working with real-time image manipulation on larger image sizes.


# What I've learned
- Understanding how to incorporate composition of classes into my project. It helped separate the logic of the UI and photo-editing features, maintaining readability
- This project also helped me fill in gaps of knowledge I had about OOP (Object-Oriented-Programming) as I got more practice. 
- Reading the official documentation of a library helped me visualize its structure and debug certain parts of my program.

# Screenshots

## Startup Menu 

<img src="/images/startup-screenshot.png" alt="Startup Screen" width="400">\
## Before editing 

<img src="/images/before-edited-screenshot.png" alt="Before editing" width="400">\
## After Editing 

<img src="/images/edited-screenshot.png" alt="After editing" width="400">\

# How to Install and Run the Project

Follow these steps to get the PhotoQT application up and running:

## 1. Clone the repository
First, download or clone the repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
## 2. Optional: Set up virtual environment
It's best to set up use a venv to avoid conflicts with other Python packages:
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

## 3. Install dependencies
Install packages from `requirements.txt`
```bash
pip install -r requirements.txt
```

## 4. Run appplication:
Execute the main Python file to launch the GUI:
```bash
python main.py
```

# References
Check out 



