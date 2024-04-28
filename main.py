from tkinter import *

from Logger import Logger
from VaalOrbCalculator import VaalOrbCalculator


root = Tk()
root.title("Calculator")
root.geometry("1100x600")
root.config(bg="darkgrey")


log_lines = (10, 10)
log_labels = []

menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
item.config(bg="lightgrey")
menu.add_cascade(label="File", menu=item)
root.config(menu=menu)

logger = Logger(root)

vaalOrbCalc = VaalOrbCalculator(root, logger)
logger.readLog()

root.mainloop()
