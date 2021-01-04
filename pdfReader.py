#! python3
# Convert from PDF to csv

import tabula
tabula.convert_into("invoice-english2.pdf","invoice-english2.csv",lattice=True,output_format="csv",pages='all')
tabula.convert_into("invoice-standard1.pdf","invoice-standard1.csv",lattice=True,output_format="csv",pages='all')

# import glob
# invoice = glob.glob('invoice/*.pdf')