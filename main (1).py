def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content

def write_data(file_name, data):
    f = open(file_name, "w")
    l = data.split()
    a = (l[0].split(','))
    f.write("[\n")
    for i in range(len(l) - 1):
        b = (l[i + 1].split(','))
        f.write("\t{\n")
        for m in range(len(l)):
            if m == 1:
                f.write('\t\t"' + a[m] + '": '+'"' + b[m] + '",\n')
            elif m == 3:
                f.write('\t\t"' + a[m] + '": '+ b[m]+"\n")
            else:
                f.write('\t\t"' + a[m] + '": '+ b[m] + ',\n')
        if i == (len(l) - 2):
            f.write("\t}\n")
        else:
            f.write("\t},\n")
    f.write("]\n")
    f.close()
write_data('Task2.json', read_data('Task.csv'))
