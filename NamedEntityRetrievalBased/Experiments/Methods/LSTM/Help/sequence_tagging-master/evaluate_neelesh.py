from model.data_utils import CoNLLDataset
from model.ner_model import NERModel
from model.config import Config
import os

config = Config()
model = NERModel(config)
model.build()
model.restore_session(config.dir_model)

sentence = "Staff Reporter Terror suspect is the prime accused in Kozhikode twin-blast case Nazir to be taken to blast sites today NIA has secured custody of Nazir for 10 days KOZHIKODE"
words_raw = sentence.strip().split(" ")
preds = model.predict(words_raw)
print (preds)

# Test
relevant_tag_count = dict() # TP + FN
relevant_retrieved_tag_count = dict() # TP
retrieved_tag_count = dict() # TP + FP

relevant_tag_count['PER_Others'] = 0
relevant_retrieved_tag_count['PER_Others'] = 0
retrieved_tag_count['PER_Others'] = 0

relevant_tag_count['PER_Victim'] = 0
relevant_retrieved_tag_count['PER_Victim'] = 0
retrieved_tag_count['PER_Victim'] = 0

relevant_tag_count['PER_Accused'] = 0
relevant_retrieved_tag_count['PER_Accused'] = 0
retrieved_tag_count['PER_Accused'] = 0

relevant_tag_count['ORG_Victim'] = 0
relevant_retrieved_tag_count['ORG_Victim'] = 0
retrieved_tag_count['ORG_Victim'] = 0

relevant_tag_count['ORG_Accused'] = 0
relevant_retrieved_tag_count['ORG_Accused'] = 0
retrieved_tag_count['ORG_Accused'] = 0

relevant_tag_count['ORG_Others'] = 0
relevant_retrieved_tag_count['ORG_Others'] = 0
retrieved_tag_count['ORG_Others'] = 0

relevant_tag_count['LOC_Accused'] = 0
relevant_retrieved_tag_count['LOC_Accused'] = 0
retrieved_tag_count['LOC_Accused'] = 0

relevant_tag_count['LOC_Others'] = 0
relevant_retrieved_tag_count['LOC_Others'] = 0
retrieved_tag_count['LOC_Others'] = 0

relevant_tag_count['LOC_Event'] = 0
relevant_retrieved_tag_count['LOC_Event'] = 0
retrieved_tag_count['LOC_Event'] = 0

relevant_tag_count['LOC_Victim'] = 0
relevant_retrieved_tag_count['LOC_Victim'] = 0
retrieved_tag_count['LOC_Victim'] = 0

test_file_path = 'data/test.txt'

with open(test_file_path, "rt") as test_file:
    words = []
    actual_tags = []
    for line in test_file:
        if line != '\n':
            tokens = line.split()
            words.append(tokens[0])
            actual_tags.append(tokens[1])
        else:
            # We have read one sentence
            predicted_tags = model.predict(words)
            result_len = min(len(predicted_tags), len(actual_tags))
            for i in range(result_len):
                if actual_tags[i] in relevant_tag_count.keys():
                    relevant_tag_count[actual_tags[i]] = relevant_tag_count[actual_tags[i]] + 1
                if predicted_tags[i] in retrieved_tag_count.keys():
                    retrieved_tag_count[predicted_tags[i]] = retrieved_tag_count[predicted_tags[i]] + 1
                if actual_tags[i] == predicted_tags[i]:
                    if actual_tags[i] in relevant_retrieved_tag_count.keys():
                        relevant_retrieved_tag_count[actual_tags[i]] = relevant_retrieved_tag_count[actual_tags[i]] + 1
            # One sentence finished. Reinitialize
            words = []
            actual_tags = []

avg_precision = 0
avg_recall = 0

print('======= Precision Class Wise =====================\n')

print('Class    Precision %')
print('--------------------------')

count_keys = 0
for key in retrieved_tag_count.keys():
    if key[4:]!='Others':
        count_keys = count_keys + 1
        if retrieved_tag_count[key] != 0:
            prec = float(relevant_retrieved_tag_count[key])/retrieved_tag_count[key]
            print(key, prec)
            avg_precision = avg_precision + prec
        else:
            print(key, 0.0)
        
        recall = float(relevant_retrieved_tag_count[key])/relevant_tag_count[key]
        avg_recall = avg_recall + recall
        
print('\n======= Avergae Precision =====================\n')
print('Average Precision: ',avg_precision/count_keys)

avg_f1 = (2*avg_precision*avg_recall)/(avg_precision + avg_recall)/count_keys
print('Average Recall: ',avg_recall/count_keys)
print('Average f1: ',avg_f1)
