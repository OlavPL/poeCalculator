import datetime
from tkinter import *


class AwakenedLevelingCalculator:
    log_path = "Awakened_leveling_log.txt"
    background_image_path = "res/AwaLevelBackground_test.png"

    def __init__(self, root, logger):

        self.font = ("Comic Sans MS", 11, "bold")

        self.root = root
        self.fixed_width = 12
        self.y_padding = 2
        self.x_padding = 4

        self.awakened_grid = None
        self.div_cost_label = None
        self.div_cost_input = None
        self.gem_name_label = None
        self.gem_name_input = None
        self.gem_cost_label = None
        self.gem_cost_input = None
        self.beast_cost_label = None
        self.beast_cost_input = None
        self.qual_cost_label = None
        self.qual_cost_input = None
        self.maxlvl_value_label = None
        self.maxlvl_value_input = None
        self.result_label = None
        self.result = None
        self.btn = None
        self.logger = logger
        self.logger.current_log = "awakened_level"

        self.button_images = []
        self.isHoveringButton = False
        self.topPadding = (20, 5)
        self.empty_cells = 2
        self.filler_cells = []

        self.init_ui()

    def init_ui(self):
        photo = PhotoImage(file="res/buttonStock1.png")
        self.button_images.append(photo.subsample(2, 2))
        photo = PhotoImage(file="res/buttonStock1d.png")
        self.button_images.append(photo.subsample(2, 2))
        photo = PhotoImage(file="res/buttonStock1h.png")
        self.button_images.append(photo.subsample(2, 2))

        self.awakened_grid = Label(self.root, bg="black", fg="gold", font=self.font, text="Awakened Gem lvl", width=self.fixed_width+4)
        self.awakened_grid.grid(column=1, row=0, pady=self.topPadding, padx=self.x_padding)
        self.awakened_grid.config()

        self.div_cost_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Divine cost")
        self.div_cost_label.grid(column=2, row=0, pady=self.topPadding)

        self.div_cost_input = Entry(self.root, bg="black", fg="gold", font=self.font, width=10)
        self.div_cost_input.insert(0, "100")
        self.div_cost_input.grid(column=3, row=0, pady=self.topPadding)

        self.gem_name_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Gem name")
        self.gem_name_label.grid(column=1, row=1)

        self.gem_cost_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Gem cost")
        self.gem_cost_label.grid(column=2, row=1)

        self.beast_cost_label = Label(self.root, bg="black", fg="gold",font=self.font, text="Beast cost")
        self.beast_cost_label.grid(column=3, row=1)

        self.qual_cost_label = Label(self.root, bg="black", fg="gold",font=self.font, text="Qual cost")
        self.qual_cost_label.grid(column=4, row=1)

        self.maxlvl_value_label = Label(self.root, bg="black", fg="gold", font=self.font,text="lvl 5 cost")
        self.maxlvl_value_label.grid(column=5, row=1)

        self.result_label = Label(self.root, bg="black", fg="gold", font=self.font, text="Avg return (c)")
        self.result_label.grid(column=8, row=1)

        self.gem_name_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.gem_name_input.grid(column=1, row=2, pady=self.y_padding, padx=self.x_padding)

        self.gem_cost_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font,
                                    width=self.fixed_width)
        self.gem_cost_input.grid(column=2, row=2, pady=self.y_padding, padx=self.x_padding)

        self.beast_cost_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.beast_cost_input.grid(column=3, row=2, pady=self.y_padding, padx=self.x_padding)

        self.qual_cost_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.qual_cost_input.grid(column=4, row=2, pady=self.y_padding, padx=self.x_padding)

        self.maxlvl_value_input = Entry(self.root, bg="black", fg="gold", insertbackground="gold", font=self.font, width=self.fixed_width)
        self.maxlvl_value_input.grid(column=5, row=2, pady=self.y_padding, padx=self.x_padding)

        # filler columns to keep result and button in same position acoss views.
        for i in range(self.empty_cells):
            self.filler_cells.append(Label(self.root, width=self.fixed_width, bg="black", fg="gold", font=self.font, text=""))
            self.filler_cells[-1].grid(column=6+i, row=2, pady=self.y_padding, padx=self.x_padding)

        self.result = Label(self.root, text="", bg="black", fg="gold", font=self.font, width=self.fixed_width)
        self.result.grid(column=8, row=2, pady=self.y_padding, padx=self.x_padding)

        self.btn = Button(self.root, bg="black", fg="gold", font=self.font, command=self.calculate,
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

    def calculate(self):
        try:
            res = -float(self.gem_cost_input.get())
            res -= float(self.beast_cost_input.get())*4
            res -= float(self.qual_cost_input.get())
            res += float(self.maxlvl_value_input.get())
            res = int(res * float(self.div_cost_input.get()))
            self.result.config(text=res)
        except:
            self.result.config(text="Invalid input.")
            return

        log_string = self.gem_name_input.get() + "," + self.gem_cost_input.get() + "," + self.beast_cost_input.get() + "," + self.qual_cost_input.get() + "," + self.maxlvl_value_input.get() + ", , ," + str(int(res)) + "," + str(datetime.datetime.now()) + "\n"
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
        self.awakened_grid.grid_forget()
        self.div_cost_label.grid_forget()
        self.div_cost_input.grid_forget()
        self.gem_name_label.grid_forget()
        self.gem_name_input.grid_forget()
        self.gem_cost_label.grid_forget()
        self.gem_cost_input.grid_forget()
        self.beast_cost_label.grid_forget()
        self.beast_cost_input.grid_forget()
        self.qual_cost_label.grid_forget()
        self.qual_cost_input.grid_forget()
        self.maxlvl_value_label.grid_forget()
        self.maxlvl_value_input.grid_forget()
        self.result_label.grid_forget()
        self.result.grid_forget()
        self.btn.grid_forget()
        self.btn.unbind('<ButtonPress-1>')
        self.btn.unbind('<ButtonRelease-1>')
        self.btn.unbind('<Enter>')
        self.btn.unbind('<Leave>')