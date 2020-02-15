import argparse
import csv
import itertools
import sys

parser = argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--numeric", help="items are numeric",
                    action="store_true", default=False)
parser.add_argument("support", help="support threshold")
parser.add_argument("-p", "--percentage",
                    action="store_true", default=False,
                    help="treat support threshold as percentage value")
parser.add_argument("filename", help="input filename")
parser.add_argument("-o", "--output", type=str, help="output file")

args = parser.parse_args()
support = args.support

input_file = open(args.filename, 'r')
csv_reader = csv.reader(input_file, delimiter=',')

def APriori(csv_reader,support):

    all_freq = {}
    k = 1
    freqk = APrioriFirstPass(csv_reader,support)
    while ((freqk is not None)and (k<=3)):
        all_freq.update(freqk.items())
        freq = APrioriPass(csv_reader,freqk,k,support)
        freqk = freq
        k = k + 1

    return all_freq

def APrioriPass(csv_reader,freqk,k,support):

    counts = {}
    freq = {}
    counter = 0
    input_file = open(args.filename, 'r')
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        counter = counter + 1
        if (args.numeric == True):
            unique_row_items = set([int(field) for field in row])
        else:
            unique_row_items = set([field.lower().strip() for field in row])
        frequencySet = set()
        for key in freqk.keys():
            for i in key:
               frequencySet.add(i) 
        items_pairs = itertools.combinations(frequencySet,k+1)
        candidates = []
        for pair in items_pairs:
            pair = set(pair)
            candidate = tuple(sorted(pair))
            if candidate not in candidates:
                candidates.append(candidate)
                if ((len(candidate) == k + 1) and (pair <= unique_row_items )):
                    if candidate in counts:
                        counts[candidate] += 1
                    else:
                        counts[candidate] = 1

    for item,count in counts.items():
        if (args.percentage == False):
            if (count >= int(support)):
                freq.update({item:count})
        else:
            s = (int(support)*(counter/100))
            if (count >= int(s)):
                freq.update({item:count})

    return freq

def APrioriFirstPass(csv_reader,support):

    counts = {}
    freq = {}
    counter = 0
    input_file = open(args.filename, 'r')
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        counter = counter + 1
        if (args.numeric == True):
            unique_row_items = set([int(field) for field in row])
        else:
            unique_row_items = set([field.lower().strip() for field in row])
        items = unique_row_items
        for item in items:
            key = (item,)
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1

    for item,count in counts.items():
        if (args.percentage == False):
            if (count >= int(support)):
                freq.update({item:count})
        else:
            s = (int(support)*(counter/100))
            if (count >= int(s)):
                freq.update({item:count})

    return freq       

if (args.output is None):

    le3iko_monwn = APrioriFirstPass(csv_reader,support)
    
    k = 1
    freqk = APrioriFirstPass(csv_reader,support)
    le3iko_diplwn = APrioriPass(csv_reader,freqk,k,support)
    le3iko_triplwn = APrioriPass(csv_reader,freqk,k+1,support)

    csv_writer = csv.writer(sys.stdout, delimiter=';')

    for freqs in sorted(le3iko_monwn):
        row = []
        row.append("{0}:{1}".format(freqs, le3iko_monwn[freqs]))
        csv_writer.writerow(row)

    for freqs in sorted(le3iko_diplwn):
        row = []
        row.append("{0}:{1}".format(freqs, le3iko_diplwn[freqs]))
        csv_writer.writerow(row)

    for freqs in sorted(le3iko_triplwn):
        row = []
        row.append("{0}:{1}".format(freqs, le3iko_triplwn[freqs]))
        csv_writer.writerow(row)

else:

    le3iko_monwn = APrioriFirstPass(csv_reader,support)
    
    k = 1
    freqk = APrioriFirstPass(csv_reader,support)
    le3iko_diplwn = APrioriPass(csv_reader,freqk,k,support)
    le3iko_triplwn = APrioriPass(csv_reader,freqk,k+1,support)
   
    output_file = open(args.output, 'w')
    csv_writer = csv.writer(output_file, delimiter=';')

    for freqs in sorted(le3iko_monwn):
        row = []
        row.append("{0}:{1}".format(freqs, le3iko_monwn[freqs]))
        csv_writer.writerow(row)

    for freqs in sorted(le3iko_diplwn):
        row = []
        row.append("{0}:{1}".format(freqs, le3iko_diplwn[freqs]))
        csv_writer.writerow(row)

    for freqs in sorted(le3iko_triplwn):
        row = []
        row.append("{0}:{1}".format(freqs, le3iko_triplwn[freqs]))
        csv_writer.writerow(row)

