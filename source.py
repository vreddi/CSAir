__author__ = 'vishrutreddi'

from Controller.graphCreator import graphCreator
from Controller.menuController import menuController


g = graphCreator()
menu = menuController()


# Parse JSON Data
g.parseMetroJSON()
g.parseRouteJSON()

# Creating the Network Graph from JSON Data
g.createGraph()

menu.startMenu(g)

