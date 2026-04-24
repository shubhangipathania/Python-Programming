class Library:
    def __init__(self, bid, bname ):
        self._bid= bid
        self._bname=bname

    @property
    def bid(self):
        return self._bid
    
    @bid.setter
    def bid(self, newid):
        self._bid= newid

    @property
    def bname(self):
        return self._bname
    
    @bname.setter
    def bname(self, newname):
        self._bname= newname


obj1=Library(12334, "Better than the Movies")
print(obj1.bid, obj1.bname)
obj1.bname= "The 5Am Club"
print(obj1.bid, obj1.bname)