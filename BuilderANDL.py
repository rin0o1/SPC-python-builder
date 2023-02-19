import os
from Constants import *

class BuilderANDL:
    log = "BuilderANDL: "
    def __init__(self,o):
        self.o = o
    
    def build(self):
        lns = self.loadCandl()
        self.editCandl(lns)
        self.exportLines(lns)
        self.generateANDL()

    def loadCandl(self):
        print(self.log + "Loading CANDL")
        cI = self.o.candlI
        if not os.path.exists(cI):
            print(self.log + "Candl file does not exist")
        lns = []
        with open(cI, "r") as file:
            lns = file.readlines()
            file.close()
        return lns

    def editCandl(self, lns):
        print(self.log + "Adapting the CANDL")
        pnts = []
        nls = len(lns)
        for i in range(0,nls):
            l = lns[i]
            l += "\n"
            if "//"+Constants.CANDL_COMMENT_NUMBER_OF_INSTANCE_COMPLEX_OBJECT in l:
                pnts.append(i+1)
            if "//"+Constants.CANDL_COMMENT_DIMENSIONS in l:
                pnts.append(i+1)
        
        for i in range(len(pnts)-1, -1, -1):
            pnt = pnts[i]

            if i == 0:
                x = f"\tint {Constants.CANDL_GRID_DIMENSION_X} = " + str(self.o.x) + "; \n"
                y = f"\tint {Constants.CANDL_GRID_DIMENSION_Y} = " + str(self.o.y) + "; \n"
                lns[pnt] = x + y
            
            if i == 1:
                inst = f"\tint {Constants.CANDL_INSTANCES} = " + str(self.o.nco) + " ;\n"
                lns[pnt] = inst
    
    def exportLines(self, lns):
        print(self.log +"Preparing for exporting")
        O = open(Constants.CANDL_NAME_OUTPUT, "w")
        O.writelines(lns)
        O.close()
    
    def generateANDL(self):
        CANDL = Constants.CANDL_NAME_OUTPUT
        ANDL = Constants.ANDL_NAME_OUTPUT
        os.system("spike load -f= " + CANDL + " unfold save -f="+ANDL)
        print(self.log + "ANDL generated successfully")
