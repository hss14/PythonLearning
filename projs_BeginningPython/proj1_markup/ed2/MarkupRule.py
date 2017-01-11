from MarkupHandler import *

class Rules(object):
    """
    """
    def __init__(self, handler, name="paragraph"):
        self.handler = handler
        self.name = name

    def condition(self, block):
        return True

    def action(self, block):
        self.handler.startMethod( self.name )
        self.handler.feedMethod( self.name, block )
        self.handler.endMethod( self.name )
        return True  # true means no need for further probe


class headingRule(Rules):
    def condition(self, block):
        return ( '\n' not in block and block[-1]!=":" and len(block)<=70 )


class titleRule(headingRule):
    def __init__(self, handler, name="title"):
        super(titleRule, self).__init__(handler, name)
        self.firstline = True

    def condition(self, block):
        if self.firstline:
            self.firstline = False
            return headingRule.condition(self, block)        
        return False


class listitemRule(Rules):
    def condition(self, block):
        return block[0:2]=='- '
    def action(self, block):
        self.handler.startMethod( self.name )
        self.handler.feedMethod( self.name, block.strip("- ") )
        self.handler.endMethod( self.name )
        return True  # true means no need for further probe


class listRule(listitemRule):
    def __init__(self, handler, name="list"):
        super(listRule, self).__init__(handler, name)
        self.inlist = False

    def action(self, block):
        if not self.inlist and listitemRule.condition(self, block) :
            self.inlist = True
            self.handler.startMethod(self.name)
        elif self.inlist and not listitemRule.condition(self, block) :
            self.inlist = False
            self.handler.endMethod(self.name)
        return False  #continue probing
