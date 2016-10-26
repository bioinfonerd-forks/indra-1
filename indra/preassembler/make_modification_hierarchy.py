from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import sys
import csv
from os.path import join, dirname, abspath
from rdflib import Graph, Namespace, Literal

hierarchy_path = join(dirname(abspath(__file__)),
                      '../resources/modification_hierarchy.rdf')

def main():
    indra_ns = 'http://sorger.med.harvard.edu/indra/'
    rn = Namespace(indra_ns + 'relations/')
    en = Namespace(indra_ns + 'entities/')
    g = Graph()

    isa = rn.term('isa')

    g.add((en.term('phosphorylation'), isa, en.term('modification')))
    g.add((en.term('ubiquitination'), isa, en.term('modification')))
    g.add((en.term('sumoylation'), isa, en.term('modification')))
    g.add((en.term('acetylation'), isa, en.term('modification')))
    g.add((en.term('hydroxylation'), isa, en.term('modification')))

    with open(hierarchy_path, 'wb') as out_file:
        g_bytes = g.serialize(format='nt')
        # Replace extra new lines in string and get rid of empty line at end
        g_bytes = g_bytes.replace('\n\n', '\n').strip()
        # Split into rows and sort
        rows = g_bytes.split('\n')
        rows.sort()
        g_bytes = '\n'.join(rows)
        out_file.write(g_bytes)

if __name__ == '__main__':
    main()
