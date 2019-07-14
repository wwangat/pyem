#!/usr/bin/env python2.7
# Written by Wei Wang in HKUST
# wwangat@gmail.com

# function: extract principal components from cryoSPARC metafile
# usage: python extract_pca_components.py -f temp.cs -o temp.dat -n 3

import numpy as np
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--input", help=".cs file")
parser.add_option("-o", "--output", help="filename for the output")
parser.add_option("-n", "--numPCs", help="number of PCs to deal with")

(options, args) = parser.parse_args()

meta = np.load(options.input)

output = open(options.output, 'w')
output.write("mrcs_name #1\n")
output.write("image_id #2\n")

for j in range(int(options.numPCs)):
    output.write("PC%d_components #%d\n"%(j, 3+j))

output.write("\n")
for j in range(len(meta['uid'])):
    output.write("%20s %8d" % (meta['blob/path'][j], meta['blob/idx'][j]))
    for k in range(int(options.numPCs)):
        output.write("%16.10f "%(meta['components_mode_%d/value'%(k)][j]))
    output.write('\n')
output.close()
