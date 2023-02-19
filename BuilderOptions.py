from Constants import *

class BuilderOptions:
    
    def setOptions(self, x, y, nco, spc, candl):
        # check options before setting them
        self.x = x
        self.y = y
        self.nco = nco
        self.spc = spc
        self.andlO = Constants.ANDL_NAME_OUTPUT
        self.candlO = Constants.CANDL_NAME_OUTPUT
        self.candlI = candl
        self.l0 = -1
        #return 0 if everything is fine, otherwise reports error
        return 0
