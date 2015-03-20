__author__ = 'vishrutreddi'


class ConsoleUI:

    def __init__(self):

        # Used to identify which Menu-Screen the User is currently on
        self.currentMenuScreen = 'MainScreen'

    # Used to print the Main Console UI Instructions
    def printMainInstructions(self):

        print('Enter Option:')
        print('1. Get List of all the cities that CSAir Flies to')
        print('2. Get Info About a City')
        print('3. Get Statistical information about CSAir Route Network')
        print('4. Route Network Edit Menu')
        print('5. Save the Route Network')
        print('6. Exit')


    # Used to print the Sub Console UI Instructions
    # These Instructions are details about a particular city
    def printCityInfoInstructions(self):

        print('Enter Option:')
        print('1. Get City Code')
        print('2. Get City Name')
        print('3. Get City Country')
        print('4. Get City Continent')
        print('5. Get City Time-Zone')
        print('6. Get City Population')
        print('7. Get City Region')
        print('8. Get Cities single non-stop flight from City')
        print('9. Back to Previous Menu')
        print('10. Exit')


    # Used to print the Sub Console UI Instructions
    # These Instructions are details about Statistical Data
    def printStatisticalInstructions(self):

        print('Enter Option:')
        print('1. Get Longest Single Flight in the Network')
        print('2. Ge the shortest Single Flight in the network')
        print('3. Get the average distance of all the flights in the network')
        print('4. Get the biggest city (by population) served by CSAir')
        print('5. Get the smallest city (by population) served by CSAir')
        print('6. Get the average size (by population) of all the cities served by CSAir')
        print('7. Get a list of all the continents served by CSAir and the cities within that continent')
        print('8. Get the list of CSAir Hub-Cities')
        print('9. Back to Previous Menu')
        print('10. Exit')


    # Used to print the Sub Console UI Instructions
    # These Instructions are details about Route Network Editing
    def printRouteNetworkEditInstructions(self):

        print('Enter Option:')
        print('1. Remove a City')
        print('2. Remove a Route')
        print('3. Add a City, including all its necessary information')
        print('4. Add a Route, including all its necessary information')
        print('5. Edit an existing City')
        print('6. Back to Previous Menu')
        print('7. Exit')


    # Used to print the Sub Console UI Instructions
    # These Instructions are details about Route Network Editing
    def printCityEditOptions(self):

        print('Enter Option')
        print('1. Edit City Name')
        print('2. Edit City Code')
        print('3. Edit City Country')
        print('4. Edit City Continent')
        print('5. Edit City Time-Zone')
        print('6. Edit City Population')
        print('7. Edit City Region')
        print('8. Edit City Coordinates')
        print('9. Go Back To Previous Menu')
        print('10. Exit')
