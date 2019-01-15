import obonet
import networkx
from OntologyTree import OntologyTree


def open_hpo():
    # Read the ontology
    url = 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'
    graph = obonet.read_obo(url)
    # Number of nodes
    print("Number of nodes: %s" %(len(graph)))
    # Number of edges
    print("Number of edges %s" %(graph.number_of_edges()))
    # Check if the ontology is a DAG
    print("Is a DAG: %s" %(networkx.is_directed_acyclic_graph(graph)))
    return graph


def open_snomed(conditions, relations):
    print("Load the conditions")
    snomed = dict()
    myFile = open(conditions, 'r', encoding='utf8', errors='ignore')
    for aRow in myFile:
        line = aRow.split('\t')
        snomed[line[0]] = line[1]
    myFile.close()
    print("Number of conditions %s" % (len(snomed.values())))

    print("Load the ontology tree")
    snomed_terms = []
    myFile = open(relations, "rU")
    for aRow in myFile:
        line = aRow.split('\t')
        snomed_terms.append([line[1], line[3][0:-2]])
    myFile.close()
    Tree = OntologyTree(snomed_terms)
    print("Number of nodes %s" % len(Tree.tree))

    return (snomed, Tree)
