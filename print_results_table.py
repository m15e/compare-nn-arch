#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Mark Rode
# DATE CREATED: October 11 2018                          
# REVISED DATE: 
# PURPOSE: Prints dataset information and model comparison data to the screen
#
##
# 
from os import listdir
import numpy as np
import pandas as pd

# Create dictionary that contains models and final results and prints results
model_comp_dic = {}
for file in listdir('.'):
        if file.endswith("pet-images.txt"):
            with open(file) as f:
                for line in f:
                        if 'arch' in line:
                            key = line.replace('arch = ','').strip().title()
                            model_comp_dic.update({ key: [ line.replace('\n','').split(': ')[1] for line in f if 'Number' in line or '%' in line ] })

# Print dictionary 
# {'resnet': [['Number of Images', '40'], ['Number of Dog Images', '30'], ['Number of "Not-a" Dog Images', '10'], ['% Correct Dogs','100.0'], ['% Correct Notdogs', '90.0'], ['% Correct Breed', '90.0'], ['% Match', '0']], 'alexnet': [['Number of Images', '40'], ['Number of Dog Images', '30'], ['Number of "Not-a" Dog Images', '10'], ['% Correct Dogs', '100.0'], ['% Correct Notdogs', '100.0'],['% Correct Breed', '80.0'], ['% Match', '0']], 'vgg': [['Number of Images', '40'], ['Number of Dog Images', '30'], ['Number of "Not-a" Dog Images', '10'], ['% Correct Dogs', '100.0'], ['% Correct Notdogs', '100.0'], ['% Correct Breed', '93.33333333333333'], ['% Match', '0']]}
# for model, results in model_comp_dic.items():
#     print('\n'+model.title()+'\n'+'-'*25)
#     for i in range(len(results)):
#         if '%' in results[i][0]:
#             print(results[i][0] + ': ' + results[i][1])

df = pd.DataFrame.from_dict(model_comp_dic,orient='index')
df.columns = [ '# Images','# Dog Images','# "Not-a" Dog Images','% Correct Dogs','% Correct Notdogs','% Correct Breed','% Match Labels' ]
results_df = df.iloc[:,-4:]
print('\nDataset Information:\n'+'-'*27+'\n'+df.iloc[:,:3].to_string()+'\n')
print('\nModel Performace Comparison:\n'+'-'*27+'\n'+results_df.to_string()+'\n')