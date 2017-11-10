import pandas

from pybedtools import BedTool
from sklearn import linear_model

SENTINEL = -1

regionsFile = "input/table1_list_vista_enchancer_elements.csv"
#sequencingDatasetsFile = "input/table2_sequencingDatasets.csv"
#encodeParentURL = "https://www.encodeproject.org/"
#HEADERS = {'accept': 'application/json'}

#def getEncodeURL(urlSnippet):
#	return encodeParentURL + urlSnippet + "/?frame=object"

#def getEncodeJSONResponse(urlSnippet):
#	response = requests.get(getEncodeURL(urlSnippet), headers=HEADERS)
#	return response.json()

#def processEncodeDataset(accession):
#	responseExperimentDict = getEncodeJSONResponse(accession)	
#	dataset = responseExperimentDict["dataset"]
#	responseDatasetDict = getEncodeJSONResponse(dataset)
#
#	bedFilepath = SENTINEL
#
#	for encodeFile in responseDatasetDict["original_files"]:
#		encodeFileDict = getEncodeJSONResponse(encodeFile)
#		if "file_type" in encodeFileDict.keys() and "output_type" in encodeFileDict.keys():
#			if encodeFileDict["file_type"] == "bed narrowPeak" and encodeFileDict["output_type"] == "replicated peaks":
#				bedFilepath = encodeFileDict["href"]
#				break
#
#	if bedFilepath == SENTINEL:
#		raise ValueError("dataset " + dataset + " had no valid file for accession value " + accession)
#
#	bedFile = requests.get(getEncodeURL(bedFilepath))
#	bedFileContent = BedTool(bedFile)
#
#
#	print(len(bedFileContent))


def processSequencingDatasets():
	sequencingDatasets = pandas.read_csv(sequencingDatasetsFile)
#	row = next(sequencingDatasets.iterrows())[1]
#	for row in sequencingDatasets.iterrows():
#	if row["Accession Type of the Control File(s)"] == "ENCODE": 
#		processEncodeDataset(row["Accession"]) 

def main():
	regions = pandas.read_csv(regionsFile)
	processSequencingDatasets()


if __name__ == "__main__":
    main()