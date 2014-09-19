'''
Created on 12 aug 2014

@author: HaNaK0
'''
from tkinter import *
import widgets
import workspace


root = Tk()
images = workspace.loadImages()
workspace = workspace.Workspace(root, widgets.StatusBar(root, images), images, gridX = 32, gridY = 32, width = 1920 * 3, height = 1080)
root.config(menu = widgets.MenuBar(root, workspace, images))
root.geometry("600x600")
root.title("RBR_LD")
root.mainloop()
