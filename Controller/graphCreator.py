__author__ = 'vishrutreddi'

import json
from GraphComponents.graph import graph

class graphCreator():

    # Storage for JSON Extraction
    metroList = []
    routeList = []


    # Graph Reference that the Graph-Creator Object Creates
    graphNetwork = graph()

    def __init__(self):
        return


    # This method parses the JSON file (given) to extract the metros with all its key-value information
    # and stores it in the graphCreator object's local reference
    def parseMetroJSON(self):

        json_data = open('/Users/vishrutreddi/Documents/PycharmProjects/CSAir/Resources/map_data.json', 'r')
        data = json.load(json_data)

        for data_obj in data['metros']:

            # Creating a dictionary for each location object
            metro = {}

            #Filling in Location information
            metro['CODE'] = data_obj['code']
            metro['CONTINENT'] = data_obj['continent']
            metro['COORDINATES'] = data_obj['coordinates']
            metro['COUNTRY'] = data_obj['country']
            metro['NAME'] = data_obj['name']
            metro['POPULATION'] = data_obj['population']
            metro['REGION'] = data_obj['region']
            metro['TIMEZONE'] = data_obj['timezone']

            # Add the Dictionary Object to the List of Locations
            self.metroList.append(metro)


        json_data.close()



    # This method parses the JSON file (given) to extract the routes with all its key-value information
    # and stores it in the graphCreator object's local reference
    def parseRouteJSON(self):

        json_data = open('/Users/vishrutreddi/Documents/PycharmProjects/CSAir/Resources/map_data.json', 'r')
        data = json.load(json_data)

        for data_obj in data['routes']:

            # Creating Route in the one direction
            route1 = {}
            route1['PORTS'] = list(data_obj['ports'])
            route1['DISTANCE'] = data_obj['distance']

            # Adding Route in one direction
            self.routeList.append(route1)

            # Creating Route in the opposite direction
            route2 = {}

            # list() is used to get a copy and not reference of the data list
            route2['PORTS'] = list(data_obj['ports'])
            route2['PORTS'].reverse()
            route2['DISTANCE'] = data_obj['distance']

            # Adding Route in the opposite direction
            self.routeList.append(route2)




    def createGraph(self):

        # Adding all Nodes
        for metro in self.metroList:

            # Add Each Node to the Graph
            self.graphNetwork.addNode(metro)

        # Adding All Edges
        for route in self.routeList:

            # Add Each Edge to the Graph
            self.graphNetwork.addRoute(route)


    def getGraph(self):
        return self.graphNetwork





