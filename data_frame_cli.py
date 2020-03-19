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
#this adds the head printing argument with the help  of action argument. When its given store_true it doesnt want any other argument
parser.add_argument('-t','--head', help='Print dataframe head',action = 'store_true' )

#This prints all the info of the dataframe
parser.add_argument('-i','--info', help='Print dataframe info', action = 'store_true')

#This will describe the whole dataframe or the specific column
#metavar s used to name the second argument meaning the column name 
#nargs is number of arguments allowed and the qeustion mark allows to give as many arguments as i want
parser.add_argument('-d','--describe',metavar='COLUMN_NAME',nargs ='?', help='Print dataframe statistics. If COLUMN_NAME provided, print statistics of selected column only.')

parser.add_argument('-u','--unique', metavar='COLUMN_NAME', help='print unique values of column COLUMN_NAME.')
parser.add_argument('-p','--plot_histogram',metavar='COLUMN_NAME',  help='Plot histogram of column COLUMN_NAME')
parser.add_argument('-o','--plot_filename',metavar='FILENAME', help='Save histogram plot (-p COLUMN_NAME) to file FILENAME')


args = parser.parse_args()

try:
    df = pd.read_csv(args.csv_filename)
except:
    print('There was an error reading {}'.format(args.csv_filename))
    print('Make sure file is present, readable, and formatted as csv.')
    exit()

def print_info(info):
    """This is a function to print the info  """
    print('\n{} df.info() {}\n'.format('*'*3, '*'*3) )
    print(df.info())

def print_head(head):
    """This is a function to print the info """
    print('\n{} df.head() {}\n'.format('*'*3, '*'*3) )
    print(df.head())



print_heading('df.shape')
print('{} loaded with shape {}'.format(args.csv_filename, df.shape))

#this is the if statmebt for the differernt arguments provided from the interface

if args.info:
    print_info(args.info)

elif args.head:
    print_head(args.head)

elif args.describe:
    print('\n{} df[{}].describe {}\n'.format('*'*3, args.describe, '*'*3) )
    print('\n{}\n'.format(df[args.describe].describe()) )

elif args.unique or args.plot_histogram or args.plot_filename :
    print('**********Not done yet**********')    
else:
    print('\n{} df.describe() {}\n'.format('*'*3, '*'*3) )
    print(df.describe())

    


    