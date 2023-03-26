from Constants import *
import random

class BuilderSPC:

    log = "BuilderSPC: "

    def __init__(self, o) -> None:
        self.o = o
    
    def build(self):
        lns = Constants.getSPCTemplate(Constants.ANDL_NAME_OUTPUT)
        ptns = self.getPointersForSections(lns)
        for i in range(len(ptns)-1, -1, -1):
            pnt = ptns[i]
            if i == 0:
                print(self.log + "setting SPC variables")
                self.onStepVariableDeclaration(lns, pnt)
            elif i == 1:
                print(self.log + "setting SPC loop statement")
                self.onStepStepwise(lns, pnt)
            elif i == 2:
                print(self.log + "setting SPC place export")
                self.export(lns, pnt)
        print(f'{self.log} exporting spc')
        O = open(Constants.SPC_OUT, "w")
        O.writelines(lns)
        O.close()
        print(f'{self.log} spc exported.')    

    def onStepVariableDeclaration(self, lns, pnt):
        # Initialising the spc variable used to store 
        # the SPC code as a Python string.
        spc = ""
        # Get the options from the BuilderOptions.py.
        # The variables within this object are set from the
        # user through the parameters on running the script.
        nco = self.o.nco 
        # 2D list containing the x,y location for each complex 
        # object.
        # It uses the initial locations for each complex object
        # if set by the user, generate them randomly otherwise.
        # l0s for 2 complex objects which x,y initial locations 
        # are 3,2 and 4,1 does have the following content: 
        # [[3,2], [4,1]].
        l0s = self.parseL0s() if self.o.l0 > 0 \
            else self.generateL0s()
        m = self
        # add comments in the SPC script. 
        # m.n and m.t refer to self.n and self.n used for common 
        # characters.
        # self.t(n) returns a string with n tabs characters. 
        # eg. self.t(2) returns "\t\t".
        # this simplifies indentation when generating the spc file.
        # self.n return a string with a new line character. 
        # eg. self.n() return "\n".
        spc += f'// {m.t(2)} ++++++++ Code generated from the Builder ++++++++  {m.n()}'
        spc += f'// =================== ON STEP VARIABLE DECLARATION ================== {m.n()}'
        # For each complex object.
        for i in range(nco):
            # Create an id for the complex object. 
            id = str(i+1)
            # Getting the x,y initial location for the i_th 
            # complex object.
            lx0 = l0s[i][0]
            ly0 = l0s[i][1]
            # Store the x,y initial location lx0,ly0 for the i_th 
            # complex object as a string. This will help in the next
            # lines to use these values for writing the SPC code 
            # as a string.
            x = f'X_{id}'
            y = f'Y_{id}'
            # Writing the SPC code for declaring the initial 
            # locations for the i_th complex object
            # using Python string.
            spc += f'{m.t(1)}{x} = {lx0} ; {m.n()}'
            spc += f'{m.t(1)}{y} = {ly0} ; {m.n()}' 
            # Writing the SPC code for declaring the observers 
            # as Python strings
            spc += f'{m.t(1)}{x}_obv:observe:{x};{m.n()}'
            spc += f'{m.t(1)}{y}_obv:observe:{y};{m.n()}'
        # write a comment 
        spc += f'//================================================================== {m.n()}'
        # lns contains the full SPC script as a string.
        # pnt is a pointer indicating at which point of lns the 
        # content within the spc string has to be inserted.
        # Inserting the spc content in lns at line pnt
        lns.insert(pnt, spc)
    
    def onStepStepwise(self, lns, pnt):
        print(f'{self.log}writing onStep stepwise')
        nco = self.o.nco
        x = self.o.x
        y = self.o.y
        spc = ""
        m = self
        # for each complex object entity
        for i in range(nco-1, -1, -1):
            id = i+1
            # for each available ys within the grid environment
            for _y in range(1, y+1):
                # for each available xs within the grid environment
                for _x in range(1, x+1):
                    isIf = "if" if _x<=1 and _y<=1 else "else if"
                    spc += f'{m.t(1)}{isIf}(X_{id} == {_x} && Y_{id} == {_y}) {"{"}{m.n()}'
                    spc += f'{m.t(2)}// add here your code when complex object {id} {m.n()}'
                    spc += f'{m.t(2)}// is in location {_x};{_y}{m.n()}'
                    spc += f'{m.t(1)}{"}"}{m.n()}'
        lns.insert(pnt, spc)
    
    def export(self, lns, pnt):
        print(f'{self.log}writing spc export')
        m = self
        nco = m.o.nco
        spc = ""
        spc += f'{m.t(1)}places: [];{m.n()}'
        exb = f'{m.t(1)}observers: ['
        for i in range(nco):
            id = i+1
            exb += f'X_{id}_obv, Y_{id}_obv'
            exb += "" if i == nco-1 else ","
        
        spc += f'{exb}];{m.n()}'
        lns.insert(pnt, spc)
    
    def generateL0s(self):
        x = self.o.x
        y = self.o.y
        nco = self.o.nco
        x0 = [random.randrange(1,x , 1) for t in range(nco)]  
        y0 = [random.randrange(1,y , 1) for t in range(nco)] 
        l0s = []
        for i in range(len(x0)):
            l0s.append([x0[i], y0[i]])
        return l0s

    def parseL0s(self):
        l0s = self.o.l0.split(",")
        l0 = []
        for l in range(len(l0s)):
            cs = l0s[l].split(";")
            l0.append(int(cs[0]), int(cs[1]))
        return l0

    
    def getPointersForSections(self,lns):
        pnts = []
        for i in range(0, len(lns)):
            l = lns[i]
            if Constants.SPC_COMMENT_FOR_LOOP_VARIABLES in l:
                pnts.append(i+1)
            elif Constants.SPC_COMMENT_FOR_LOOP_STATEMENT in l:
                pnts.append(i+1)
            elif Constants.SPC_COMMENT_FOR_PLACE_EXPORT in l:
                pnts.append(i+1)
        return pnts

    def b(self, isOpen):
        return "{" if isOpen else "}"
    
    def t(self,identation):
        return "\t"*identation

    def n(self):
        return "\n"
    


    