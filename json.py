import json 

import glob

# find all notebooks 
all_notebooks = glob.glob('**/*.ipynb', recursive=True)

# iterate over all notebooks
for nb in all_notebooks:

    with open(nb) as f: 
        data = json.load(f)

    student_version = []
    for cell in data['cells']:
        if 'tags' in cell['metadata']:
            if 'solution' not in cell['metadata']['tags']:
                student_version.append(cell)
        else:
            student_version.append(cell)

    data['cells'] = student_version

    with open(nb, 'w') as outfile:
        json.dump(data, outfile)