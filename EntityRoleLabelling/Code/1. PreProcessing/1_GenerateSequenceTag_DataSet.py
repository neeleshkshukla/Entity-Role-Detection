import os
import json
import numpy as np
import traceback


#Path to dataset directory
dataset_dir = '../../Dataset/tagged_dataset'
dataset_content_dir = '../../Dataset/tagsequence_dataset/content'
dataset_tag_dir = '../../Dataset/tagsequence_dataset/tag'

# Create output directory
if not os.path.exists(dataset_content_dir):
	os.makedirs(dataset_content_dir)

if not os.path.exists(dataset_tag_dir):
	os.makedirs(dataset_tag_dir)

# Json doc keys for location, person and organization

#Location Structure ENTITY_TYPE:[...., ["Word_Sequence, Position of first word of word_sequence in content, Role"], .....]
#Eample: "LOC" : [ [ "New Delhi", "1",  "Neutral" ], ...]

LOCATION_KEY = 'LOC'
PERSON_KEY = 'PER'
ORGANIZATION_KEY = 'ORG'
CONTENT_KEY = 'content'

try:
    # Read all the json files and create txt file and tag sequence file
    fileProcessed = 0;
    for f in os.listdir(dataset_dir):
        fileProcessed = fileProcessed + 1
        print('Processing file# '+str(fileProcessed))
        # Only jsn file
        if f.endswith('.jsn'):
            filepath = os.path.join(dataset_dir, f)
            print(filepath)
            with open(filepath) as jsonfile:
                data = json.load(jsonfile)
                content_file_write_path = os.path.join(dataset_content_dir, os.path.splitext(f)[0]+'.txt')
                tag_file_write_path = os.path.join(dataset_tag_dir, os.path.splitext(f)[0] + '.txt')
                content_file = open(content_file_write_path, 'w')
                tag_file = open(tag_file_write_path, 'w')
                content = data[CONTENT_KEY]
                content_file.write(content)
                content_file.close()

            # Start building tah sequence
            # Get the number of words in content. All the words are seperated by space
                content_arr = content.split(' ')

            # Create array to keep track of words which has been tgagged
                status_arr = np.zeros((len(content_arr),), dtype=np.int)
            #Get all the Locations
                location_list = data[LOCATION_KEY]
                for loc in location_list:
                    for i in xrange(len(loc[0].split(' '))):
                        content_arr[int(loc[1])-1+i] = LOCATION_KEY+'_'+loc[2]
                        status_arr[int(loc[1])-1+i]=1

            # Get all persons
                person_list = data[PERSON_KEY]
                for person in person_list:
                    for i in xrange(len(person[0].split(' '))):
                        content_arr[int(person[1]) - 1 + i] = PERSON_KEY + '_' + person[2]
                        status_arr[int(person[1]) - 1 + i]=1

            # Get all Organizations
                org_list = data[ORGANIZATION_KEY]
                for org in org_list:
                    for i in xrange(len(org[0].split(' '))):
                        content_arr[int(org[1]) - 1 + i] = ORGANIZATION_KEY + '_' + org[2]
                        status_arr[int(org[1]) - 1 + i]=1

                tag_text = ''
                for i in range(len(content_arr)):
                    if status_arr[i] == 0:
                        content_arr[i] = 'O'
                    tag_text = tag_text+content_arr[i]+' '
            #print(content_arr)
            #print(tag_text)
                tag_file.write(tag_text)
                tag_file.close()
except:
    traceback.print_exc()
