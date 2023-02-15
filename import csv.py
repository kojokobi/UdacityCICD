import csv
import pandas as pd

# read contents of a file
def read_textTxtFile():
    with open('./file-to-read.txt') as f:
        lines = f.readlines()
        for x in lines:
            print(x)

# read contents of a csv file
def read_csvFile():
    try:
        with open('sample-test-cases.csv','r') as f:
            reader = csv.reader(f)
            for line in reader:
                # get contents of testCase file 
                print(line)
    except:
        print("An error occured while reading file contents")


def read_excel_file():
    # Display contents of excel file
    xlContents = pd.read_excel("./testCaseGenSample.xlsx") #TODO excel filename should be read from a config file
    print(xlContents)


def main():
    # read_textTxtFile()
    read_excel_file()
    




if __name__ == "__main__":
    main()
    