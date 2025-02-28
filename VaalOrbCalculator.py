import datetime
from tkinter import *

class VaalOrbCalculator:
    log_path = "vaal_orb_log.txt"
    background_image_path = "res/atziri_wallpaper_wide.png"
    vaal_orb_table = {
        "lvl_up": 0.125,
        "lvl_down": 0.125,
        "qual_up": 0.125,
        "qual_down": 0.125,
        "no_change": 0.5
    }

    def __init__(self, root, logger, font=("Comic Sans MS", 11, "bold")):

        self.font = font
        self.root = root
        self.fixed_width = 12
        self.y_padding = 2
        self.x_padding = 4

        self.vaal_orb_grid = None
        self.div_cost_label = None
        self.div_cost_input = None
        self.gem_name_label = None
        self.gem_name_input = None
        self.gem_cost_label = None
        self.gem_cost_input = None
        self.lvl_up_label = None
        self.lvl_up_input = None
        self.lvl_down_label = None
        self.lvl_down_input = None
        self.qual_up_label = None
        self.qual_up_input = None
        self.qual_down_label = None
        self.qual_down_input = None
        self.no_change_label = None
        self.no_change_input = None
        self.result = None
        self.btn = None
        self.logger = logger
        self.logger.current_log = "vaal_orb"

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

        self.vaal_orb_grid = Label(self.root, bg="black", fg="gold", font=self.font, text="Vaal Orb calculator", width=self.fixed_width+4)
        self.vaal_orb_grid.grid(column=1, row=0, pady=self.topPadding, padx=self.x_padding)
        self.vaal_orb_grid.config()

        self.div_cost_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Divine cost")
        self.div_cost_label.grid(column=2, row=0, pady=self.topPadding)

        self.div_cost_input = Entry(self.root, bg="black", fg="gold", font=self.font, width=10)
        self.div_cost_input.insert(0, "100")
        self.div_cost_input.grid(column=3, row=0, pady=self.topPadding)

        self.gem_name_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Gem name")
        self.gem_name_label.grid(column=1, row=1)

        self.gem_cost_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Gem cost")
        self.gem_cost_label.grid(column=2, row=1)

        self.lvl_up_label = Label(self.root, bg="black",font=self.font, fg="green", text="+1 val")
        self.lvl_up_label.grid(column=3, row=1)

        self.lvl_down_label = Label(self.root, bg="black",font=self.font, fg="red", text="-1 val")
        self.lvl_down_label.grid(column=4, row=1)

        self.qual_up_label = Label(self.root, bg="black",font=self.font, fg="green", text="+qual val")
        self.qual_up_label.grid(column=5, row=1)

        self.qual_down_label = Label(self.root, bg="black",font=self.font, fg="red", text="-qual val")
        self.qual_down_label.grid(column=6, row=1)

        self.no_change_label = Label(self.root, bg="black", fg="gold", font=self.font, text="no change val")
        self.no_change_label.grid(column=7, row=1)

        self.result_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Avg return (c)")
        self.result_label.grid(column=8, row=1)

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

        self.logger.readLog(self.log_path)

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
            res = -float(self.gem_cost_input.get())
            res += float(self.lvl_up_input.get()) * self.vaal_orb_table["lvl_up"]
            res += float(self.lvl_down_input.get()) * self.vaal_orb_table["lvl_down"]
            res += float(self.qual_up_input.get()) * self.vaal_orb_table["qual_up"]
            res += float(self.qual_down_input.get()) * self.vaal_orb_table["qual_down"]
            res += float(self.no_change_input.get()) * self.vaal_orb_table["no_change"]
            res = int(res * float(self.div_cost_input.get()))

            self.result.config(text=res)
        except:
            self.result.config(text="Invalid input.")
            return

        # format: gem_name, gem cost, lvl_up, lvl_down, qual_up, qual_down, no_change, result, timestamp
        log_string = self.gem_name_input.get() + "," + self.gem_cost_input.get() + "," + self.lvl_up_input.get() + "," + self.lvl_down_input.get() + "," + self.qual_up_input.get() + "," + self.qual_down_input.get() + "," + self.no_change_input.get() + "," + str(
            res) + "," + str(datetime.datetime.now()) + "\n"

        # add result to file, or replace line if gem_name_input exists.
        try:
            f = open(self.log_path, "r")
            lines = f.readlines()
            f.close()
            f = open(self.log_path, "w")
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
            f = open(self.log_path, "w")
            f.write(log_string)
            f.close()
        self.logger.readLog(self.log_path)

    def forget(self):
        self.vaal_orb_grid.grid_forget()
        self.div_cost_label.grid_forget()
        self.div_cost_input.grid_forget()
        self.gem_name_label.grid_forget()
        self.gem_name_input.grid_forget()
        self.gem_cost_label.grid_forget()
        self.gem_cost_input.grid_forget()
        self.lvl_up_label.grid_forget()
        self.lvl_up_input.grid_forget()
        self.lvl_down_label.grid_forget()
        self.lvl_down_input.grid_forget()
        self.qual_up_label.grid_forget()
        self.qual_up_input.grid_forget()
        self.qual_down_label.grid_forget()
        self.qual_down_input.grid_forget()
        self.no_change_label.grid_forget()
        self.no_change_input.grid_forget()
        self.result_label.grid_forget()
        self.result.grid_forget()
        self.btn.grid_forget()
        self.btn.unbind('<ButtonPress-1>')
        self.btn.unbind('<ButtonRelease-1>')
        self.btn.unbind('<Enter>')
        self.btn.unbind('<Leave>')
