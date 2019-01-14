from open_ontologies import open_hpo, open_snomed

# Open the snomed ontology
SNOMED = open_snomed("snomed_terms.tab", "snomed_term_term.tab")
Tree = SNOMED[1].tree
Conditions = SNOMED[0]

# Open the HPO ontology
HPO = open_hpo()

# Look at the condition form the HPO ontology that already have a matching
Matching = {}

Nodes = list(HPO.nodes(data=True))
for conditions in Nodes[0:1000]:
    if 'xref' in conditions[1]:
        for word in conditions[1]['xref']:
            if "SNOMEDCT" in word:
                if word.split('SNOMEDCT_US:')[1] in Conditions.keys():
                    if conditions[0].split('HP:')[1] in Matching:
                        Matching[conditions[0].split('HP:')[1]].append(word.split('SNOMEDCT_US:')[1])
                    else:
                        Matching[conditions[0].split('HP:')[1]] = word.split('SNOMEDCT_US:')[1]





