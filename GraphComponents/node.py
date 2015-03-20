__author__ = 'vishrutreddi'

'''
------------------------------------------------------------------------------------------X
GRAPH COMPONENT: NODE  |                                                                  |
-----------------------                                                                   |
                                                                                          |
This file represents the locations which are modeled as nodes of a connected graph.       |
                                                                                          |
------------------------------------------------------------------------------------------X
'''


class node:

    def __index__(self, metro):
        self.code = metro['CODE']
        self.name = metro['NAME']
        self.country = metro['COUNTRY']
        self.continent = metro['CONTINENT']
        self.timezone = metro['TIMEZONE']
        self.coordinates = metro['COORDINATES']
        self.population = metro['POPULATION']
        self.region = metro['REGION']




    # This function for the current node/cities finds all the cities that are connected
    # to this city, meaning that a single flight exists from a city to the current city.
    # For all the connecting cities, a list is established which includes all those cities.
    # This list is then returned.
    def getConnectedCitiesToCurrent(self, graphMaker):

        connectedCities = []

        network = graphMaker.getGraph()

        for route in network.routeList:

            if(route['PORTS'][0] == self.code):
                connectedCities.append(route['PORTS'][1])

            elif(route['PORTS'][1] == self.code):
                connectedCities.append(route['PORTS'][0])


        # A list of codes of the connected cities returned
        return connectedCities

