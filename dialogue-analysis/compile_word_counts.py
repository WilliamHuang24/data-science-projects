import argparse
import json
import csv
import string


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
parser.add_argument('-d', '--dialog')

args = parser.parse_args()

counts = {}

with open(args.dialog) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        name = row[2]
        word_count = None

        if name not in counts.keys():
            counts[name] = {}
            word_count = counts[name]
        else:
            word_count = counts[name]

        sentence = row[3]

        for c in "{}[],.-?!:;#&":
            sentence.replace(c, '')
            
        for w in sentence.split(' '):
            if w not in word_count.keys():
                word_count[w] = 1
            else:
                word_count[w] = word_count[w] + 1

    

    with open(args.output, 'w') as f:
        json.dump(counts, f)

