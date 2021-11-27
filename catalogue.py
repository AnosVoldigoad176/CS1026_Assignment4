from country import Country


class CountryCatalogue:
    def __init__(self, countryFile):
        """
        __init__ take the country file and create a dictionary of country objects
        :param countryFile:
        """
        self.countryCat = {}

        try:
            with open(countryFile, 'r') as countryFile:
                # Read first line as header
                header = countryFile.readline()

                # Read rest of file
                for line in countryFile:
                    # Make sure there is no trailing space and then split it by "|"
                    countryListFormat = line.strip().split("|")
                    # Create country object based on the line
                    countryObj = Country(countryListFormat[0], countryListFormat[2], countryListFormat[3],
                                         countryListFormat[1])
                    # Add country object to the dictionary, key will be country name, value will be the country object
                    self.countryCat[countryObj.getName()] = countryObj
        except FileNotFoundError:
            print("File not found")

    def setPopulationOfCountry(self, countryObj, population):
        """
        setPopulationOfCountry take the country object and population you want to set to the country object
        :param countryObj:
        :param population:
        :return: Nothing, just set the population of the country object with updated population of the country
        """
        # Go through the dictionary and find the country object
        for key in self.countryCat.keys():
            if countryObj.getName() == key:
                # Set the population of the country object in dictionary
                self.countryCat[key].setPopulation(population)

    def setAreaOfCountry(self, countryObj, area):
        """
        setAreaOfCountry take the country object and area you want to set to the country object
        :param countryObj:
        :param area:
        :return: Nothing, just set the area of the country object with updated area of the country
        """
        # Go through the dictionary and find the country object
        for key in self.countryCat.keys():
            if countryObj.getName() == key:
                # Set the area of the country object in dictionary
                self.countryCat[key].setArea(area)

    def setContinentOfCountry(self, countryObj, continent):
        """
        setContinentOfCountry take the country object and continent you want to set to the country object
        :param countryObj:
        :param continent:
        :return: Nothing, just set the continent of the country object with updated continent of the country
        """
        # Go through the dictionary and find the country object
        for key in self.countryCat.keys():
            if countryObj.getName() == key:
                # Set the continent of the country object in dictionary
                self.countryCat[key].setContinent(continent)

    def findCountry(self, countryObj):
        """
        findCountry take the country object and find the country object in the dictionary.
        If the country object is found, return the country object otherwise return None
        :param countryObj:
        :return: Country object if found, None if not found
        """
        for key in self.countryCat.keys():
            # Check if the country object is in the dictionary
            if countryObj.getName() == key:
                return self.countryCat[key]
            # Else return None object
            else:
                return None

    def addCountry(self, countryName, countryPopulation, countryArea, countryContinent):
        """
        addCountry take country name, population, area and continent then add to the dictionary if it doesn't exists
        :param countryName:
        :param countryPopulation:
        :param countryArea:
        :param countryContinent:
        :return: True if added, False if not added
        """
        for key in self.countryCat.keys():
            # Check if the country object is in the dictionary
            if countryName == key:
                return False
            # Add new country object if it doesn't exist
            else:
                self.countryCat[countryName] = Country(countryName, countryPopulation, countryArea, countryContinent)
                return True

    def printCountryCatalogue(self):
        """
        printCountryCatalogue print the country dictionary
        :return: Nothing, just print the country dictionary
        """
        # Go through the dictionary and print all country objects
        for key in self.countryCat.keys():
            print(self.countryCat[key])

    def saveCountryCatalogue(self, fileName):
        """
        saveCountryCatalogue save the country dictionary to a file
        :param fileName:
        :return:
        """
        count = 0
        try:
            with open(fileName, 'w') as file:
                # Write header
                file.write("Country|Continent|Population|Area\n")
                # Write the dictionary to file with the header format
                for key in sorted(self.countryCat.keys()):
                    # Increment count for every line
                    count += 1
                    line = self.countryCat[key].getName() + "|" + self.countryCat[key].getContinent() + "|" + \
                        str(self.countryCat[key].getPopulation()) + "|" + str(self.countryCat[key].getArea()) + "\n"
                    file.write(line)
        # If there is any error, return -1
        except Exception as e:
            return -1
        return count

# Test code for CountryCatalogue class
def main():
    countryCat = CountryCatalogue("data3.txt")

    countryCat.addCountry("Pogger", 100, 100, "North America")
    countryCat.printCountryCatalogue()
    countryCat.saveCountryCatalogue("ok.txt")


main()
