#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modified by Yu Wang(wyhitcs@gmail.com)

# Modify code from Claus Haslauer (https://github.com/clausTue/OO_latex)
# Reasons of Modify: MacTex have different texbin; pdfcrop is a perl script could not get right result in shell command, remove crop in python script and add Terminal execution in applescript

# Time: 2016.04.17
"""

"""
import sys
import os
import datetime
import time




def main():
    """
    this script uses `pdflatex` and `pdfcrop` to produce a pdf of a latex string that is passed to the script as command line argument
    
    requires valid latex installation
    
    - there is no test for this string being a valid latex expression
    
    """
    
    cur_path = os.getcwd() 
    
    # # check if previous files exist; if yes: delete them
    filenames = ["temp.ps"
               , "temp.aux"
               , "temp.dvi"
               , "temp.log"
               , "temp.tex"
               , "temp.pdf"
               , "temp-crop.pdf"]
    for filename in filenames:
        try:
            os.remove(filename)
        except:
            print "file did not exist"
            pass
           
    # # other option    
    #if os.path.isfile(os.path.join(cur_path, 'temp.ps')):
        
    
    
    
    # # this is the latex string that is being passed
    str_latex_note = sys.argv[1]
    print "%s" %  str_latex_note
    if str_latex_note == '':
        str_latex_note = " \hspace{0.2cm} ".join("LaTex string should be note of the selected row.".split())
 
 
     # # this is a minimal latex template into which the string is inserted
    preamble = """\documentclass{article}
\usepackage{amsmath,amssymb}
\pagestyle{empty}

\\begin{document}
{\huge
\[
 %s
 \]
}
\end{document}"""% (str_latex_note)
     
    
    ## write latex file
    cur_file = "temp.tex"
    fobj = open(os.path.join(cur_path, cur_file), 'w')
    fobj.writelines(preamble)
    fobj.close()
    
    ## process latex file
    # print cur_path
    os.chdir(cur_path)
    # Here change the path
    cmd = '/Library/Tex/texbin/pdflatex temp.tex'
    # print cmd
    # print "running latex"
    os.system(cmd)

    
    
if __name__ == '__main__':
    main()
