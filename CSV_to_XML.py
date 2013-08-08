__author__ = 'William'
import csv
import sys

xmloutput = ""
root = ""
element = ""
attributes = []
opentag = '<'
closetag = '>'


def loadFile(filename):
    file = open(filename)
    try:
        reader = csv.reader(file)
        extractHeadings(reader)
    finally:
        file.close()


def extractHeadings(reader):
    global root, element, attributes
    select = reader.next()
    root = select[0]
    element = select[1]
    select = reader.next()
    attributes = select
    buildxml(reader)


def buildxml(reader):
    global xmloutput

    xmloutput += '\n' + opentag + root + closetag  #<root>
    xmloutput += '\n' + '\t' + opentag + element + closetag  #<element>
    #<attributes>
    xmloutput += '\n' + '\t' + opentag + '/' + element + closetag  #</element>
    xmloutput += '\n' + opentag + '/' + root + closetag  #</root>






    for row in reader:
        print row


if __name__ == '__main__':
    loadFile(str(sys.argv[1]))
    print xmloutput