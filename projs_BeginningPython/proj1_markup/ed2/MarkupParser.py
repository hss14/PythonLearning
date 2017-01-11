import sys, string
from MarkupRule import *
from MarkupHandler import *

def getBlock( f = sys.stdin ):
    """ yield each block of file object f, 
        which is the only parameter whose default value equals sys.stdin
    """
    block = []
    for l in f:
        line = l.strip()
        if line:
            block.append( line )
        elif block:
            yield '\n'.join(block)
            block = []
    if block:
        yield '\n'.join(block)



class MarkupParser(object):
    """
    """

    def __init__(self, handler, fileno):
        self.fileno = fileno
        self.ruleList=[]
        self.filterList={}
        self.handler = handler

    def addRule(self, rule):
        self.ruleList.append(rule)

    def addFilter(self, name, pattern):
        self.filterList[name] = pattern

    def parse(self):
        for theblock in getBlock(self.fileno):
            block = theblock
            for name,pattern in self.filterList.items():
                block = re.sub(pattern, self.handler.subMethod(name), block)
            for rule in self.ruleList:
                if rule.condition(block):
                    if rule.action(block): break




def main():

    emphasisPattern = r"\*([^\*]+?)\*"
    urlPattern = r"(http://[/a-zA-Z0-9\.]+)"
    emailPattern = r"([a-zA-Z0-9\.\-_]+@[a-zA-Z0-9\.\-_]+)"

    for filename in sys.argv[1:] :
        fileno = open(filename,"r")
        outfilename = filename+".html"
        outfileno = open(outfilename, "w")

        handler = HTMLHandler(f=outfileno)
        parser = MarkupParser(handler, fileno)

        parser.addFilter("emphasis",emphasisPattern)
        parser.addFilter("url",urlPattern)
        parser.addFilter("email",emailPattern)

        parser.addRule( titleRule(handler,"title") )
        parser.addRule( headingRule(handler, "heading") )
        parser.addRule( listRule(handler,"list") )
        parser.addRule( listitemRule(handler,"listitem") )
        parser.addRule( Rules(handler,"paragraph") )

        parser.parse()

        fileno.close()
        outfileno.close()



if __name__ == "__main__": main()
