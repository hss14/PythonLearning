import sys,os
from xml.sax.handler import ContentHandler
from xml.sax import parse

class Dispatch(object):
    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs )

    def endElement(self, name):
        self.dispatch('end', name )

    def dispatch(self, prefix, name, attrs=None ):
        method = getattr( self, prefix + name.capitalize(), None )
        if hasattr( method, '__call__' ):
            args = ()
        else:
            method = getattr( self, prefix + 'Default', None )
            if not hasattr( method, '__call__' ):
                return
            args = (name,)
        if prefix=='start':
            args += (attrs,)
        method( *args )

class WebsiteHandler( Dispatch, ContentHandler ):
    def __init__(self, serverPath):
        self.fd = sys.stdout
        self.inPage = False
        self.dirList = [ serverPath ]
        self.ensurePath()

    def ensurePath(self):
        path = os.path.join( *self.dirList )
        if not os.path.isdir(path):
            os.makedirs(path)

    def writeHeader(self, title):
        prefix = [ "<!DOCTYPE html>\n", "<html>\n", "\t<head>\n", 
			"\t\t<title>" + title + "</title>\n",
			"\t</head>\n", "\t<body>\n" ]
        self.fd.writelines(prefix)

    def writeFooter(self):
        postfix = [ "\t</body>\n", "</html>\n" ]
        self.fd.writelines(postfix)

    def startDefault(self, name, attrs):
        if self.inPage:
            self.fd.write( '\t\t<' + name )
            if attrs:
                for k,d in  attrs.items():
                    self.fd.write( ' %s="%s" ' % (k,d) )
            self.fd.write( '>' )

    def endDefault(self, name):
        if self.inPage:
            self.fd.write( '\t\t</%s>\n' % name )

    def characters(self, string):
        if self.inPage:
            self.fd.write(string) 

    def startDirectory(self, attrs):
        self.dirList.append( attrs['name'] )
        self.ensurePath()

    def endDirectory(self):
        self.dirList.pop()

    def startPage(self, attrs):
        self.inPage = True
        self.dirList.append( attrs['name']+'.html' )
        self.fd = open( os.path.join(*self.dirList), 'w' )
        self.writeHeader( attrs['title'] )

    def endPage(self):
        self.writeFooter()
        self.fd.close()
        self.dirList.pop()
        self.inPage = False



parse( sys.argv[1], WebsiteHandler(sys.argv[2]) )
