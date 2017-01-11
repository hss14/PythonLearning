import sys,string,re

class MarkupHandler(object):
    """
    """
    def __init__(self, f=sys.stdin):
        self.fileno = f

    def callback(self, methodName, *args):
        method = getattr(self, methodName, None)
        if callable(method): return method(*args)

    def startMethod(self, name, *args):
        return self.callback( "start_"+name, *args )

    def endMethod(self, name, *args):
        return self.callback( "end_"+name, *args )

    def subMethod(self, name, *args):
        def replacement(match):
            method = self.callback( "sub_"+name, match )
            if method is None:
                return match.group(0)
            return method
        return replacement

    def feedMethod(self, name, block):
        self.fileno.write( block )



class HTMLHandler(MarkupHandler):
    """
    """
    def __init__(self, f=sys.stdin, title="..."):
        super(HTMLHandler, self).__init__(f)
        self.fileno.write("<html><head><title>"+title+"</title></head><body>")

    def sub_emphasis(self, match):
        return "<em>" + match.group(1) + "</em>"

    def sub_url(self, match):
        return "<a href='%s'>%s</a>" % ( match.group(1), match.group(1) )

    def sub_email(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def start_paragraph(self):
        self.fileno.write("<p>")

    def end_paragraph(self):
        self.fileno.write("</p>\n")

    def start_heading(self):
        self.fileno.write("<h2>")

    def end_heading(self):
        self.fileno.write("</h2>\n")

    def start_title(self):
        self.fileno.write("<h1>")

    def end_title(self):
        self.fileno.write("</h1>\n")

    def start_list(self):
        self.fileno.write("<ul>\n")

    def end_list(self):
        self.fileno.write("</ul>\n")

    def start_listitem(self):
        self.fileno.write("\t<li>")

    def end_listitem(self):
        self.fileno.write("\t</li>\n")

