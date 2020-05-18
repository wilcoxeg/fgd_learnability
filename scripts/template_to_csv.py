import json
import pandas as pd
import pprint
import collections
from os import listdir
import numpy as np
import sys


def jsonify_template(to_jsonify, dir_path):
  
  total_sents = []
  total_by_word = []

  for suite in to_jsonify:
      print("JSONifying: " + suite)
      
      suite_path = dir_path + suite
      df = pd.read_csv(suite_path, comment = "#")

      by_word_result = []
      by_sentence_result = []
      test = suite.split(".")[0]
              
      for index, row in df.iterrows():
        item = row["item"]
        condition = row["condition"]

        sent = []
        for name, region in row[2:].items():
          if type(region) == str:
            words = region.split(" ")
            for w in words:
              sent.append(w)
              by_word_result.append([test, item, condition, name, w])
        by_sentence_result.append( " ".join(sent + ["."]))

      total_sents.extend(by_sentence_result)
      total_by_word.extend(by_word_result)

      with open(dir_path+"test_sents.txt", "w") as outf:
        outf.write("\n".join([x for x in total_sents]))

      outdf = pd.DataFrame(total_by_word)
      outdf.to_csv(dir_path+"test_items", index=False)


def main(dir_path):
  to_jsonify = sorted([x for x in listdir(dir_path) if ( (not x.startswith(".")) & (x.endswith(".csv")))])
  jsonify_template(to_jsonify, dir_path)


if __name__ == '__main__':
  main(sys.argv[1])




