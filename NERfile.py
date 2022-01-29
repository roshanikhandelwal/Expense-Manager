import spacy
import pandas as pd
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

def InfoSpecifier(filename):
    with open(filename) as f:
        data = f.readlines()


    data = listToString(data)


    array =[]
    matcher = Matcher(nlp.vocab)
    doc=nlp(data)
    pattern1 =[{"ORTH":{"REGEX":"^[1-9]\d[.][0-9][0-9]$"}}]
    pattern2 =[{"ORTH":{"REGEX":"^[1-9]\d\d[.][0-9][0-9]$"}}]
    pattern3 =[{"ORTH":{"REGEX":"^[1-9]\d\d\d[.][0-9][0-9]$"}}]
    pattern4 =[{"ORTH":{"REGEX":"^[1-9]\d\d\d\d[.][0-9][0-9]$"}}]
    pattern5 =[{"ORTH":{"REGEX":"^[1-9]\d\d\d\d\d[.][0-9][0-9]$"}}]
    pattern6 =[{"ORTH":{"REGEX":"^[1-9]\d\d\d\d\d\d[.][0-9][0-9]$"}}]
    pattern7 =[{"ORTH":{"REGEX":"^[1-9]\d\d\d\d\d\d\d[.][0-9][0-9]$"}}]
    pattern8 =[{"ORTH":{"REGEX":"^[1-9]\d\d\d\d\d\d\d\d[.][0-9][0-9]$"}}]

    matcher.add("COST", [pattern1,pattern2,pattern3,pattern4,pattern5,pattern6,pattern7,pattern8])

    matches = matcher(doc)
    #print([t.text for t in doc])
    for match_id, start, end in matches:
        span = doc[start:end]
        array.append(float(span.text))

    matcher2=Matcher(nlp.vocab)
    doc2=nlp(data)
    array2=[]
    pattern11=[{"ORTH":{"REGEX":"^[0-9][0-9][/][0-9][0-9]/[1-2][0-9][0-9][0-9]"}}]
    #pattern12=[{"ORTH":{"REGEX":"^[1-9]\d[.][0-9][0-9][%]$"}}]
    matcher2.add("TAX",[pattern11])
    matches2=matcher2(doc)
    for match_id, start, end in matches2:
        span = doc2[start:end]
        # print(span.text)
        array2.append(span.text)

    # print("Date of bill is {}".format(array2[0]))
    date = array2[0]
    arr =[]
    for X in doc.ents:

            if X.label_ == 'PERCENT':
              a= X.text
            if X.label_ == 'ORG':
              arr.append(X.text)

    # print(max(array))
    total_amount = max(array)
    # print(array2[0],array2[1])
    # print(a)
    # print(arr[0])
    org_name = arr[0]
    return date,total_amount,org_name
