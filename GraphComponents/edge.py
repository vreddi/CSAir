__author__ = 'vishrutreddi'

'''
--------------------------------------------------------------------------------------X
GRAPH COMPONENT: EDGE  |                                                              |
-----------------------                                                               |
                                                                                      |
This file represents the paths which are modeled as edges in a  connected graph.      |




DATA STRUCTURE INFO:                                                                  |
'ports[0]' corresponds to Source Node (City Code)                                     |
'ports[1]' corresponds to Destination Node (City Code)                                |
'distance' corresponds to the numerical distance between the 2 ports.                 |
--------------------------------------------------------------------------------------X
'''

class edge:

    def __init__(self, route):

        self.ports = route['PORTS']
        self.distance = route['DISTANCE']
