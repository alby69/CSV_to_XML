__author__ = 'William'
import csv
import sys
import re

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
    root = re.sub(r'\W+', '', select[0])
    element = re.sub(r'\W+', '', select[1])
    select = reader.next()
    attributes = select
    buildxml(reader)


def buildxml(reader):
    global xmloutput
    xmloutput += opentag + root + closetag  #<root>
    #<attributes>
    for row in reader:
        buildAttributes(row)
    xmloutput += '\n' + opentag + '/' + root + closetag  #</root>


def buildAttributes(row):
    global xmloutput
    xmloutput += '\n\t' + opentag + element + closetag  #<element>
    for i in range(len(attributes)):
        attribute = re.sub(r'\W+', '', attributes[i])
        xmloutput += '\n\t\t' + opentag + attribute + closetag + row[i] + opentag + '/' + attribute + closetag
    xmloutput += '\n\t' + opentag + '/' + element + closetag  #</element>


def saveToFile(filename):
    text_file = open(filename, 'w')
    text_file.write(xmloutput)
    text_file.close()


if __name__ == '__main__':
    loadFile(str(sys.argv[1]))
    saveToFile(sys.argv[2])
    #print xmloutput