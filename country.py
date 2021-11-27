class Country:
    # Constructor
    def __init__(self, name, population, area, continent):
        """
        Constructor for the Country class.
        :param name: Name of the country object.
        :param population: Population of the country object.
        :param area: Area of the country object.
        :param continent: Continent of the country object.
        """
        self.name = name
        self.population = population
        self.area = area
        self.continent = continent

    # Getters
    def getName(self):
        """
        Getter for the name of the country object.
        :return: Name of the country object.
        """
        return self.name

    def getPopulation(self):
        """
        Getter for the population of the country object.
        :return: Population of the country object.
        """
        return self.population

    def getArea(self):
        """
        Getter for the area of the country object.
        :return: Area of the country object.
        """
        return self.area

    def getContinent(self):
        """
        Getter for the continent of the country object.
        :return: Continent of the country object.
        """
        return self.continent

    # Setters
    def setPopulation(self, population):
        """
        Setter for the population of the country object.
        :param population: Population to set.
        :return: Nothing.
        """
        self.population = population

    def setArea(self, area):
        """
        Setter for the area of the country object.
        :param area: Area to set.
        :return: Nothing.
        """
        self.area = area

    def setContinent(self, continent):
        """
        Setter for the continent of the country object.
        :param continent: Continent to set.
        :return: Nothing.
        """
        self.continent = continent

    # Representation
    def __repr__(self):
        """
        Representation of the country object.
        :return: e.g., Nigeria (pop: 11723456, size: 324935) in Africa
        """
        return "%s (pop: %s, size: %s) in %s" % (self.name, str(self.population).replace(',', ''),
                                                 str(self.area).replace(',', ''), self.continent)

# Test code for Country class
# def main():
#     country = Country("China", 1300000000, 9596961, "Asia")
#     print(country)
#     country.setPopulation(1400000000)
#     country.setArea(888999)
#     country.setContinent("Latin America")
#     print(country)
#
#
# main()
