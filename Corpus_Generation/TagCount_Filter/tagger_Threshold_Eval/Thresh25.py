# -*- coding: utf-8 -*-
"""NER_TAGGING_filter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ngfyyhBCaOkk17wjiPMjK6L9VfY3147H

    !pip install spacy

!pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz #just change en_ner_bionlp13cg_md to different ones so we get more tags but not specific to our extraction

"""
import spacy

nlp = spacy.load("en_ner_bc5cdr_md")

#import json

#input_file = '/content/drive/MyDrive/pmidtotext/test_150_hard_coded.jsonl'
folder_path = r"C:\Users\karan\OneDrive - ualberta.ca\Bioin_401\tagger_Threshold_stats\EvalSet"
good_articles_path = 'output25'




    #break # testing for 1
      # for line in tqdm(infile)

def TagText(text): # takes in string
    #add navs tagging here ----------------------------------------------
  text_element = text
  doc = nlp(text)
  offset = 0
  for ent in doc.ents:
    #print(text_element[ent.start_char + offset - 1:ent.start_char + offset])
    if text_element[ent.start_char + offset - 1:ent.start_char + offset] != ">":
        text_element = (text_element[:ent.start_char + offset] + f"<{ent.label_}>" +
                        text_element[ent.start_char + offset:ent.end_char + offset] + f"</{ent.label_}>" +
                        text_element[ent.end_char + offset:])
        offset += (len(ent.label_) * 2) + 5

  return text_element

import os
import shutil
Tag_Threshold = 125 # at minimum the first 1000 words need

# first test: thresh = 125  --> 125/5000 = 2.5% of inital 1000 word text must be tagged-------------------------



def TagCount(text): # takes in string
    #add navs tagging here ----------------------------------------------





  count = 0

  text_element = TagText(text)


  #print(text_element)
  in_tag = False  # Flag to track if we're currently processing a tag
  for char in text_element:
    if char == "<":
      in_tag = True
    elif char == ">":
      in_tag = False
    if in_tag:  # If we just exited a tag, count it
        count += 1





  return count/2 # because 1 word has 2 tags <chemical> word </chemical>






def process_file(filename):

  words_1000 = ""
  word_count = 0
  keep_file = False
  with open(filename, 'r',encoding='latin-1') as f:
      for line in f:
        # Split line into words and iterate through them
        for word in line.split():
          word_count += 1
          words_1000 += word + " "
          if word_count >= 5000:
            break
      #print(f'{word_count}sssssssss')
      #print(words_1000)
      test = TagCount(words_1000)
      if test >= Tag_Threshold and word_count == 5000:
            keep_file = True
      #elif b/c on if less then 5000 words  #shouldnt need it because we get first 1000 words only but just in caser
      elif word_count >= 500 and word_count < 5000: # word count threshold
        if(test/word_count >= 0.025):
          keep_file = True

      if word_count > 0:  # Check if any words were read
        # Check if logic found relevant words
        if keep_file:
          # Delete the file if not keeping it
          new_filename = good_articles_path
          shutil.copy2(filename, new_filename)
          print(f"Copied: {filename} to {good_articles_path}")


# Get the folder path


# Loop through files
for filename in os.listdir(folder_path): # can do tdqm here
  if filename.endswith(".txt"):
    process_file(os.path.join(folder_path, filename))