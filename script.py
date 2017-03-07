import sys
from pprint import pprint
from collections import defaultdict

def compute_avg_rating(file):
    ratings = defaultdict(lambda: (0, 0))
    for line in file:
        line = line.lower()
        ignored, name_and_rating = line.split('-')
        name_rating = name_and_rating.split('\t')

        name = name_rating[0]
        rating = int(name_rating[1].strip('\n'))

        old_rating, old_count = ratings[name]
        ratings[name] = (rating+old_rating, old_count+1)

    return ratings

def generate_output(file_1, file_2):
    d1 = compute_avg_rating(file_1)
    d2 = compute_avg_rating(file_2)
    output_d = {}

    for key_1, value_1 in d1.iteritems():
        rating, count = value_1
        avg = float(rating) / count
        output_d[key_1] = (avg, 0)

    for key_2, value_2 in d2.iteritems():
        rating, count = value_2
        avg = float(rating) / count

        if output_d.get(key_2) == None: # restr not in d1
            output_d[key_2] = (0, avg)
        else:
            value_from_one, ignored = output_d[key_2]
            output_d[key_2] = (value_from_one, avg)

    output_csv = ''
    for name, ratings in output_d.iteritems():
        rating_1, rating_2 = ratings

        output_csv += name

        if rating_1 != 0:
            output_csv += ','+ str(rating_1)
        else:
            output_csv += ','

        if rating_2 != 0:
            output_csv += ',' + str(rating_2)
        else:
            output_csv += ','

        output_csv += '\n'

    return output_csv

if __name__ == '__main__':
    # argparse
    file_1 = open(sys.argv[1])
    file_2 = open(sys.argv[2])
    output_file = open(sys.argv[3], 'w')

    csv_string = generate_output(file_1, file_2)
    print csv_string
