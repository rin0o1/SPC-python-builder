from BuilderANDL import *
from BuilderSPC import *
class BuilderHandler:
    log = "BuilderHandler: "
    def build(self,o):
        self.o = o
        print(self.log + "starting genearation")
        self.buildANDL()
        self.buildSPC()
        print(f'{self.log}generation completed')
    
    def buildANDL(self):
        print(self.log + "Building ANDL")
        BuilderANDL(self.o).build()
    
    def buildSPC(self):
        print(self.log + "Building SPC")
        BuilderSPC(self.o).build()
    
