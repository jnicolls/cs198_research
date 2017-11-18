import pandas
import os

from pybedtools import BedTool
from sklearn import linear_model

SENTINEL = -1

regionsFile = "input/table1_list_vista_enchancer_elements.csv"
dataPath = "input/rawData/filteredBedGraph/"
inputPath = "all_merged"
trainingIndex = 9
chrIndex = 0
startIndex = 1
endIndex = 2
labelIndex = 8


def processSequencingDatasets():
    sequencingDatasets = pandas.read_csv(sequencingDatasetsFile)

def readData(trainingData):
    for filename in os.listdir(dataPath):

        inputdata = pandas.read_table(dataPath + filename + inputPath)
        inputdatarows = inputdata.iterrows()
        inputrow = next(inputdata.iterrows())

        for index, row in trainingData.iterrows():
            while inputrow[startIndex] > row[endIndex]:
                inputrow = next(inputdatarows)
            rpm = 0.0
            k = (row[endIndex] - row[startIndex])/1000
            while inputrow[endIndex] < row[endIndex]:
                rpm += inputrow[3]
                inputrow = next(inputdatarows)
            rpkm = rpm/1000
            row['rpkms'] += rpkms
            row['totals'] += totals

    for index, row in trainingData:
        row['rpkms'] /= row['totals'] 

    return trainingData





def main():
    regions = pandas.read_csv(regionsFile)
    chrs, starts, ends, rpkms, totals, label = []
        for index, row in regions.iterrows():
            if row[trainingIndex] == "yes":
      #          chrs.append(row[chrIndex])
                starts.append(row[startIndex])
                ends.append(row[endIndex])
                labels.append(row[labelIndex])
    for i in range(0, len(starts)):
        rpkms.append(0.0)
        totals.append(0)
    d = {'starts': starts, 'ends':ends, 'rpkms':rpkms, 'totals':totals}
    trainingData = pandas.df(data=d)
    trainingData = readData(trainingData)





if __name__ == "__main__":
    main()