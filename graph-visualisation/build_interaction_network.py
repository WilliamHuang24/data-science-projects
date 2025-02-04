import csv
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')

args = parser.parse_args()

speaks = {}

with open(args.input, 'r') as input_csv:
    reader = csv.reader(input_csv)
    
    prev_pony = None

    for row in reader:
        skip = False

        for el in ['others', 'ponies', 'and', 'all']:
            if el in row[2].split(' '):
                prev_pony = None
                skip = True
                break
        
        if skip:
            continue
        
        cur_pony = row[2].lower()

        if prev_pony is not None and prev_pony != cur_pony:
            if prev_pony in speaks.keys():
                sub_dict = speaks[prev_pony]

                if cur_pony in sub_dict.keys():
                    sub_dict[cur_pony] += 1
                else:
                    sub_dict[cur_pony] = 1

            else:
                speaks[prev_pony] = {}
                speaks[prev_pony][cur_pony] = 1
        
        prev_pony = cur_pony
    
    with open(args.output, 'w') as output_file:
        json.dump(speaks, output_file)