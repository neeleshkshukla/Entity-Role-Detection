import os
import json
import numpy as np
import traceback


#Path to dataset directory
dataset_dir = '../../Dataset/tagged_dataset'

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
            #print(filepath)
            with open(filepath) as jsonfile:
                data = json.load(jsonfile)

                location_list = data[LOCATION_KEY]
                for loc in location_list:
                    if loc[2] not in loc_tags:
                        loc_tags[loc[2]] = 1
                    else:
                        loc_tags[loc[2]] = loc_tags[loc[2]] + 1

            # Get all persons
                person_list = data[PERSON_KEY]
                for person in person_list:
                    if person[2] not in per_tags:
                        per_tags[person[2]] = 1
                    else:
                        per_tags[person[2]] = per_tags[person[2]] + 1


            # Get all Organizations
                org_list = data[ORGANIZATION_KEY]
                for org in org_list:
                    if org[2] not in org_tags:
                        org_tags[org[2]] = 1
                    else:
                        org_tags[org[2]] = org_tags[org[2]] + 1

    print(loc_tags)
    print(per_tags)
    print(org_tags)
except:
    traceback.print_exc()
