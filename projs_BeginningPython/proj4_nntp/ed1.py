from nntplib import NNTP

class GetNNTP(object):

    def __init__(self, serverlist, grouplist, date, time):
        self.serverlist = serverlist
        self.grouplist = grouplist
        self.date = date
        self.time = time

    def addSource(self, server, group):
        self.serverlist.append(server)
        self.grouplist.append(group)

    def getNews(self):
        for server,group in enumerate(self.serverlist, self.grouplist):
            srv = NNTP(server)
            ids = srv.newnews(group, self.date, self.time)[1]
            for news in ids:
                head = server.head(news)[3]
                    for line in head:
                        if line.lower().startswith("subject:"):
                            subject = line[9:]
                            break
                body = server.body(news)[3]
                content = "\n".join(body)
                yield (subject, content)
        srv.quit()



class NewsHandler(object):

    def __init__(self,  ):
