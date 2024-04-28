from tkinter import *


class VaalOrbCalculator:
    def __init__(self, root, logger):

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

        self.init_ui()

    def init_ui(self):
        self.div_cost_label = Label(self.root, bg="darkgrey", text="Divine cost")
        self.div_cost_label.grid(column=1, row=0)

        self.div_cost_input = Entry(self.root, bg="darkgrey", width=10)
        self.div_cost_input.grid(column=2, row=0)

        self.col_title_1 = Label(self.root, bg="darkgrey", text="Gem name")
        self.col_title_1.grid(column=0, row=1)

        self.gem_cost_title = Label(self.root, bg="darkgrey", text="Gem cost")
        self.gem_cost_title.grid(column=1, row=1)

        self.lvl_up_title = Label(self.root, bg="darkgrey", fg="green", text="+1 val")
        self.lvl_up_title.grid(column=2, row=1)

        self.lvl_down_title = Label(self.root, bg="darkgrey", fg="red", text="-1 val")
        self.lvl_down_title.grid(column=3, row=1)

        self.qual_up_title = Label(self.root, bg="darkgrey", fg="green", text="+qual val")
        self.qual_up_title.grid(column=4, row=1)

        self.qual_down_title = Label(self.root, bg="darkgrey", fg="red", text="-qual val")
        self.qual_down_title.grid(column=5, row=1)

        self.no_change_title = Label(self.root, bg="darkgrey", text="no change val")
        self.no_change_title.grid(column=6, row=1)

        self.result_title = Label(self.root, bg="darkgrey", text="Avg return (c)")
        self.result_title.grid(column=7, row=1)

        self.gem_name_input = Entry(self.root, bg="lightgray", width=self.fixed_width)
        self.gem_name_input.grid(column=0, row=2, pady=self.y_padding, padx=self.x_padding)

        self.gem_cost_input = Entry(self.root, bg="lightgray", width=self.fixed_width)
        self.gem_cost_input.grid(column=1, row=2, pady=self.y_padding, padx=self.x_padding)

        self.lvl_up_input = Entry(self.root, bg="lightgray", width=self.fixed_width)
        self.lvl_up_input.grid(column=2, row=2, pady=self.y_padding, padx=self.x_padding)

        self.lvl_down_input = Entry(self.root, bg="lightgray", width=self.fixed_width)
        self.lvl_down_input.grid(column=3, row=2, pady=self.y_padding, padx=self.x_padding)

        self.qual_up_input = Entry(self.root, bg="lightgray", width=self.fixed_width)
        self.qual_up_input.grid(column=4, row=2, pady=self.y_padding, padx=self.x_padding)

        self.qual_down_input = Entry(self.root, bg="lightgray", width=self.fixed_width)
        self.qual_down_input.grid(column=5, row=2, pady=self.y_padding, padx=self.x_padding)

        self.no_change_input = Entry(self.root, bg="lightgray", width=self.fixed_width)
        self.no_change_input.grid(column=6, row=2, pady=self.y_padding, padx=self.x_padding)

        self.result = Label(self.root, text="", bg="lightgray", width=self.fixed_width)
        self.result.grid(column=7, row=2, pady=self.y_padding, padx=self.x_padding)

        self.btn = Button(self.root, text="Calculate", fg="black", command=self.calculateVaalOrb)
        self.btn.grid(column=8, row=2, padx=self.x_padding, pady=self.y_padding)

    def calculateVaalOrb(self):
        res = -int(self.gem_cost_input.get())
        res += int(self.lvl_up_input.get()) * self.vaal_orb_table["lvl_up"]
        res += int(self.lvl_down_input.get()) * self.vaal_orb_table["lvl_down"]
        res += int(self.qual_up_input.get()) * self.vaal_orb_table["qual_up"]
        res += int(self.qual_down_input.get()) * self.vaal_orb_table["qual_down"]
        res += int(self.no_change_input.get()) * self.vaal_orb_table["no_change"]
        res = res * int(self.div_cost_input.get())
        self.result.config(text=res)

        # format: gem_name, gem cost, lvl_up, lvl_down, qual_up, qual_down, no_change, result
        log_string = self.gem_name_input.get() + "," + self.gem_cost_input.get() + ", " + self.lvl_up_input.get() + ", " + self.lvl_down_input.get() + ", " + self.qual_up_input.get() + ", " + self.qual_down_input.get() + ", " + self.no_change_input.get() + ", " + str(
            res) + "\n"

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