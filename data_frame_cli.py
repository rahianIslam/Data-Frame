# Author: Yves Pauchard
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def print_heading(text):
    """Prints text with heading formatting.
    """
    print('\n{} {} {}\n'.format('*'*3, text, '*'*3) )

parser = argparse.ArgumentParser(description="Inspecting csv files with Pandas DataFrame methods.")
parser.add_argument('csv_filename', help='A (nice) csv file.')

args = parser.parse_args()

try:
    df = pd.read_csv(args.csv_filename)
except:
    print('There was an error reading {}'.format(args.csv_filename))
    print('Make sure file is present, readable, and formatted as csv.')
    exit()

print_heading('df.shape')
print('{} loaded with shape {}'.format(args.csv_filename, df.shape))
