import datetime
from tkinter import *

class VaalOrbCalculator:
    def __init__(self, root, logger):

        self.font = ("Comic Sans MS", 11, "bold")

        self.root = root
        self.fixed_width = 12
        self.y_padding = 2
        self.x_padding = 4
        self.vaal_orb_table = {
            "lvl_up": 0.125,
            "lvl_down": 0.125,
            "qual_up": 0.125,
            "qual_down": 0.125,
            "no_change": 0.5
        }
        self.log_path = "vaal_orb_results.txt"

        self.vaal_orb_grid = None
        self.div_cost_label = None
        self.div_cost_input = None
        self.gem_name_input = None
        self.gem_cost_input = None
        self.lvl_up_input = None
        self.lvl_down_input = None
        self.qual_up_input = None
        self.qual_down_input = None
        self.no_change_input = None
        self.result = None
        self.btn = None
        self.logger = logger

        self.button_images = []
        self.isHoveringButton = False
        self.topPadding = (20, 5)

        self.init_ui()

    def init_ui(self):
        photo = PhotoImage(file="res/buttonStock1.png")
        self.button_images.append(photo.subsample(2, 2))
        photo = PhotoImage(file="res/buttonStock1d.png")
        self.button_images.append(photo.subsample(2, 2))
        photo = PhotoImage(file="res/buttonStock1h.png")
        self.button_images.append(photo.subsample(2, 2))

        self.vaal_orb_grid = Label(self.root, bg="black", fg="gold", font=self.font, text="Vaal Orb calculator")
        self.vaal_orb_grid.grid(column=1, row=0, pady=self.topPadding, padx=self.x_padding)
        self.vaal_orb_grid.config()

        self.div_cost_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Divine cost")
        self.div_cost_label.grid(column=2, row=0, pady=self.topPadding)

        self.div_cost_input = Entry(self.root, bg="black", fg="gold", font=self.font, width=10)
        self.div_cost_input.insert(0, "100")
        self.div_cost_input.grid(column=3, row=0, pady=self.topPadding)

        gem_name_title = Label(self.root, bg="black", fg="gold", font=self.font, text="Gem name")
        gem_name_title.grid(column=1, row=1)

        gem_cost_title = Label(self.root, bg="black", fg="gold", font=self.font, text="Gem cost")
        gem_cost_title.grid(column=2, row=1)

        lvl_up_title = Label(self.root, bg="black",font=self.font, fg="green", text="+1 val")
        lvl_up_title.grid(column=3, row=1)

        vl_down_title = Label(self.root, bg="black",font=self.font, fg="red", text="-1 val")
        vl_down_title.grid(column=4, row=1)

        qual_up_title = Label(self.root, bg="black",font=self.font, fg="green", text="+qual val")
        qual_up_title.grid(column=5, row=1)

        qual_down_title = Label(self.root, bg="black",font=self.font, fg="red", text="-qual val")
        qual_down_title.grid(column=6, row=1)

        no_change_title = Label(self.root, bg="black", fg="gold", font=self.font, text="no change val")
        no_change_title.grid(column=7, row=1)

        esult_title = Label(self.root, bg="black", fg="gold", font=self.font, text="Avg return (c)")
        esult_title.grid(column=8, row=1)

        self.gem_name_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.gem_name_input.grid(column=1, row=2, pady=self.y_padding, padx=self.x_padding)

        self.gem_cost_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.gem_cost_input.grid(column=2, row=2, pady=self.y_padding, padx=self.x_padding)

        self.lvl_up_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.lvl_up_input.grid(column=3, row=2, pady=self.y_padding, padx=self.x_padding)

        self.lvl_down_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.lvl_down_input.grid(column=4, row=2, pady=self.y_padding, padx=self.x_padding)

        self.qual_up_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.qual_up_input.grid(column=5, row=2, pady=self.y_padding, padx=self.x_padding)

        self.qual_down_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.qual_down_input.grid(column=6, row=2, pady=self.y_padding, padx=self.x_padding)

        self.no_change_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.no_change_input.grid(column=7, row=2, pady=self.y_padding, padx=self.x_padding)

        self.result = Label(self.root, text="", bg="black", fg="gold", font=self.font, width=self.fixed_width)
        self.result.grid(column=8, row=2, pady=self.y_padding, padx=self.x_padding)

        self.btn = Button(self.root, bg="black", fg="gold", font=self.font, command=self.calculateVaalOrb,
                          image=self.button_images[0], compound='center', relief=FLAT, text="Calculate",
                          activebackground="black", activeforeground="gold", highlightbackground="black",
                          highlightcolor="yellow", bd=0, pady=10)
        self.btn.grid(column=8, row=0, padx=self.x_padding, pady=self.y_padding)
        self.btn.bind('<ButtonPress-1>', self.change_image_down)
        self.btn.bind('<ButtonRelease-1>', self.change_image_up)
        self.btn.bind('<Enter>', self.change_image_hover)
        self.btn.bind('<Leave>', self.change_image_leave)

    def change_image_down(self, event):
        # Change the image of the button to the second image in the list when the button is pressed
        self.btn.config(image=self.button_images[1])

    def change_image_up(self, event):
        # Change the image of the button back to the first image in the list when the button is released
        if self.isHoveringButton:
            self.btn.config(image=self.button_images[2])
        else:
            self.btn.config(image=self.button_images[0])

    def change_image_hover(self, event):
        # Change the image of the button to the third image in the list when the mouse pointer enters the button area
        self.btn.config(image=self.button_images[2])
        self.isHoveringButton = True

    def change_image_leave(self, event):
        # Change the image of the button back to the first image in the list when the mouse pointer leaves the button area
        self.btn.config(image=self.button_images[0])
        self.isHoveringButton = False

    def calculateVaalOrb(self):
        try:
            res = -int(self.gem_cost_input.get())
            res += int(self.lvl_up_input.get()) * self.vaal_orb_table["lvl_up"]
            res += int(self.lvl_down_input.get()) * self.vaal_orb_table["lvl_down"]
            res += int(self.qual_up_input.get()) * self.vaal_orb_table["qual_up"]
            res += int(self.qual_down_input.get()) * self.vaal_orb_table["qual_down"]
            res += int(self.no_change_input.get()) * self.vaal_orb_table["no_change"]
            res = res * int(self.div_cost_input.get())
            self.result.config(text=res)
        except:
            self.result.config(text="Invalid input.")
            return

        # format: gem_name, gem cost, lvl_up, lvl_down, qual_up, qual_down, no_change, result, timestamp
        log_string = self.gem_name_input.get() + "," + self.gem_cost_input.get() + "," + self.lvl_up_input.get() + "," + self.lvl_down_input.get() + "," + self.qual_up_input.get() + "," + self.qual_down_input.get() + "," + self.no_change_input.get() + "," + str(
            res) + "," + str(datetime.datetime.now()) + "\n"

        # add result to file, or replace line if gem_name_input exists.
        try:
            f = open("vaal_orb_results.txt", "r")
            lines = f.readlines()
            f.close()
            f = open("vaal_orb_results.txt", "w")
            found = False
            for i in range(0, len(lines)):
                line = lines[i].split(",")
                if line[0] == self.gem_name_input.get():
                    lines[i] = log_string
                    found = True
            if not found:
                lines.append(log_string)
            for line in lines:
                f.write(line)
            f.close()
        except:
            f = open("vaal_orb_results.txt", "w")
            f.write(log_string)
            f.close()
        self.logger.readLog(self.log_path)
