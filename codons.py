def create_codon_dict(file_path):
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()
    codon_mapping = {}
    for row in rows:
        cells = row.strip().split('\t')
        if len(cells) >= 3: # Basic safety check to avoid empty lines
            codon = cells[0]
            amino_acid = cells[2]
            codon_mapping[codon] = amino_acid
    return codon_mapping


