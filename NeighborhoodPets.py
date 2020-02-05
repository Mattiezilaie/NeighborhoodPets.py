# Author: Mahtab Zilaie
# Date: January 4 2020
# Description: has a pet library that contains information about the pet name, owner name, species of the
# pet. method option to delete a pet name, method to gt an owner name, method to save the file to a json
# file, method to load new information to json file, and method to get a list of the species.

import json

class NeighborhoodPets:

    """class named Neighborhood Pets methods for adding a pet, deleting a pet, searching for the owner of a pet,
    saving data to a JSON file, loading data from a JSON file, and getting a list of all pet species """

    def __init__(self):

        """ init has a parameter that sets self.pet_lib to a dictionary"""

        self.pet_lib = {}    # sets pet_lib to dictionary

    def add_pet(self, pet_name,species, owner_name):

        """ checks if pet name is not in the dictionary then adds pet name, species, and owner name to dictionary under
        that pet name"""

        if pet_name not in self.pet_lib.keys():   # makes sure pet_name is not in the dictionary
            self.pet_lib[pet_name] = {'Pet name': pet_name, "Species": species, "Owner": owner_name}
            # adds pet name, species, and owner name to dictionary under the key pet name

    def delete_pet(self, pet_name):

        """delete's pet name"""

        if pet_name in self.pet_lib.keys():    # checks to see if pet name is in dictionary
            del self.pet_lib[pet_name]        # deletes the key with pet name and all info attached to pet

    def get_owner(self, pet_name):

        """gets owners name"""

        if pet_name in self.pet_lib.keys():    # checks if pet name is in dictionary
            return self.pet_lib[pet_name]["Owner"]   # returns owner name

    def save_as_json(self, file_name):

        """opens json file and dumps the dictionary information into the file"""

        with open(file_name, 'w') as outfile:
            json.dump(self.pet_lib, outfile)       # opens json file and dumps dictionary into the file

    def read_json(self, file_name):

        """ reads information from json file"""

        with open(file_name) as infile:
            self.pet_lib = json.load(infile)     # opens the dictionary json file

    def get_all_species(self):

        """ returns a list of species in the dictionary"""

        retSpecies = set()         # sets retSpecies to a set which does not allow duplicate values

        for value in self.pet_lib.values():    # iterates through the dictionary values
            retSpecies.add(value["Species"])   # adding values from "Species" category

        return retSpecies
