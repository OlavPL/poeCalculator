from tkinter import Label

class Logger:
    def __init__(self, root):
        self.root = root
        self.log_labels = []

        self.log_name = Label(self.root, text="Gem name", bg="darkgrey")
        self.log_name.grid(column=0, row=5)

        self.log_cost = Label(self.root, text="Gem cost", bg="darkgrey")
        self.log_cost.grid(column=1, row=5)

        self.log_lvl_up = Label(self.root, text="lvl up", bg="darkgrey")
        self.log_lvl_up.grid(column=2, row=5)

        self.log_lvl_down = Label(self.root, text="lvl down", bg="darkgrey")
        self.log_lvl_down.grid(column=3, row=5)

        self.log_qual_up = Label(self.root, text="qual up", bg="darkgrey")
        self.log_qual_up.grid(column=4, row=5)

        self.log_qual_down = Label(self.root, text="qual down", bg="darkgrey")
        self.log_qual_down.grid(column=5, row=5)

        self.log_no_change = Label(self.root, text="no change", bg="darkgrey")
        self.log_no_change.grid(column=6, row=5)

        self.log_result = Label(self.root, text="avg return (c)", bg="darkgrey")
        self.log_result.grid(column=7, row=5)

    def readLog(self, file_name="vaal_orb_results.txt"):
        try:
            f = open(file_name, "r")
            lines = f.readlines()
            f.close()

            for label in self.log_labels:
                label.grid_forget()
            self.log_labels.clear()

            for i in range(0, len(lines)):
                line = lines[i].split(",")
                for j in range(len(line)):
                    label = Label(self.root, text=line[j], bg="lightgrey")
                    self.log_labels.append(label)
                    label.grid(column=j, row=i + 6)
        except:
            return