from os import strerror

filename = input("Enter file name: ")

histogram = {}
try:
    filedata = open(filename, 'rt')
    ch = filedata.read(1)
    while ch != '':
        if not ch.isalpha():
            ch = filedata.read(1)
            continue

        lowerch = ch.lower()
        if lowerch not in histogram:
            histogram.setdefault(lowerch, 1)
        else:
            histogram[lowerch] += 1
            
        ch = filedata.read(1)
    filedata.close()
except Exception as e:
    print("Cannot open file: ", strerror(e.errno))
    exit(e.errno)

sortedhistogram = sorted(histogram.items(), key=lambda x:x[1], reverse=True)

writedata = ""
for key in sortedhistogram:
    writedata += key[0] + " -> " + str(key[1]) + "\n"

try:
    filedata = open(filename + ".hist", 'wt')
    filedata.write(writedata)
    filedata.close()
except Exception as e:
    print("Cannot create file: ", strerror(e.errno))
    exit(e.errno)


