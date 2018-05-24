# We have so many tags and want to reduce tags
# Before running this code, create move all files from old_tags to temp_tag.
# This code replaces one class at a time. Cut from new_tags and paste it to temp_tag before replacing another tag.
# Finally delete temp.
# Location: {'Source': 167, 'Neutral': 4971, 'Accused': 431, 'Victim': 165, 'Event': 3781, 'Assoc_Event': 331}

# Person: {'Comment': 1818, 'Assoc_Victim': 19,'Accused': 1178, 'Victim':513, 'Others': 2066, 'Assoc_Accused': 199}

# Organization: {'Assoc_Victim': 16, 'Accused': 1382, 'Assoc_Accused': 93, 'Victim': 108, 'Others': 3991}

# Covert LOC:{Source, Neutral, Assoc_Event} -> Others so final classes will be [Accused, Victim, Event and Others]
# Covert PERSON: {Comment, Assoc_Victim, Assoc_Accused} -> Others so final classes will be [Accused, Victim and Others]
# Covert Organization: {Assoc_Victim, Assoc_Accused} -> Others so final classes will be [Accused, Victim and Others]

import os

old_tag_dir = '../../Dataset/tagsequence_dataset/temp_tag'
new_tag_dir = '../../Dataset/tagsequence_dataset/new_tags'


for f in os.listdir(old_tag_dir):
	filepath = os.path.join(old_tag_dir, f)
	newfilepath = os.path.join(new_tag_dir, f)
	with open(filepath, "rt") as fin:
    		with open(newfilepath, "wt") as fout:
        		for line in fin:
            			fout.write(line.replace('ORG_Assoc_Victim', 'ORG_Others'))



