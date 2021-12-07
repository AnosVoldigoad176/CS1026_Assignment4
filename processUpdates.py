import catalogue
from country import Country
from catalogue import CountryCatalogue
import os.path


def countryValidator(string):
    """
    This function check if the country name is in valid form (no space, in upper case first letter,
    no special characters except for "_" and not space characters)
    :param string: Input string
    :return: True if valid, False if not
    """
    string = string.strip()  # Remove trailing and leading spaces
    if len(string) == 0:  # Check if country is empty
        return False
    if all(c.isalpha() or c == '_' for c in string) and string[0].isupper():  # Valid condition
        return True
    return False


def populationValidator(string):
    """
    This function check if the population or area is in valid form (no space, "," separator)
    :param string: Input string
    :return: True if valid, False if not
    """
    if string.strip().startswith("P="):
        originalp = string.strip().replace("P=", '').replace(' ', '')  # Get original string without spaces
    else:
        return False

    temporary = originalp.replace(',', '')  # Get temporary from original without ","
    temporary = '{:,}'.format(int(temporary))  # Format to comma separated
    if originalp == temporary:  # Check if original and temporary are equal
        return True
    return False


def areaValidator(string):
    """
    This function check if the area is in valid form (no space, "," separator)
    :param string: Input string
    :return: True if valid, False if not
    """
    if string.strip().startswith("A="):
        originala = string.strip().replace("A=", '').replace(' ', '')
    else:
        return False

    temporary = originala.replace(',', '')
    temporary = '{:,}'.format(int(temporary))
    if originala == temporary:
        return True
    return False


def continentValidator(string):
    """
    This function check if the continent name is in valid form
    :param string: Input String
    :return: True if valid, False if not
    """
    validContinent = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]
    if string.strip().startswith("C="):
        continent = string.strip().replace("C=", '')
        if continent in validContinent:
            return True
    return False


def processUpdates(countryFileName, updateFileName, badUpdateFileName):
    """
    This function take original data file (file 1), update it based on the file containing what to update (file 2)
    and store it into "output.txt". For invalid records, store it to file specified in third param.
    :param countryFileName: Original data file
    :param updateFileName: File containing what to update
    :param badUpdateFileName: Store invalid update records
    :return: (True, CatalogName) if successful, (False, None) if not
    """

    # Check if country file exists if no then prompt user to enter file name until it exists
    while not os.path.isfile(countryFileName):
        choice1 = input("Country file doesn't exist. Do you want to quit? (y/n): ")
        if choice1.lower() == "n":
            countryFileName = input("Re-enter file name: ")
        else:
            open("output.txt", "w").write("Update Unsuccessful\n")
            return False, None

    # Check if update file exists if no then prompt user to enter file name until it exists
    while not os.path.isfile(updateFileName):
        choice2 = input("Update file doesn't exist. Do you want to quit? (y/n): ")
        if choice2.lower() == "n":
            updateFileName = input("Re-enter file name: ")
        else:
            open("output.txt", "w").write("Update Unsuccessful\n")
            return False, None

    # Open necessary files
    updateFile = open(updateFileName, "r")
    badUpdateFile = open(badUpdateFileName, "w")

    # Initialize country catalogue
    countryCat = CountryCatalogue(countryFileName)

    population = ""
    area = ""
    continent = ""

    # Process country file using catalogue
    for line in updateFile:
        # Ensure no trailing spaces then split word in line by ";"
        lineListFormat = line.strip().split(";")
        # Check if country is valid (no space, in upper case first letter)
        country = lineListFormat[0].strip()
        if len(lineListFormat) > 4:
            badUpdateFile.write(line)
            continue
        if countryValidator(country):
            # Check if population, area and continent format is valid
            for element in lineListFormat[1:]:
                # If element is population and population is not exists yet
                if element.strip().startswith("P=") and population == "":
                    if populationValidator(element):
                        population = element.replace("P=", "").strip()
                    else:
                        badUpdateFile.write(line)
                        break
                # If element is area and area is not exists yet
                elif element.strip().startswith("A=") and area == "":
                    if areaValidator(element):
                        area = element.replace("A=", "").strip()
                    else:
                        badUpdateFile.write(line)
                        break
                # If element is continent and continent is not exists yet
                elif element.strip().startswith("C=") and continent == "":
                    if continentValidator(element):
                        continent = element.replace("C=", "").strip()
                    else:
                        badUpdateFile.write(line)
                        break
                else:
                    badUpdateFile.write(line)
                    break
            # Create country object
            countryObj = Country(country, population, area, continent)
            print(countryObj)
            # If population is blank then no update to prevent overwrite
            if population != "":
                countryCat.setPopulationOfCountry(countryObj, population)
                population = ""
            # If area is blank then no update to prevent overwrite
            if area != "":
                countryCat.setAreaOfCountry(countryObj, area)
                area = ""
            # If continent is blank then no update to prevent overwrite
            if continent != "":
                countryCat.setContinentOfCountry(countryObj, continent)
                continent = ""
        # Country not valid
        else:
            badUpdateFile.write(line)
            continue

    # Output file for successful updates
    countryCat.saveCountryCatalogue("output.txt")
    badUpdateFile.close()
    updateFile.close()
    return True, countryCat

