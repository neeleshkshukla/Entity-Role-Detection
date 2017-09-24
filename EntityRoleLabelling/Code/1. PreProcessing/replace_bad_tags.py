## Tags are not used propely. Like soome places 'Accused' used and some places 'Accused Location'. Making all the same. 
# This code repalces the bad tags with correct tag like 'Accused Location' to 'Accused'

import os

bad_file_dir = '../../Dataset/bad'
clean_file_dir = '../../Dataset/clean'


for f in os.listdir(bad_file_dir):
	filepath = os.path.join(bad_file_dir, f)
	cleanfilepath = os.path.join(clean_file_dir, f)
	with open(filepath, "rt") as fin:
    		with open(cleanfilepath, "wt") as fout:
        		for line in fin:
            			fout.write(line.replace('Assoc Accused', 'Assoc_Accused'))



