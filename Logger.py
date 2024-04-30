from datetime import datetime
from tkinter import Label, Frame


class Logger:
    log_setup = {
        "vaal_orb": {
            "log_path": "vaal_orb_log.txt",
            "log_labels": [
                "Gem name",
                "Gem cost",
                "lvl up",
                "lvl down",
                "qual up",
                "qual down",
                "no change",
                "avg return (c)",
                "Last seen"
            ]
        },
        "awakened_level": {
            "log_path": "Awakened_leveling_log.txt",
            "log_labels": [
                "Gem name",
                "Gem cost",
                "Beast cost",
                "Quality cost",
                "lvl 5 cost",
                "",
                "",
                "avg return (c)",
                "Last seen"
            ]
        }
    }

    def __init__(self, root, log_path="vaal_orb_log.txt"):
        self.root = root
        self.log_labels = []
        self.font = ("Comic Sans MS", 11, "bold")
        self.topPadding = (80, 5)

        self.log_name = Label(self.root, text="Gem name", bg="black", fg="gold", font=self.font)
        self.log_name.grid(column=1, row=5, pady=self.topPadding)

        self.log_cost = Label(self.root, text="Gem cost", bg="black", fg="gold", font=self.font)
        self.log_cost.grid(column=2, row=5, pady=self.topPadding)

        self.log_lvl_up = Label(self.root, text="lvl up", bg="black", fg="gold", font=self.font)
        self.log_lvl_up.grid(column=3, row=5, pady=self.topPadding)

        self.log_lvl_down = Label(self.root, text="lvl down", bg="black", fg="gold", font=self.font)
        self.log_lvl_down.grid(column=4, row=5, pady=self.topPadding)

        self.log_qual_up = Label(self.root, text="qual up", bg="black", fg="gold", font=self.font)
        self.log_qual_up.grid(column=5, row=5, pady=self.topPadding)

        self.log_qual_down = Label(self.root, text="qual down", bg="black", fg="gold", font=self.font)
        self.log_qual_down.grid(column=6, row=5, pady=self.topPadding)

        self.log_no_change = Label(self.root, text="no change", bg="black", fg="gold", font=self.font)
        self.log_no_change.grid(column=7, row=5, pady=self.topPadding)

        self.log_result = Label(self.root, text="avg return (c)", bg="black", fg="gold", font=self.font)
        self.log_result.grid(column=8, row=5, pady=self.topPadding)

        self.last_update = Label(self.root, text="Last seen", bg="black", fg="gold", font=self.font)
        self.last_update.grid(column=9, row=5, pady=self.topPadding)
        self.current_log = log_path

    def readLog(self, file_name="vaal_orb_log.txt"):
        try:
            f = open(file_name, "r")
            lines = f.readlines()
            f.close()

            for label in self.log_labels:
                label.grid_forget()
            self.log_labels.clear()

            for i in range(0, len(lines)):
                line = lines[i].split(",")
                line[-1] = line[-1].replace("\n", "")
                for j in range(len(line)):
                    text = line[j]
                    if j == len(line) - 1:
                        try:
                            now = datetime.now()
                            then = datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")
                            diff = now - then
                            minutes = diff.total_seconds() / 60
                            text = f"{int(minutes)} min ago"
                        except ValueError as e:
                            print(f"Error converting text to datetime: {e}")
                            return

                    label = Label(self.root, text=text, bg="black", fg="gold", font=self.font)
                    self.log_labels.append(label)
                    label.grid(column=j + 1, row=i * 2 + 6)

                # Add a separation line below each row
                separator = Frame(self.root, height=2, bg="#5c0e02")
                separator.grid(column=1, row=i * 2 + 7, columnspan=len(line), sticky='we')
                self.log_labels.append(separator)
        except:
            return

    def forget(self):
        for label in self.log_labels:
            label.grid_forget()
        self.log_labels.clear()

        # Forgets padding aswell when doing this
        # self.log_name.grid_forget()
        # self.log_cost.grid_forget()
        # self.log_lvl_up.grid_forget()
        # self.log_lvl_down.grid_forget()
        # self.log_qual_up.grid_forget()
        # self.log_qual_down.grid_forget()
        # self.log_no_change.grid_forget()
        # self.log_result.grid_forget()
        # self.last_update.grid_forget()

    def init_vaal_orb_log(self):
        self.log_name.config(text=self.log_setup["vaal_orb"]["log_labels"][0])
        self.log_cost.config(text=self.log_setup["vaal_orb"]["log_labels"][1])
        self.log_lvl_up.config(text=self.log_setup["vaal_orb"]["log_labels"][2])
        self.log_lvl_down.config(text=self.log_setup["vaal_orb"]["log_labels"][3])
        self.log_qual_up.config(text=self.log_setup["vaal_orb"]["log_labels"][4])
        self.log_qual_down.config(text=self.log_setup["vaal_orb"]["log_labels"][5])
        self.log_no_change.config(text=self.log_setup["vaal_orb"]["log_labels"][6])
        self.log_result.config(text=self.log_setup["vaal_orb"]["log_labels"][7])
        self.last_update.config(text=self.log_setup["vaal_orb"]["log_labels"][8])

    def init_awakened_level_log(self):
        self.log_name.config(text=self.log_setup["awakened_level"]["log_labels"][0])
        self.log_cost.config(text=self.log_setup["awakened_level"]["log_labels"][1])
        self.log_lvl_up.config(text=self.log_setup["awakened_level"]["log_labels"][2])
        self.log_lvl_down.config(text=self.log_setup["awakened_level"]["log_labels"][3])
        self.log_qual_up.config(text=self.log_setup["awakened_level"]["log_labels"][4])
        self.log_qual_down.config(text=self.log_setup["awakened_level"]["log_labels"][5])
        self.log_no_change.config(text=self.log_setup["awakened_level"]["log_labels"][6])
        self.log_result.config(text=self.log_setup["awakened_level"]["log_labels"][7])
        self.last_update.config(text=self.log_setup["awakened_level"]["log_labels"][8])
