import sys, os
from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):

    def __init__(self, serverPath):
        self.filename = [serverPath]
        self.fd = sys.stdout
        self.inPage = False

    def startElement(self, name, attrs):
        if name=="page":
            self.start_page(attrs)
        elif name=="directory":
            self.start_directory(attrs)
        elif name=="website": pass
        elif self.inPage:
            if attrs:
                self.fd.write( "\t\t<" + name  )
                for k,d in attrs.items():
                    self.fd.write( ' ' + k + '="' + d + '"' )
                self.fd.write( ">" )
            else:
                self.fd.write( "\t\t<"+name+">" )

    def endElement(self, name):
        if name=="page":
            self.end_page()
        elif name=="directory":
            self.end_directory()
        elif name=="website": pass
        elif self.inPage:
            self.fd.write( "</"+name+">\n" )

    def characters(self, string):
        if self.inPage and string.strip():
            self.fd.write(string)

    def start_directory(self, attrs):
        self.filename.append( attrs['name']+'/' )
        os.makedirs( "".join(self.filename) )

    def end_directory(self):
        self.filename.pop()

    def start_page(self, attrs):
        self.inPage = True
        self.filename.append( attrs['name']+".html" )
        self.fd = open( "".join(self.filename), "w" )
        prefix = [ "<!DOCTYPE html>\n", "<html>\n", "\t<head>\n", 
			"\t\t<title>" + attrs['title'] + "</title>\n",
			"\t</head>\n", "\t<body>\n" ]
        self.fd.writelines(prefix)

    def end_page(self):
        postfix = [ "\t</body>\n", "</html>\n" ]
        self.fd.writelines(postfix)
        self.fd.close()
        self.filename.pop()
        self.inPage = False

parse( sys.argv[1], TestHandler( sys.argv[2] ) )
