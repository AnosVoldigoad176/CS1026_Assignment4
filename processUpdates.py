from country import Country
from catalogue import CountryCatalogue


def processUpdates(countryFileName, updateFileName, badUpdateFile):

    """
    This function take original data file (file 1), update it based on the file containing what to update (file 2)
    and store it into "output.txt". For invalid records, store it to file specified in third param.
    :param countryFileName: Original data file
    :param updateFileName: File containing what to update
    :param badUpdateFile: Store invalid update records
    :return:
    """

    validContinent = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]

    try:
        with open(updateFileName, 'r') as updateFile:
            with open(badUpdateFile, 'w') as badUpdateFile:
                with open(countryFileName, 'r') as countryFile:
                    # Go through the whole file
                    for line in updateFile:
                        # Make sure there is no trailing space and split the line by ";"
                        lineListFormat = line.strip().split(";")
                        # Check if the country name is valid
                        if lineListFormat[0].isupper() and ' ' not in line[0]:
                            countryName = line[0]
                            # Get length of lineListFormat and loop through index
                            for i in range(1, len(lineListFormat)):
                                if lineListFormat[i].startswith("P="):
                                    originalPopulation = lineListFormat[i].strip().replace("P=", '')
                                    newPopulation = originalPopulation.replace(',', '')

                        else:
                            countryNameInvalid = line[0]

    except FileNotFoundError:
        print("File not found")

            
