#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence_tuple = (len(sentence), None)
        return sentence_tuple
    sentence_tuple = (len(sentence), sentence[0])
    return sentence_tuple
