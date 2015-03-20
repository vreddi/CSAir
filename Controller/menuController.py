__author__ = 'vishrutreddi'


from View.ConsoleUI import ConsoleUI
from Controller.graphCreator import graphCreator

class menuController:

    # Helps in determining which Menu Screen the User is currently on
    currentMenuScreen = 'MainMenuScreen'

    # User can request info about any city, and this reference helps in deciding
    # which city is requested by the User
    currentCityInfoRequest = ''


    def __index__(self):
        return



    def getInputFromUser(self, graphMaker):

        if(self.currentMenuScreen.lower() == 'mainmenuscreen'):

            self.mainScreenAttachFunction(graphMaker)

        elif(self.currentMenuScreen.lower() == 'citymenuscreen'):

            self.cityScreenAttachFunction(graphMaker)

        elif(self.currentMenuScreen.lower() == 'statisticalmenuscreen'):

            self.statisticalScreenAttachFunction(graphMaker)

        elif(self.currentMenuScreen.lower() == 'routenetworkeditmenuscreen'):

            self.routeNetworkEditScreenAttachFunction(graphMaker)


    #
    # @param graphMaker : The Object responsible for the creation of Current Graphs In Use
    def startMenu(self, graphMaker):
        self.currentMenuScreen = 'MainMenuScreen'
        view = ConsoleUI()
        view.printMainInstructions()
        self.getInputFromUser(graphMaker)

    def mainScreenAttachFunction(self, graphMaker):

        choice = input('Choice: ')

        if(choice == '1'):
            print('\n \n')
            self.getAllCities(graphMaker.getGraph())
            graphMaker.getGraph().greatCircleMapURLMaker("LAX-LIM-MEX")

            # Request Completed, Revert Back to the Start Menu
            print('\n')
            self.startMenu(graphMaker)

        elif(choice == '2'):
            view = ConsoleUI()
            print('\n')
            self.currentCityInfoRequest = input('Enter the Name of the City: ')
            found = False

            for metro in graphMaker.getGraph().nodeList:

                if(metro['NAME'].lower() == self.currentCityInfoRequest.lower()):

                    self.currentCityInfoRequest = metro
                    found = True
                    break

            if(not found):
                print('\n')
                print('City Not Found, CSAir Does not Service your City.')
                print('Sorry for the inconvenience.')
                input('Press Return to Continue...')
                print('\n')
                self.startMenu(graphMaker)

            else:
                print(' \n')
                view.printCityInfoInstructions()
                self.currentMenuScreen = 'CityMenuScreen'
                self.getInputFromUser(graphMaker)


        elif(choice == '3'):
            view = ConsoleUI()
            print(' \n \n')
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        elif(choice == '4'):
            view = ConsoleUI()
            print(' \n \n')
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        elif(choice == '6'):
            exit()

        else:
            print('Invalid Choice, Try Again: ')
            self.getInputFromUser(graphMaker)


    #
    # @param graphMaker : The Object responsible for the creation of Current Graphs In Use
    def cityScreenAttachFunction(self, graphMaker):

        choice = input('Choice: ')
        cityInRequest = self.currentCityInfoRequest


        if(choice == '1'):
            print('\n City Code: ' + cityInRequest['CODE'])
            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)


        elif(choice == '2'):
            print('\n City Name: ' + cityInRequest['NAME'])
            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)


        elif(choice == '3'):
            print('\n City Country: ' + cityInRequest['COUNTRY'])
            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)

        elif(choice == '4'):
            print('\n City Continent: ' + cityInRequest['CONTINENT'])
            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)

        elif(choice == '5'):
            print('\n City Time-Zone: ' + str(cityInRequest['TIMEZONE']))
            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)

        elif(choice == '6'):
            print('\n City Population: ' + str(cityInRequest['POPULATION']))
            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)

        elif(choice == '7'):
            print('\n City Region: ' + str(cityInRequest['REGION']))
            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)

        elif(choice == '8'):

            singleFlightCityList = graphMaker.getGraph().getCitiesSingleFlightAway(cityInRequest)

            print('\n')
            for city in singleFlightCityList:
                print(city)

            input('Press Return to Continue...\n')
            self.currentMenuScreen = 'CityMenuScreen'
            view = ConsoleUI()
            view.printCityInfoInstructions()
            self.getInputFromUser(graphMaker)

        elif(choice == '9'):
            print('\n')
            self.startMenu(graphMaker)

        elif(choice == '10'):
            exit()

        else:
            print('Invalid Choice, Try Again: ')
            self.getInputFromUser(graphMaker)



    # This method acts like a gateway for methods that provide all the statistical data related to
    # CSAir.
    #
    # @param graphMaker : The Object responsible for the creation of Current Graphs In Use
    def statisticalScreenAttachFunction(self, graphMaker):

        choice = input('Choice: ')

        network = graphMaker.getGraph()

        # Get the Longest Single Flight Details in the CSAir Network
        if(choice == '1'):
            print('\n')
            ans = network.getLongestFlight()
            print(ans)
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get the Shortest Single Flight Details in the CSAir Network
        elif(choice == '2'):
            print('\n')
            ans = network.getShortestFlight()
            print(ans)
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get the Average Distance of all the Flights in the Network
        elif(choice == '3'):
            print('\n')
            ans = network.getAverageFlightDistance()
            print(ans)
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get the Biggest City (by Population) served by CSAir
        elif(choice == '4'):
            print('\n')
            ans = network.getBiggestCity()
            print(ans)
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get the smallest city (by Population) served by CSAir
        elif(choice == '5'):
            print('\n')
            ans = network.getSmallestCity()
            print(ans)
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get the Average Size (by Population) of all the cities served by CSAir
        elif(choice == '6'):
            print('\n')
            ans = network.getAverageCitySize()
            print(ans)
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get the list of all the continents served by CSAir and the Cities within it
        elif(choice == '7'):
            print('\n')
            network.printContinentsWithCities()
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get all the CSAir's hub cities – the cities that have the most direct connections.
        elif(choice == '8'):
            print('\n')
            network.printHubCities()
            print('\n')
            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printStatisticalInstructions()
            self.currentMenuScreen = 'StatisticalMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get back to the previous menu
        elif(choice == '9'):
            print('\n')
            self.startMenu(graphMaker)

        # For Exiting the program
        elif(choice == '10'):
            exit()

        # If invalid choice entered
        else:
            print('Invalid Choice, Try Again: ')
            self.getInputFromUser(graphMaker)




    #
    #
    def routeNetworkEditScreenAttachFunction(self, graphMaker):

        choice = input('Choice: ')

        network = graphMaker.getGraph()

        # Remove a City
        if(choice == '1'):
            print('\n')
            cityCodeToRemove = ""
            print('1. Enter City Name to Remove')
            print('OR')
            print('2. Enter City Code to Remove')
            option = input('Choice: ')

            if(option == '1'):

                # Ask the User to enter the City Name
                cityName = input('Enter City Name: ')

                # Convert the City Name to its City Code
                cityCodeToRemove = network.cityNameToCode(cityName)

                # Assuming that cities could have a code up-to 5 characters long
                # A long string with the error message is returned if the city name
                # is not there in the JSON file
                if(len(cityCodeToRemove) > 5 ):

                    # Error Message Returned from the function
                    print(cityCodeToRemove)
                    print('Invalid Choice, Try Again: ')
                    view = ConsoleUI()
                    view.printRouteNetworkEditInstructions()
                    self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
                    self.getInputFromUser(graphMaker)

                # Remove the City from the Graph
                else:
                    returnMessage = network.removeACity(cityCodeToRemove)
                    print(returnMessage)

            elif(option == '2'):
                cityCode = input('Enter City Code: ')
                returnMessage = network.removeACity(cityCode)
                print(returnMessage)

            else:
                print('Invalid Choice, Try Again: ')
                view = ConsoleUI()
                view.printRouteNetworkEditInstructions()
                self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
                self.getInputFromUser(graphMaker)


            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Remove a route
        elif(choice == '2'):
            print('\n')
            print('Enter the City Codes for which you want to remove the connecting route.')
            cityCode1 = input('Enter Source City Code: ')
            cityCode2 = input('Enter Destination City Code: ')

            #Removing Route
            returnMessage = network.removeARoute(cityCode1, cityCode2)

            print(returnMessage)

            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Add a City, including all its necessary information
        elif(choice == '3'):

            # To see if the Data entered is Valid or Not
            processingError = False

            newCity = {}

            print('\n')
            print('Enter the Details of the City which will be added to CSAir: ')

            # Taking inputs for the new City from the User
            cityName = input('Enter the City Name: ')
            cityCode = input('Enter the City Code (MAX 4 Characters long): ')
            cityCountry = input('Enter the Name of ' + cityName +'s Country: ')
            cityContinent = input('Enter the Name of ' + cityName +'s Continent: ')
            cityRegion = input('Enter the Name of ' + cityName +'s Region: ')
            print('Enter the Name of ' + cityName +'s Coordinates (Note: Leave Blank for the Directions that are not available): ')
            cityCoordinatesN = input('North : ')
            cityCoordinatesS = input('South : ')
            cityCoordinatesE = input('East : ')
            cityCoordinatesW = input('West : ')
            cityCoordinates = {}
            cityTimeZone = input('Enter ' + cityName +'s Time-Zone: ')
            cityPopulation = input('Enter ' + cityName +'s Population: ')

            #Processing User Input...
            print('\nProcessing the new Data...')

            # Checks if the City Code already exists in CSAir Data Set
            codeExists = network.cityCodeExists(cityCode)

            # Checks if the CIty Name already exists in CSAir Data Set
            cityNameExists = network.cityNameExists(cityName)

            # Checking Validity of Country's Value
            if(len(cityCountry) < 0):
                processingError = True
                print('Invalid Country Name. Country Name Field cannot be left blank.')
                print('New City Addition Un-Successful...')

            # Checking Validity of City's Value
            if(len(cityContinent) < 0):
                processingError = True
                print('Invalid Continent Name. Continent Name Field cannot be left blank.')
                print('New City Addition Un-Successful...')

            # Checking Validity of Coordinates Entered
            if((len(cityCoordinatesN) > 0 or len(cityCoordinatesS) > 0) and (len(cityCoordinatesE) > 0 or len(cityCoordinatesW))):

                # Checking Validity of Coordinate Value (They should be numerical)
                try:
                    if(len(cityCoordinatesN) > 0):
                        valueN = int(cityCoordinatesN)

                    if(len(cityCoordinatesS) > 0):
                        valueS = int(cityCoordinatesS)

                    if( len(cityCoordinatesE) > 0):
                        valueE = int(cityCoordinatesE)

                    if( len(cityCoordinatesW) > 0):
                        valueW = int(cityCoordinatesW)

                except ValueError:
                    print('Coordinates should have a numerical value')
                    print('New City Addition Un-Successful...')
                    processingError = True

                # They are Valid so add them to the dictionary
                if(not processingError):
                    if(len(cityCoordinatesN) > 0):
                        cityCoordinates['N'] = int(cityCoordinatesN)

                    if(len(cityCoordinatesS) > 0):
                        cityCoordinates['S'] = int(cityCoordinatesS)

                    if( len(cityCoordinatesE) > 0):
                        cityCoordinates['E'] = int(cityCoordinatesE)

                    if( len(cityCoordinatesW) > 0):
                        cityCoordinates['W'] = int(cityCoordinatesW)

            # At-least one from N and S and one from E and W should be present
            else:
                processingError = True
                print('Insufficient Data for Coordinates. Unable to Process.')
                print('New City Addition Un-Successful...')

            # Checking Validity of Region Value
            try:
                value = int(cityRegion)

                if(value < 0):
                    processingError = True
                    print('Region should be a valid Integer')
                    print('New City Addition Un-Successful...')


            except ValueError:
                print('Region should be a valid Integer')
                print('New City Addition Un-Successful...')
                processingError = True

            # Checking Validity of Time-Zone Value
            try:
                value = int(cityTimeZone)
            except ValueError:
                print('Time-Zone should be a valid Integer')
                print('New City Addition Un-Successful...')
                processingError = True

            # Checking Validity of Population Value
            try:
                value = int(cityPopulation)
                if(value < 0):
                    processingError = True
                    print('Population should be a valid Integer')
                    print('New City Addition Un-Successful...')

            except ValueError:
                print('Population should be a valid Integer')
                print('New City Addition Un-Successful...')
                processingError = True


            if(codeExists or cityNameExists):
                print('CSAir_ERROR: City Name or City Code Entered already Exists.')
                print(' To add a new City to CSAir, the Name and code of the City should be unique')
                print('New City Addition Un-Successful...')
                processingError = True

            # If the Data entered is valid then we create the nde and add it to the graph network
            if(not processingError):

                # Add Details to the new dictionary
                newCity['CODE'] = cityCode
                newCity['NAME'] = cityName
                newCity['COUNTRY'] = cityCountry
                newCity['CONTINENT'] = cityContinent
                newCity['TIMEZONE'] = int(cityTimeZone)
                newCity['COORDINATES'] = cityCoordinates
                newCity['POPULATION'] = int(cityPopulation)
                newCity['REGION'] = int(cityRegion)

                # Add New Node to the Graph
                network.addNode(newCity)

                print('City: ' + cityName + ' (' + cityCode + ') Successfully Added.')

            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Add a Route, including all its necessary information
        elif(choice == '4'):
            print('\n')
            print('1. Create Route by City Names')
            print('OR')
            print('2. Create Route by City Codes')
            option = input('Choice: ')

            cityCodeSource = ''
            cityCodeDestination = ''
            distance = 0

            # To determine if the data is valid or not
            processingError = False

            # Enter by City Names
            if(option == '1'):

                # Ask the User to enter the Source and Destination
                cityNameSource = input('Enter Source City Name: ')
                cityNameDestination = input('Enter Destination City Name: ')

                # Convert the City Names to its City Codes
                cityCodeSource = network.cityNameToCode(cityNameSource)
                cityCodeDestination = network.cityNameToCode(cityNameDestination)

            # Enter by City Codes
            elif(option == '2'):
                cityCodeSource = input('Enter Source City Code: ')
                cityCodeDestination = input('Enter Destination City Code: ')

                # Check if both cities exist in the network
                sourceExists = network.cityCodeExists(cityCodeSource)
                destinationExists = network.cityCodeExists(cityCodeDestination)

            # Invalid Option by User
            else:
                print('Invalid Choice, Try Again:')
                view = ConsoleUI()
                view.printRouteNetworkEditInstructions()
                self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
                self.getInputFromUser(graphMaker)

            # Take Input Value for Distance
            distance = input('Enter the Distance Between Cities: ')

            print('\nProcessing Data...')

            # Check for Validity of the cities and distance
            sourceExists = network.cityCodeExists(cityCodeSource)
            destinationExists = network.cityCodeExists(cityCodeDestination)

            # Check for if the Source and Destination are entered to be the same
            # (User trying to be a Bad-Ass. CSAir still wont crash.)
            if(cityCodeSource == cityCodeDestination):
                print('Source and Destination are the same location. CSAir does not allow that.')
                print('New Route Addition Un-Successful...')
                processingError = True

            # Checking Validity of Distance Value
            try:
                value = int(distance)
                if(value < 0):
                    processingError = True
                    print('Distance Data is invalid. It has to be numeric and greater than 0')
                    print('New Route Addition Un-Successful...')

            except ValueError:
                print('Distance Data is invalid. It has to be numeric and greater than 0')
                print('New Route Addition Un-Successful...')
                processingError = True

            # Check if the Source and Destination Exists (Provide with Error Message)
            if(not sourceExists or not destinationExists):
                print('Entered Source or Destination is Invalid/The Data for that city does not exist in CSAir')
                print('Try Adding that City First...')
                print('New Route Addition Un-Successful...')
                processingError = True

            # Check if the Route already Exists
            routeExists = network.routeExists(cityCodeSource, cityCodeDestination)

            if(routeExists):
                processingError = True
                print('The Route You are trying to add already exists in the CSAir Network')
                print('New Route Addition Un-Successful...')

            # If no Processing Errors exist then add the route
            if(not processingError):

                # Create new Route Dictionary
                newRoute = {}

                # FIll in the Details for the new Route
                ports = [cityCodeSource, cityCodeDestination]
                newRoute['PORTS'] = ports
                newRoute['DISTANCE'] = distance

                # Add the Route to the Distance
                network.addRoute(newRoute)

                print('Route: ' + cityCodeSource + ' -> ' + cityCodeDestination + ' Successfully Added.')


            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Edit an Existing City
        elif(choice == '5'):
            print('\n')
            cityName = input('Enter the Name of the City you want to Edit: ')

            # Check if the CIty Exists in the Data-Set
            cityExists = network.cityNameExists(cityName)

            if(not cityExists):
                print('No such city exists in the CSAir DataSet.')
                print('Try Again as no Edits can be made for the entered the City')


            else:
                view = ConsoleUI()
                view.printCityEditOptions()
                subChoice = input('Choice: ')

                # Calling the Function that does the work for the selected option
                self.editCityDetails(cityName, graphMaker, subChoice)

            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Get Back to Previous Menu
        elif(choice == '6'):
            print('\n')
            self.startMenu(graphMaker)

        # Exit Program
        elif(choice == '7'):
            exit()




    #
    #
    #
    # @param originalCityName
    # @param graphMaker
    # @param choice
    #
    def editCityDetails(self, originalCityName, graphMaker, choice):

        # Get Access the to The Graph/CSAir Network
        network = graphMaker.getGraph()

        # To determine if the data entered is Valid or Not
        processingError = False

        # Edit the City Name
        if(choice == '1'):
            print('\n')
            newCityName = input('Enter the New City Name: ')

            nameExists = network.cityNameExists(newCityName)

            # Checking if the Name Entered already Exists
            if(nameExists):
                print('Sorry this City Name already exists in the CSAir Network')
                print('Try Using a Different Name')
                print('Edit Unsuccessful...')
                processingError = True

            # No Processing Errors, Editing the City Name
            if(not processingError):

                # Edit the Name in the Network
                network.editCityName(originalCityName, newCityName)

                print('Edit Successfully Made!')
                print('' + originalCityName + ' will now be known as: ' + newCityName)


            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Edit City Code
        elif(choice == '2'):
           print('\n')
           newCityCode = input('Enter the New City Code: ')

           codeExists = network.cityCodeExists(newCityCode)

           # Checking if the Name Entered already Exists
           if(codeExists):
               print('Sorry this City Code already exists in the CSAir Network')
               print('Try Using a Different COde')
               print('Edit Unsuccessful...')
               processingError = True


           # No Processing Errors, Editing the City Code
           if(not processingError):
               originalCityCode = network.cityNameToCode(originalCityName)
               network.editCityCode(originalCityCode, newCityCode)
               print('Edit Successfully Made!')
               print('' + originalCityCode + ' will now be known as: ' + newCityCode)

           input('Press Return to Continue... \n')
           view = ConsoleUI()
           view.printRouteNetworkEditInstructions()
           self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
           self.getInputFromUser(graphMaker)

        
        # Edit City Country
        elif(choice == '3'):
           print('\n')

           newCityCountry = input('Enter the New City Country: ')

           # No Processing Errors, Editing the City Country
           if(not processingError):

               # Get the Code for the City
               originalCityCode = network.cityNameToCode(originalCityName)

               # Change the Country Name
               network.editCityCountry(originalCityCode, newCityCountry)
               print('Edit Successfully Made!')
               print('' + originalCityName + '\'s Country will now be known as: ' + newCityCountry)

           input('Press Return to Continue... \n')
           view = ConsoleUI()
           view.printRouteNetworkEditInstructions()
           self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
           self.getInputFromUser(graphMaker)

        # Edit City Continent
        elif(choice == '4'):
            print('\n')

            newCityContinent = input('Enter the New City Continent: ')

            # No Processing Errors, Editing the City Continent
            if(not processingError):

                # Get the Code for the City
                originalCityCode = network.cityNameToCode(originalCityName)

                # Change the Continent Name
                network.editCityContinent(originalCityCode, newCityContinent)
                print('Edit Successfully Made!')
                print('' + originalCityName + '\'s Continent will now be known as: ' + newCityContinent)

            input('Press Return to Continue... \n')
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Edit City TimeZone
        elif(choice == '5'):
            print('\n')

            newCityTimeZone = input('Enter the New City Time-Zone: ')


            # Checking Validity of Time-Zone Value
            try:
                value = int(newCityTimeZone)
            except ValueError:
                print('Time-Zone should be a valid Integer')
                print('New City Addition Un-Successful...')
                processingError = True


            # No Processing Errors, Editing the City Time-Zone
            if(not processingError):

                # Get the Code for the City
                originalCityCode = network.cityNameToCode(originalCityName)

                # Change the Time-Zone
                network.editCityTimeZone(originalCityCode, newCityTimeZone)
                print('Edit Successfully Made!')
                print('' + originalCityName + '\'s Time-Zone will now be known as: ' + newCityTimeZone)

        # Edit the Population
        elif(choice == '6'):
            print('\n')

            newCityPopulation = input('Enter the New City Population: ')


            # Checking Validity of Population Value
            try:
                value = int(newCityPopulation)
                if(value < 0):
                    processingError = True
                    print('Population should be a valid Integer')
                    print('New City Addition Un-Successful...')

            except ValueError:
                print('Population should be a valid Integer')
                print('New City Addition Un-Successful...')
                processingError = True


            # No Processing Errors, Editing the City Population
            if(not processingError):

                # Get the Code for the City
                originalCityCode = network.cityNameToCode(originalCityName)

                # Change the Population
                network.editCityPopulation(originalCityCode, newCityPopulation)
                print('Edit Successfully Made!')
                print('' + originalCityName + '\'s Population is now: ' + newCityPopulation)

        # Edit Region
        elif(choice == '7'):
            print('\n')

            newCityRegion = input('Enter the New City Region: ')

            # Checking Validity of Region Value
            try:
                value = int(newCityRegion)

                if(value < 0):
                    processingError = True
                    print('Region should be a valid Integer')
                    print('New City Addition Un-Successful...')


            except ValueError:
                print('Region should be a valid Integer')
                print('New City Addition Un-Successful...')
                processingError = True


            # No Processing Errors, Editing the City Region
            if(not processingError):

                # Get the Code for the City
                originalCityCode = network.cityNameToCode(originalCityName)

                # Change the Population
                network.editCityRegion(originalCityCode, newCityRegion)
                print('Edit Successfully Made!')
                print('' + originalCityName + '\'s Region is now: ' + newCityRegion)

        # Edit the Coordinates
        elif(choice == '8'):
            print('\n')

        # Go to the Previous Menu
        elif(choice == '9'):
            view = ConsoleUI()
            view.printRouteNetworkEditInstructions()
            self.currentMenuScreen = 'RouteNetworkEditMenuScreen'
            self.getInputFromUser(graphMaker)

        # Exit the Program
        elif(choice == '10'):
            exit()



    # This function given a graph passed in as a parameter prints all the nodes/cities
    # present in that graph. Thus this function gives/prints all the cities that CSAir
    # serves at any time.
    def getAllCities(self, graphNetwork):

        cityList = graphNetwork.nodeList

        for metro in cityList:

            print(metro['NAME'])
