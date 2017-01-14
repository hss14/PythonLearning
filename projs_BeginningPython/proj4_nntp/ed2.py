from nntplib import NNTP
from time import time,localtime,strftime
import sys

class NewItem(object):
    def __init__(self, title, body):
        self.title = title
        self.body = body


class NewsAgent(object):

    def __init__(self):
        self.srcs = []
        self.dests = []

    def addSource(self, source):
        self.srcs.append(source)

    def addDestination(self, dest):
        self.dests.append(dest)

    def distribute(self):
        items = []
        for src in self.srcs:
            items.append( src.getItem() ) #extend in sample code
        for dest in self.dests:
            dest.receive(items)


class NNTPSource(object):

    def __init__(self, server, group, date, time):
        self.servername = server
        self.group = group
        self.date = date
        self.time = time

    def getItem(self):
        server = NNTP(self.servername)
        ids = server.newnews(self.group, self.date, self.time)[1]
        for news in ids:
            head = server.head(news)[3]
                for line in head:
                    if line.lower().startswith("subject:"):
                        subject = line[9:]
                        break
            body = server.body(news)[3]
            content = "\n".join(body)
            yield NewItem(subject, content)
        server.quit()



class PlainDestination(object):

    def __init__(self, filename=""):
        if filename:
            self.fd = open(filename,"w")
        else:
            self.fd = sys.stdout

    def receive(self, items):
        for item in items:
            self.fd.write( item.title )
            self.fd.write( '*'*len(item.title) )
            self.fd.write( item.body )
            self.fd.write( '\n'*3 )
        self.fd.close()


def runDefaultSetup():

    SECS = 24 * 60 * 60
    server = sys.argv[1]
    group = sys.argv[2]
    timeset = localtime( time() - SECS * eval(sys.argv[3]) )
    date = strftime("%y%m%d", timeset)
    time = strftime("%H%M%S", timeset)
    nntpsrc = NNTPSource( server, group, date, time)

    agent = NewsAgent()
    agent.addSource( nntpsrc )
    agent.addDestination( PlainDestination() )
    agent.distribute()



if __name__=="__main__": runDefaultSetup()
