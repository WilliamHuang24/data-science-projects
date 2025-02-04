import argparse
import json
import random

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--out_file')
parser.add_argument('json_filename')
parser.add_argument('num_posts')

args = parser.parse_args()


with open(args.json_filename) as input_json:
    data = json.load(input_json)

    output_tsv = open(args.out_file, 'wb')
    total_posts = data['data']['dist']
    indices = []

    #include all posts if number of requested posts is greater than the number given
    if int(args.num_posts) > total_posts:
        indices = range(total_posts)
    else:
        indices = random.sample(range(total_posts), args.num_posts)

    posts = data['data']['children']
    output_tsv.write('Name\ttitle\tcoding\n'.encode('utf-8'))

    for i in indices:
        post = posts[i]['data']
        row = post['name'] + '\t' + post['title'] + '\n'
        #print(row)
        output_tsv.write(row.encode('utf-8'))

    output_tsv.close()
