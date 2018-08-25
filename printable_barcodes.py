#!/usr/bin/python3
import os
import sys

names = open('students.csv').readlines()
barcodes = []
for n in names:
    barcodes.append(n.split(',')[0].replace(' ', '_'))

f = open('output.tex', 'w')

header = "".join(open('header.tex', 'r').readlines()[:-1])

f.write(header)

#barcodes = os.listdir('barcodes')[:6]

c = 0
new = False
first = True
f.write("\\begin{figure}[H]\n")
row = ""
while c < len(barcodes):
    if c % 3 == 0 and not first:
        f.write(row)
        f.write("\\end{figure}\n")
        f.write("\\begin{figure}[H]\n")
        row = ""
    row += "\\begin{subfigure}[t]{0.3\\textwidth}\n"
    row += "\\centering\n"
    row += "\\fbox{\\includegraphics[scale=0.6]{barcodes/" + barcodes[c] + ".png}}\n"
    row += "\\caption*{" + barcodes[c].replace('_', ' ') + "}\n"
    row += "\\end{subfigure}\n"

    first = False
    c += 1

print(type(barcodes[0]))
f.write("\\end{figure}\n")
f.write("\\end{document}")
f.close()

os.system("pdflatex output.tex")
#os.remove("output.tex")
os.remove("output.aux")
os.remove("output.log")
