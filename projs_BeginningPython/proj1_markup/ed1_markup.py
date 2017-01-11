#!/usr/bin/python

import sys, re, string

BlockPattern = re.compile( r"\n\n+" )   # >=2 newlines marks the end of a block

for infile in sys.argv[1:]:
    f = open( infile, 'r' )
    BlockList = BlockPattern.split( f.read() )
    f.close()
    try:
        while True:
            BlockList.remove("")
    except ValueError:
        pass
    for index,block in enumerate(BlockList):
        re.sub("\n", " ",block)
        block = "<p>" + re.sub( r"\*([^\*]+)\*", r"<em>\1</em>", block ) + "</p>\n"
        BlockList[index] = block
    BlockList[0] = re.sub( r"<(.*?)p>", r"<\1h1>", BlockList[0] )
    f = open( infile+"_output.html", "w" )
    f.writelines( BlockList )
    f.close()
