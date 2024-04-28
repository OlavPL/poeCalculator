from tkinter import *
from PIL import Image, ImageTk

from Logger import Logger
from VaalOrbCalculator import VaalOrbCalculator


root = Tk()
root.title("Calculator")
root.geometry("1400x600")
root.config(bg="darkgrey")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(10, weight=5)


log_lines = (10, 10)
log_labels = []

# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label="New")
# item.config(bg="lightgrey")
# menu.add_cascade(label="File", menu=item)
# root.config(menu=menu)

# Load the image file
bg_image = Image.open("res/atziri_wallpaper_wide.png")
# Resize the image to fit the window
bg_image = bg_image.resize((3000, 600))
# Convert the image to a format Tkinter can use
bg_photo = ImageTk.PhotoImage(bg_image)
# bg_photo = PhotoImage("res/atziri_wallpaper_crop.png", width=1100, height=600)

# Create a label with the image and place it at the bottom of the window
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

logger = Logger(root)

vaalOrbCalc = VaalOrbCalculator(root, logger)
logger.readLog()

root.mainloop()
