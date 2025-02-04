import argparse
import json
import math
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--input')
parser.add_argument('-n', '--num')

args = parser.parse_args()

output = {}

with open(args.input, 'r') as f:
    input_json = json.load(f)

    total_ponies = len(input_json.keys())
    words = []

    for k in input_json.keys():
        words = words + list(input_json[k].keys())

    num_words = len(set(words))

    tf_idf = {}

    for k in input_json.keys():
        tf_idf[k] = {}

    for word in set(words):
        if word == '':
            continue

        num_ponies = 0

        for pony in input_json.keys():
            d = input_json[pony]

            if word in d.keys():
                num_ponies += 1


        for pony in input_json.keys():
            d = input_json[pony]

            if word in d:
                tf = input_json[pony][word]
                idf = math.log(len(input_json.keys()) / num_ponies)
                tf_idf[pony][word] = tf * idf



    res = {}
    n = int(args.num)

    print(f'we want the top {n} strings')

    for pony in tf_idf:
       res[pony] = sorted(tf_idf[pony], key=tf_idf[pony].get, reverse=True)[0:n]
    
    print(json.dumps(res))




