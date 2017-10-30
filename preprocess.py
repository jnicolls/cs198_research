import pandas
import requests, json

regionsFile = "input/table1_list_vista_enchancer_elements.csv"
sequencingDatasetsFile = "input/table2_sequencingDatasets.csv"
encodeParentURL = "https://www.encodeproject.org/"
HEADERS = {'accept': 'application/json'}

def getEncodeURL(urlSnippet):
	return encodeParentURL + urlSnippet + "/?frame=object"

def getJSONResponse(urlSnippet):
	response = requests.get(getEncodeURL(urlSnippet), headers=HEADERS)
	return response.json()

def processEncodeDataset(accession):
	responseExperimentDict = getJSONResponse(accession)
	dataset = responseExperimentDict["dataset"]
	responseDatasetDict = getJSONResponse(dataset)
	origFileDict = getJSONResponse(responseDatasetDict["original_files"][7])

	print json.dumps(origFileDict, indent=4, separators=(',', ': '))

def processSequencingDatasets():
	sequencingDatasets = pandas.read_csv(sequencingDatasetsFile)
	row = next(sequencingDatasets.iterrows())[1]
#	for row in sequencingDatasets.iterrows():
	if row["Accession Type of the Control File(s)"] == "ENCODE": 
		processEncodeDataset(row["Accession"]) 

def main():
	regions = pandas.read_csv(regionsFile)
	processSequencingDatasets()


if __name__ == "__main__":
    main()