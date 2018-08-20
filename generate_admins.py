#!/usr/bin/python3
import barcode
from barcode.writer import ImageWriter
import numpy as np
import sqlite3
import os
import glob, os
os.chdir("./")
pics = []

CODE128 = barcode.get_barcode_class('code128')
code128 = CODE128("0000",writer=ImageWriter())
code128.save("ANNULER")
code128 = CODE128("9999",writer=ImageWriter())
code128.save("LOG UD")

conn = sqlite3.connect('øllerbøller.db')
c = conn.cursor()

c.execute("SELECT * FROM øller")
øller = c.fetchall()

for ø in øller:
    code128 = CODE128(str(ø[0]),writer=ImageWriter())
    code128.save(ø[1])
conn.close()

for file in glob.glob("*.png"):
    pics.append(file)

print (pics)
workfile = "admins.tex"
F = open(workfile,"a")
F.write("\\documentclass[a4paper,11pt]{article}")
F.write("\\usepackage{graphicx}")
F.write("\\usepackage[utf8]{inputenc}")
F.write("\\usepackage[T1]{fontenc}")
F.write("\\usepackage[danish]{babel}")
F.write("\\usepackage{array}")
F.write("\\usepackage{ragged2e}")
F.write("\\begin{document}")
for pic in pics:
    dot = pic.find(".")
    print (pic)
    F.write("\\"+"begin{table}[h!]\n")
    F.write("    \\begin{tabular}{  l l }\n")
    F.write("\\includegraphics[height=3cm,width=0.3\\textwidth]{"+pic+"}\n")
    F.write(" &   \\Huge{"+pic+"}\\\\ \\hline\n")
    F.write("    \\end{tabular}\n")
    F.write("\\end{table}\n")
    F.write(" \n")
    F.write(" \n")



F.write("\\end{document}")
F.close()
