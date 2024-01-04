#import numpy as np
import pandas as pd
from utils.file_utils import Get_Source_Root

"""
The location of the English dict in the project
To get the file:
1. Download it from here: https://www.kaggle.com/watts2/glove6b50dtxt
2. Save it to the /resources sub-folder
"""
ENGLISH_DICT_PATH = Get_Source_Root() + "/resources/glove.6B.50d.csv"


def Get_Mapping(file):
    """
    Reads a dict file and returns the 'words' and 'word_to_vec_map'
    :param file: The location of the file
    :return: A tuple of 'words', 'word_to_vec_map'
    """
    #with open(file, 'r', encoding="UTF-8") as f:
    with open(file, 'r', encoding="UTF-8") as f:
        #f = f.dropna()
        #col = f.columns
        words = []
        word_label_text = {}

        for line in f:
            #a = f.iloc[i].name
            #line = a[0]
            line = line.split(";")
            if not line[3] == "":
                curr_word = line[2]
                words.append(curr_word)
                word_label_text[curr_word] = line[5]

    return words, word_label_text

