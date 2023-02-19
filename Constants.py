
class Constants:
    ANDL_NAME_OUTPUT =  "generated-andl.andl"
    CANDL_NAME_OUTPUT = "generated-candl.candl"
    SPC_OUT = "spcOut"
    CANDL_COMMENT_FOR_DIMENSIONS = "//DIMENSIONS"
    CANDL_COMMENT_FOR_INSTANCES = "//INSTANCES"
    SPC_COMMENT_FOR_LOOP_VARIABLES = "//LOOP_VARIABLES"
    SPC_COMMENT_FOR_LOOP_STATEMENT = "//LOOP_STATEMENT"
    SPC_COMMENT_FOR_PLACE_EXPORT = "//PLACE_EXPORT" 

    @staticmethod
    def getSPCTemplate(ANDL,isCont = 0):
        simulationTypeStoch= 'type:stochastic: { solver: direct: { threads: 1; runs: 1; } single: true; } \n'
        simulationTypeCont= 'type:continuous : {   solver:  BDF: {   semantic: "adapt"; iniStep: 0.1; linSolver: "CVDense"; relTol: 1e-5;  absTol: 1.0e-10;  autoStepSize: false;  reductResultingODE: true;  checkNegativeVal: false;  outputNoiseVal: false;   }   single: true; } \n'
        lines=  ['import: {           \n ',
        '\tfrom: "'+ANDL +'";      \n ',
        '}  \n ',
        'configuration: {  \n ',
        '\tmodel: {  \n ',
        '\n ',
            '\tplaces: {   \n ',
            '\n ',
        '\n ',
            '\t}      \n ',
        '\n ',
        '}  \n ',
        'simulation:  \n ',
        '\t{  \n ',
            '\t// Name of a simulation  \n ',
            '\tname: "SIR";  \n ',
            '\t/*  \n ',
            '\t* Set up a simulation  \n ',
            '\t*/  \n ',
            simulationTypeCont if not isCont else simulationTypeStoch,        
            '\tinterval: 0:100:100;  \n ',
            '\n ',        
            '\tonStep: { \n ',
            '\n ',
        '\n ',
            '//LOOP_VARIABLES \n ',
        '\n ',
                '\n ',
        '\n ',
            'do: { \n ',
        '\n ',
                f'//LOOP_STATEMENT \n ',
        '\n ',
                '\n ',
            '} \n ',
            '\n ',
        '} \n ',
            '\n ',
            'export: {         \n ',
            '//PLACE_EXPORT \n ',
            '\n ',
                            '\tcsv: {  \n ',
                    '\t\t\sep: ",";// Separator    \n ',
                    '\t\tfile: "result"  \n ',
                        '\t\t\<< ".csv";// File name  \n ',
                    '\t}  \n ',
            '}  \n ',
        '}  \n ',
        '}     \n ',
        '\n ']

        return lines