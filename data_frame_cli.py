# Author: Rahian Islam
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def print_heading(text):
    """Prints text with heading formatting.
    """
    print('\n{} {} {}\n'.format('*'*3, text, '*'*3) )
    





parser = argparse.ArgumentParser(description="Inspecting csv files with Pandas DataFrame methods.")
parser.add_argument('csv_filename', help='A (nice) csv file.')

parser.add_argument('-t','--head',metavar='', help='Print dataframe head'  )
parser.add_argument('-i','--info',metavar='', help='Print dataframe info')
parser.add_argument('-d','--describe ',metavar='[COLUMN_NAME]', help='Print dataframe statistics. If COLUMN_NAME provided, print statistics of selected column only.')
parser.add_argument('-u','--unique',metavar='[COLUMN_NAME]', help='print unique values of column COLUMN_NAME.')
parser.add_argument('-p','--plot_histogram',metavar='[COLUMN_NAME]', help='Plot histogram of column COLUMN_NAME')
parser.add_argument('-o','--plot_filename',metavar='[FILENAME]', help='Save histogram plot (-p COLUMN_NAME) to file FILENAME')


args = parser.parse_args()

try:
    df = pd.read_csv(args.csv_filename)
except:
    print('There was an error reading {}'.format(args.csv_filename))
    print('Make sure file is present, readable, and formatted as csv.')
    exit()

def print_info(info):
    print('\n{} df.info() {}\n'.format('*'*3, '*'*3) )
    print(df.info())




print_heading('df.shape')
print('{} loaded with shape {}'.format(args.csv_filename, df.shape))

# if args.info == '-i':
#     print_info(args.info)

print_info(args.info)
# print_heading('df.heading')
# print(df.head())
# print_heading('df.info')
# print(df.info())


