class Country:
    def __init__(self, name, population, area, continent):
        self.name = name
        self.population = population
        self.area = area
        self.continent = continent

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent

    def setPopulation(self, population):
        self.population = population

    def setArea(self, area):
        self.area = area

    def setContinent(self, continent):
        self.continent = continent

    def __repr__(self):
        return "%s (pop: %d, size: %d) in %s" % (self.name, self.population, self.area, self.continent)


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
