from tkinter import *
from PIL import Image, ImageTk
from AwakenedLevelingCalculator import AwakenedLevelingCalculator
from Logger import Logger
from VaalOrbCalculator import VaalOrbCalculator


class SceneManager:
    def __init__(self):
        self.currentView = None
        self.background_image = None
        self.background_image_label = None
        self.root = self.newRoot()
        self.logger = Logger(self.root)

        self.ViewVaalOrbCalculator()


    def newRoot(self):
        root = Tk()
        root.title("Calculator")
        root.geometry("1400x600")
        root.config(bg="darkgrey")
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(10, weight=5)

        menu = Menu(root)
        item = Menu(menu)
        item.add_command(label="Vaal Orb", command=self.ViewVaalOrbCalculator)
        item.add_command(label="Awakened Gem lvl", command=self.viewAwakenedLevelingCalculator)
        item.config(bg="darkgrey")
        menu.add_cascade(label="File", menu=item)
        root.config(menu=menu)

        self.background_image_label = Label(root)
        self.background_image_label.place(x=0, y=0, relwidth=1, relheight=1)
        return root

    def ViewVaalOrbCalculator(self):
        if self.currentView is not None:
            self.currentView.forget()
        if self.logger is not None:
            self.logger.forget()

        self.setBackground(VaalOrbCalculator.background_image_path)
        self.currentView = VaalOrbCalculator(self.root, self.logger)

    def viewAwakenedLevelingCalculator(self):
        if self.currentView is not None:
            self.currentView.forget()
            self.logger.init_vaal_orb_log()
        if self.logger is not None:
            self.logger.forget()
            self.logger.init_awakened_level_log()

        self.setBackground(AwakenedLevelingCalculator.background_image_path)
        self.currentView = AwakenedLevelingCalculator(self.root, self.logger)

    def setBackground(self, path):
        img = Image.open(path)
        img = img.resize((3000, 600))
        self.background_image = ImageTk.PhotoImage(img)
        self.background_image_label.config(image=self.background_image)


# -- main --
sceneManager = SceneManager()
sceneManager.root.mainloop()
