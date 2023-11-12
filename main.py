# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from gcodeparser import GcodeParser
import gcodetime
import sys

# Press the green button in the gutter to run the script.
filename = sys.argv[1]


def ngc2gcode(inputFile):
    with open(inputFile, 'r') as f:
        gval = ''
        newlines = []
        for line in f:
            if line in ['\n', '\r\n']:
                newlines.append(line)
            elif 'M' in line:
                newlines.append(line)
            elif 'G04' in line:
                newlines.append(line)
            elif 'G' in line and not ('G04' in line):
                gval = line[line.find('G'):line.find(' ')]

                if gval == 'G0' or gval == 'G00':
                    gval = 'G00'
                elif gval == 'G1' or gval == 'G01':
                    gval = 'G01'
                elif gval == 'G2' or gval == 'G02':
                    command = 'G02'
                elif gval == 'G3' or gval == 'G03':
                    gval = 'G03'

                if line.startswith('G0 ', 0, 3):
                    newlines.append(line.replace('G0', 'G00'))
                elif line.startswith('G1 ', 0, 3):
                    newlines.append(line.replace('G1', 'G01'))
                elif line.startswith('G2 ', 0, 3):
                    newlines.append(line.replace('G2', 'G02'))
                elif line.startswith('G3 ', 0, 3):
                    newlines.append(line.replace('G3', 'G03'))
                elif line.startswith('G4 ', 0, 3):
                    newlines.append(line.replace('G4', 'G04'))
                elif line.startswith('G5 ', 0, 3):
                    newlines.append(line.replace('G5', 'G05'))
                elif line.startswith('G6 ', 0, 3):
                    newlines.append(line.replace('G6', 'G06'))
            else:
                l = gval + ' ' + line
                newlines.append(l)
        f.close()
        outputFile = inputFile[0:inputFile.index('.')]
        outputFile = outputFile + '.gcode'

        outfile = open(outputFile, 'w')
        for item in newlines:
            outfile.write('%s' % item)
        outfile.close()
    return (outputFile)


#gcodefile = ngc2gcode("Baum.ngc")  # output file from pycam gcode generator
with open('example.gcode', 'r') as f1:
    gcode = f1.read()
    parsed_gcode = GcodeParser(gcode)
    f1.close()

codelines = parsed_gcode.lines
pparam = {'X': 0, 'Y': 0, 'Z': 0, 'F': 2, 'S': 0, 'T': 0}
for line in codelines:
    var = getattr(gcodetime, 'code' + line.command_str)
    pparam = var(pparam, line.params)

print(pparam['T'])


