__author__ = 'vishrutreddi'

import operator
import webbrowser


'''
------------------------------------------------------------------------------------------X
GRAPH COMPONENT: GRAPH |                                                                  |
-----------------------                                                                   |
                                                                                          |
                                                                                          |
                                                                                          |
------------------------------------------------------------------------------------------X
'''


class graph:

    # List of Locations/Places on the Map(Graph)
    # Note: Edges for each node are attached with the node object
    nodeList = []

    #List of Travel Paths between Places on the Map(Graph)
    routeList = []



    # This method adds a location/place in the current graph
    def addNode(self, node):

        self.nodeList.append(node)



    # This method adds a path/edge in the current graph which exists
    # between 2 places/locations/nodes
    def addRoute(self, route):

        self.routeList.append(route)


    def pathExists(self, source, destination):

        for edge in self.routeList:

            if(edge.source == source and edge.destination == destination):
                return True


        return False


    # This function checks if the City Name Provided as a parameter exists in the Graph.
    # According to the answer a True/False value is returned.
    #
    # @param cityName
    # @return True/False
    def cityNameExists(self, cityName):

        for metro in self.nodeList:

            if(cityName.lower() == metro['NAME'].lower()):
                return True


        return False


    # This function checks if the City Code Provided as a parameter exists in the Graph.
    # According to the answer a True/False value is returned.
    #
    # @param cityCode
    # @return True/False
    def cityCodeExists(self, cityCode):

        for metro in self.nodeList:

            if(cityCode.lower() == metro['CODE'].lower()):
                return True


        return False


    # This function checks if the Route Provided as a parameter (Source and Destination) exists in the Graph.
    # According to the answer a True/False value is returned.
    #
    # @param source
    # @param destination
    # @return True/False
    def routeExists(self, source, destination):

        for route in self.routeList:

            # Route Found
            if(route['PORTS'][0] == source and route['PORTS'][1] == destination):
                return True

        # Route Not Found
        return False



    def getCitiesSingleFlightAway(self, sourceCity):

        singleFlightAwayList = []

        for route in self.routeList:

            if(route['PORTS'][0]  == sourceCity['CODE']):

                cityName = self.codeToCityName(route['PORTS'][1])

                singleFlightAwayList.append(cityName + ' - ' + route['PORTS'][1] + ' ' + '(Distance: ' + str(route['DISTANCE']) + ')')


        return singleFlightAwayList


    # Finds the flight with Maximum distance coverage for one single trip. It creates a string
    # with flight details which includes the 2 ports and the total distance and provides that as the
    # answer.
    #
    # @return A String with Longest Flight Details
    def getLongestFlight(self):

        # To store the Answer/ Flight Details
        answer = ''

        # Temporary Storage for all the FLight Distances
        tempDistanceList = []

        # Adding all the Distances on the CSAir Network in the List
        for route in self.routeList:

            tempDistanceList.append(route['DISTANCE'])

        # Getting Max Distance
        maxDist = max(tempDistanceList)

        # Getting other details of the Max Distance Flight and creating answer
        for route in self.routeList:

            if(maxDist == route['DISTANCE']):
                answer += 'Flight: ' + route['PORTS'][0] + ' -> ' + route['PORTS'][1] + ' , Total Distance: ' + str(maxDist) + '\n'


        # Validating if there is some flight with max distance or not
        if(len(answer) == 0):
            return '- No Flight in Record -'

        else:
            return answer




    # Finds the flight with Minimum distance coverage for one single trip. It creates a string
    # with flight details which includes the 2 ports and the total distance and provides that as the
    # answer.
    #
    # @return A String with Shortest Flight Details
    def getShortestFlight(self):

        # To store the Answer/ Flight Details
        answer = ''

        # Temporary Storage for all the FLight Distances
        tempDistanceList = []

        # Adding all the Distances on the CSAir Network in the List
        for route in self.routeList:

            tempDistanceList.append(route['DISTANCE'])

        # Getting Min Distance
        minDist = min(tempDistanceList)

        # Getting other details of the Max Distance Flight and creating answer
        for route in self.routeList:

            if(minDist == route['DISTANCE']):
                answer += 'Flight: ' + route['PORTS'][0] + ' -> ' + route['PORTS'][1] + ' , Total Distance: ' + str(minDist) + '\n'


        # Validating if there is some flight with min distance or not
        if(len(answer) == 0):
            return '- No Flight in Record -'

        else:
            return answer



    # Computes the average distance for a single flight on the CSAir Network and then stores
    # that in the result string and returns that for presentation.
    #
    # @return A String with Average Flight Distance
    def getAverageFlightDistance(self):

        # To store the Answer/ Flight Details
        answer = ''

        # Temporary Storage for all the Flight Distances
        tempDistanceList = []

        # Adding all the Distances on the CSAir Network in the List
        for route in self.routeList:

            tempDistanceList.append(route['DISTANCE'])

        # Getting Average Distance
        avgDist = sum(tempDistanceList)/len(tempDistanceList)

        # Creating answer
        answer = 'Average Distance: ' + str(avgDist)

        return answer




    # Finds the City which is the Biggest in terms of population to which the CSAir serves.
    # This method creates an answer string that is provided for presentation.
    #
    # @return A String with Biggest City Details
    def getBiggestCity(self):

        # To store the Answer/ City Details
        answer = ''

        # Temporary Storage for all the City Populations
        tempPopulationList = []

        # Adding all the Populations on the CSAir Network in the List
        for city in self.nodeList:

            tempPopulationList.append(city['POPULATION'])

        # Getting Max Population
        maxPop = max(tempPopulationList)

        # Getting other details of the Max Population City and creating answer
        for city in self.nodeList:

            if(maxPop == city['POPULATION']):
                answer += 'Biggest City: ' + city['NAME'] + ' (' + city['CODE'] + ') , Population: ' + str(maxPop) + '\n'


        # Validating if there is some city which is the biggest or not
        if(len(answer) == 0):
            return '- No City in Record -'

        else:
            return answer




    # Finds the City which is the Smallest in terms of population to which the CSAir serves.
    # This method creates an answer string that is provided for presentation.
    #
    # @return A String with Smallest City Details
    def getSmallestCity(self):

        # To store the Answer/ City Details
        answer = ''

        # Temporary Storage for all the City Populations
        tempPopulationList = []

        # Adding all the Populations on the CSAir Network in the List
        for city in self.nodeList:

            tempPopulationList.append(city['POPULATION'])

        # Getting Min Population
        minPop = min(tempPopulationList)

        # Getting other details of the Min Population City and creating answer
        for city in self.nodeList:

            if(minPop == city['POPULATION']):
                answer += 'Smallest City: ' + city['NAME'] + ' (' + city['CODE'] + ') , Population: ' + str(minPop) + '\n'


        # Validating if there is some city which is the smallest or not
        if(len(answer) == 0):
            return '- No City in Record -'

        else:
            return answer



    # Computes the average population for all the cities on the CSAir Network and then stores
    # that in the result string and returns that for presentation.
    #
    # @return A String with Average Population Size
    def getAverageCitySize(self):

        # To store the Answer/ Flight Details
        answer = ''

        # Temporary Storage for all the Populations
        tempPopulationList = []

        # Adding all the Populations on the CSAir Network in the List
        for route in self.routeList:

            tempPopulationList.append(route['DISTANCE'])

        # Getting Average Population
        avgPop = sum(tempPopulationList)/len(tempPopulationList)

        # Creating answer
        answer = 'Average Population: ' + str(avgPop)

        return answer




    def printContinentsWithCities(self):

        # A list with Unique Continent Names that CSAir serves
        tempUniqueContinentsList = []


        # Adding all the Unique Continents to the List
        for metro in self.nodeList:

            if metro['CONTINENT'] not in tempUniqueContinentsList:
                tempUniqueContinentsList.append(metro['CONTINENT'])


        for continent in tempUniqueContinentsList:

            print('\n')
            print('Continent: ' + continent)
            print('Cities in ' + continent + ': ')

            for metro in self.nodeList:

                if(metro['CONTINENT'] == continent):
                    print(metro['NAME'])




    def printHubCities(self):

        connectionDict = {}

        # Creating a Dictionary with Cities and making connections for each city 0
        for city in self.nodeList:

            connectionDict[city['CODE']] = 0


        # Updating Connections for each City
        for route in self.routeList:

            connectionDict[route['PORTS'][0]] += 1
            connectionDict[route['PORTS'][1]] += 1


        maximumConnectionCity = max(connectionDict, key=connectionDict.get)
        maximumConnections = connectionDict[maximumConnectionCity]

        print('Hub Cities: ')
        for code in connectionDict:

            if (connectionDict[code] == maximumConnections):
                print(self.codeToCityName(code) + ' (' + code + ')')






    def codeToCityName(self, code):

        for metro in self.nodeList:

            if(metro['CODE'] == code):
                return metro['NAME']

        return "The Code Does not Exist in our Data-base"



    def cityNameToCode(self, cityName):

        for metro in self.nodeList:

            if(metro['NAME'] == cityName):
                return metro['CODE']

        return "The City Does not Exist in our Data-base"





    def printAllRoutes(self, cityCode):

        for route in self.routeList:

            if(route['PORTS'][0] == cityCode or route['PORTS'][1] == cityCode):
                print(route['PORTS'][0] + " -> " + route['PORTS'][1])


    # This functions creates the URL for the Great Circle Mapper and opens the map
    # in the browser with the map for the travel path presented. The Travel path is
    # passed to the function as a String with the path extending from source to destination.
    # eg: "LAX-LIM-MEX"
    # Note: The URL is opened in the Default Browser for the machine running the function.
    def greatCircleMapURLMaker(self, travelPath):

        baseURL = "http://www.gcmap.com/mapui?P="
        finalURL = baseURL +  travelPath

        webbrowser.open(finalURL)




    # This method given a code for a city checks if that city is present in the current graph.
    # If found, then that city is removed from the graph and the network is reorganized. The re-organization
    # makes the graph eliminate that node and all the edges connected to that node.
    #
    # Note: The Node/City is removed ONLY for this run of the program. If you want to make it permanent then the
    # Graph needs to be saved.
    #
    # @param cityCode
    def removeACity(self, cityCode):

        returnMessage = "CSAir_System_Message :: The Provided City Code does not exist. No Deletions Made."
        removedRouteCount = 0

        # If Found, remove the node from the graph
        for city in self.nodeList:

            if(city['CODE'] == cityCode):
                returnMessage = "CSAir_System_Message :: City: " + self.codeToCityName(cityCode) + " (" + cityCode + ") has been removed from the Data-Set."
                self.nodeList.remove(city)

        #Contains all routes, except the routes which are to be removed
        tempRouteList = []

        # If Found, remove all the edges that connected to that node
        for route in self.routeList:

            # If a route exists containing the city which is about to be removed then
            # remove those routes
            if(route['PORTS'][0] != cityCode and route['PORTS'][1] != cityCode):
                tempRouteList.append(route)

        removedRouteCount = len(self.routeList) - len(tempRouteList)

        self.routeList.clear()

        # Re-formatting the Route List for the Graph with edges/connections that should be
        # present and that are not supposed to be removed.
        for route in tempRouteList:
            self.routeList.append(route)

        returnMessage = "\nCSAir_System_Message :: Total Connections Removed = " + str(removedRouteCount)

        return returnMessage




    # This function removes a route from the graph between 2 cities. The codes of the 2 cities between
    # whose the the route needs to be deleted are supplied by the user as parameters to the function.
    # Function returns a acknowledge message for the user to acknowledge if the function has been successful
    # or not.
    #
    # @param cityCode1
    # @param cityCode2
    # @return returnMessage
    def removeARoute(self, cityCode1, cityCode2):

        newRouteList = []
        returnMessage = "\nCSAir_System_Message :: No Route between the input cities Exist \n Please Verify the Route and/or City Codes."

        for route in self.routeList:

            # Found the Route! Don't add it to the new list of Routes
            if(cityCode1 == route['PORTS'][0] and cityCode2 == route['PORTS'][1]):
                print()

            # This is not the Route to be deleted. Add it to the new route list
            else:
                newRouteList.append(route)



        if(len(newRouteList) != len(self.routeList)):
            returnMessage = "Route between Source: " + self.codeToCityName(cityCode2) + " (" + cityCode1 + ") and Destination: " + self.codeToCityName(cityCode2) + " (" + cityCode2 + ") has been removed."

        # Clearing the Old Route List
        self.routeList.clear()

        # Giving the Graph a new list of Routes
        for route in newRouteList:
            self.routeList.append(route)

        # Return the message for the user to acknowledge
        return returnMessage



    # This Function Edits the Name of the City. This Function does not check for the fact
    # if the new City Name already exists in the list of cities currently in the Network or not. This
    # is very IMPORTANT to note! If the city-name existence is not checked before calling this function
    # then the CSAir data becomes invalid.
    # A True/False value is returned if the edit is made or not.
    #
    # @param old
    # @param new
    # @return True/False
    def editCityName(self, old, new):

        for metro in self.nodeList:

            # If City Found then the Edit is Made
            if(metro['NAME'] == old):
                metro['NAME'] = new
                return True

        return False



    # This Function Edits the Code of the City. This Function does not check for the fact
    # if the new City Code already exists in the list of cities currently in the Network or not. This
    # is very IMPORTANT to note! If the city-code existence is not checked before calling this function
    # then the CSAir data becomes invalid.
    # A True/False value is returned if the edit is made or not.
    #
    # @param old
    # @param new
    # @return True/False
    def editCityCode(self, old, new):

        for metro in self.nodeList:

            # If City Found then the Edit is Made
            if(metro['CODE'] == old):
                metro['CODE'] = new
                return True

        return False



    # This Function Edits the Country of the City. This Function does not check for the fact
    # if the new Country is valid or not by the CSAir Network Allowance conditions. This
    # is very IMPORTANT to note! If the Country validity is not checked before calling this function
    # then the CSAir data becomes invalid.
    # A True/False value is returned if the edit is made or not.
    #
    # @param cityCode
    # @param newCountry
    # @return True/False
    def editCityCountry(self, cityCode, newCountry):

        for metro in self.nodeList:

            # If City Found then the Edit is Made
            if(metro['CODE'] == cityCode):
                metro['COUNTRY'] = newCountry
                return True

        return False




    # This Function Edits the Continent of the City. This Function does not check for the fact
    # if the new Continent is valid or not by the CSAir Network Allowance conditions. This
    # is very IMPORTANT to note! If the continent validity is not checked before calling this function
    # then the CSAir data becomes invalid.
    # A True/False value is returned if the edit is made or not.
    #
    # @param cityCode
    # @param newContinent
    # @return True/False
    def editCityContinent(self, cityCode, newContinent):

        for metro in self.nodeList:

            # If City Found then the Edit is Made
            if(metro['CODE'] == cityCode):
                metro['CONTINENT'] = newContinent
                return True

        return False



    # This Function Edits the Time-Zone of the City. This Function does not check for the fact
    # if the new Time-Zone is valid or not by the CSAir Network Allowance conditions. This
    # is very IMPORTANT to note! If the Time-Zone validity is not checked before calling this function
    # then the CSAir data becomes invalid.
    # A True/False value is returned if the edit is made or not.
    #
    # @param cityCode
    # @param newTImeZone
    # @return True/False
    def editCityTimeZone(self, cityCode, newTimeZone):

        for metro in self.nodeList:

            # If City Found then the Edit is Made
            if(metro['CODE'] == cityCode):
                metro['TIMEZONE'] = newTimeZone
                return True

        return False



    # This Function Edits the Population of the City. This Function does not check for the fact
    # if the new Population is valid or not by the CSAir Network Allowance conditions. This
    # is very IMPORTANT to note! If the population validity is not checked before calling this function
    # then the CSAir data becomes invalid.
    # A True/False value is returned if the edit is made or not.
    #
    # @param cityCode
    # @param newPopulation
    # @return True/False
    def editCityPopulation(self, cityCode, newPopulation):

        for metro in self.nodeList:

            # If City Found then the Edit is Made
            if(metro['CODE'] == cityCode):
                metro['POPULATION'] = newPopulation
                return True

        return False



    # This Function Edits the Region of the City. This Function does not check for the fact
    # if the new Region is valid or not by the CSAir Network Allowance conditions. This
    # is very IMPORTANT to note! If the Region validity is not checked before calling this function
    # then the CSAir data becomes invalid.
    # A True/False value is returned if the edit is made or not.
    #
    # @param cityCode
    # @param newPopulation
    # @return True/False
    def editCityRegion(self, cityCode, newRegion):

        for metro in self.nodeList:

            # If City Found then the Edit is Made
            if(metro['CODE'] == cityCode):
                metro['REGION'] = newRegion
                return True

        return False