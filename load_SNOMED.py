from OntologyTree import OntologyTree

SNOMED = dict()

myFile = open("snomed_terms.tab", "rU")
for aRow in myFile:
    line = aRow.split('\t')
    SNOMED[line[0]] = line[1]
myFile.close()

print(len(SNOMED.values()))

SNOMED_terms = []

myFile = open("snomed_term_term.tab", "rU")
for aRow in myFile:
    line = aRow.split('\t')
    SNOMED_terms.append([line[1], line[3][0:-2]])
myFile.close()

Tree = OntologyTree(SNOMED_terms)



