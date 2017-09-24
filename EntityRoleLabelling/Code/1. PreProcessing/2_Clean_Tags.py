## Tags are not used propely. Like soome places 'Accused' used and some places 'Accused Location'. Making all the same. 
# This code filters the file having bad tags and places them in bad diirectory

import os
import json
import numpy as np
import traceback
from shutil import copyfile


#Path to dataset directory
dataset_dir = '../../Dataset/tagged_dataset'
bad_file_dir = '../../Dataset/bad'

# Json doc keys for location, person and organization

#Location Structure ENTITY_TYPE:[...., ["Word_Sequence, Position of first word of word_sequence in content, Role"], .....]
#Eample: "LOC" : [ [ "New Delhi", "1",  "Neutral" ], ...]

LOCATION_KEY = 'LOC'
PERSON_KEY = 'PER'
ORGANIZATION_KEY = 'ORG'
CONTENT_KEY = 'content'

loc_tags = dict()
per_tags = dict()
org_tags = dict()


try:
    # Read all the json files and create txt file and tag sequence file
    fileProcessed = 0;
    for f in os.listdir(dataset_dir):
        fileProcessed = fileProcessed + 1
        #print('Processing file# '+str(fileProcessed))
        # Only jsn file
        if f.endswith('.jsn'):
            filepath = os.path.join(dataset_dir, f)
	    bad_file_path = os.path.join(bad_file_dir, f)
            #print(filepath)
            with open(filepath) as jsonfile:
                data = json.load(jsonfile)

                location_list = data[LOCATION_KEY]
                for loc in location_list:
                    if loc[2] == 'Victim Location':
			print(filepath)
			copyfile(filepath, bad_file_path)
			break;

            # Get all persons
                person_list = data[PERSON_KEY]
                for person in person_list:
                    if person[2] == 'Assoc Accused':
                       	print(filepath)
			copyfile(filepath, bad_file_path)
			break;


            # Get all Organizations
                org_list = data[ORGANIZATION_KEY]
                for org in org_list:
                    if org[2] == 'Assoc Accused':
                        print(filepath)
			copyfile(filepath, bad_file_path)
			break;

    #print(loc_tags)
    #print(per_tags)
    #print(org_tags)
except:
    traceback.print_exc()
