from tkinter import *

from Logger import Logger
from VaalOrbCalculator import VaalOrbCalculator





root = Tk()
root.title("Calculator")
root.geometry("800x600")
root.config(bg="darkgrey")


log_lines = (10, 10)
log_labels = []

menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
item.config(bg="lightgrey")
menu.add_cascade(label="File", menu=item)
root.config(menu=menu)

vaal_orb_grid = Label(root, bg="darkgrey", text="Vaal Orb calculator")
vaal_orb_grid.grid()
vaal_orb_grid.config()

logger = Logger(root)

vaalOrbCalc = VaalOrbCalculator(root, logger)
logger.readLog()

root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
