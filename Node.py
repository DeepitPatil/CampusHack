class Node():
    def __init__(self,name,link, parent):
        self._name=name
        self._link=link
        self.parent = parent
        self.children = []
        if(parent != None):
            parent.children.append(self)
    
    def getName(self):
        return self._name

    def getLink(self):
        return self._link
    
    def setName(self,name):
        self._name = name

    def setLink(self, link):
        self._link = link
        

    