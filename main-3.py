def new_file(file):
    opening = open(file, 'r')
    rd = opening.read()
    return rd


def titling(records):
    splt = records.split('\n')
    title, dfn = "", ""

    for i in splt:
        if i.startswith('# title'):
            title = i.lstrip('# title')
        elif i.startswith('# description'):
            dfn = i.lstrip('# description')

    return title, dfn


def editing(title, dfn, code):
    dir = '-'.join(title.lower().split())
    symb = '+ [{}](#{})\n\n## {}\n\n{}\n\n```python\n{}\n```'

    return symb.format(title, dir, title, dfn, code)


def converting(records):
    records = rd.split(dlm)
    titles, code = records[0], records[1]
    title, dfn = titling(titles)
    res = editing(title, dfn, code.lstrip())
    return res


def adding(records):
    f = open('out.txt', "w+")
    f.write(records)
    f.close()
    return f


rd = new_file('solution.txt')
markdowns = converting(rd)
print(adding(markdowns))