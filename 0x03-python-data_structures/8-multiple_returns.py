#!/usr/bin/python3
def num_len(chars):
    count = 0
    for char in chars:
        count += 1
    return count


def multiple_returns(sentence):
    count = num_len(sentence)
    if count == 0:
        return (0, None)
    else:
        return (count, sentence[0])
