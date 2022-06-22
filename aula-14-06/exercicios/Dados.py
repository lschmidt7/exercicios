import csv

def load(filename, header_types, as_dict = False):
    f = open(filename, encoding='utf-8')
    content = csv.reader(f, delimiter=',')
    content = list(content)
    header, data = convert(content, header_types, as_dict)
    return header, data

def convert(content, types, as_dict):
    header = content[0]
    for line_idx, line in enumerate(content[1:]):
        dicionario = {}
        for typ_idx, typ in enumerate(types):
            field = header[typ_idx]
            dicionario[field] = typ(line[typ_idx])
            content[line_idx + 1] = dicionario
    return header, content[1:]