import copy
import math
import sys
from typing import overload

sys.path.insert(0, "../ChironCore/")

import cfg.ChironCFG as cfgK
import cfg.cfgBuilder as cfgB
from lattice import  *
import ChironAST.ChironAST as ChironAST
import abstractInterpretation as AI

'''
    Class for interval domain
'''
class IntervalDomain(Lattice):

    '''Initialize abstract value'''
    def __init__(self, data):
        pass

    '''To display abstract values'''
    def __str__(self):
        pass

    '''To check whether abstract value is bot or not'''
    def isBot(self):
        pass

    '''To check whether abstract value is Top or not'''
    def isTop(self):
        pass

    '''Implement the meet operator'''
    def meet(self, other):
        pass

    '''Implement the join operator'''
    def join(self, other):
        pass

    '''partial order with the other abstract value'''
    def __le__(self, other):
        pass

    '''equality check with other abstract value'''
    def __eq__(self, other):
        pass

    '''
        Add here required abstract transformers
    '''
    pass

assgn_dict = {}
class IntervalTransferFunction(TransferFunction):
    def __init__(self):
        pass

    def transferFunction(self, currBBIN, currBB):
        '''
            Transfer function for basic block 'currBB'
            args: In val for currBB, currBB
            Returns newly calculated values in a form of list

            This is the transfer function you write for Abstract Interpretation.
        '''
        #implement your transfer function here
        print("transferFunction called -----")
        bbout = copy.deepcopy(currBBIN)
        print(currBBIN)
        print(currBB.instrlist[0][0])

        if(type(currBB.instrlist[0][0])==ChironAST.MoveCommand):
            print("move command -----")
            print(str.split(str(currBB.instrlist[0][0])))
            
            
            if(len(currBBIN)!=0):
                if(str.split(str(currBB.instrlist[0][0]))[0]== "forward"):
                    step_to_move = str.split(str(currBB.instrlist[0][0]))[1]
                    if(currBBIN['IN']['D'] == 'Xpositive'):
                                bbout['IN']['X'][0] = int(step_to_move) + currBBIN['IN']['X'][0]
                                bbout['IN']['X'][1] = int(step_to_move) + currBBIN['IN']['X'][1]

                    if(currBBIN['IN']['D'] == 'Xnegative'):
                                bbout['IN']['X'][0] = -1*int(step_to_move) + currBBIN['IN']['X'][0]
                                bbout['IN']['X'][1] = -1*int(step_to_move) + currBBIN['IN']['X'][1]

                    if(currBBIN['IN']['D'] == 'Ypositive'):
                                bbout['IN']['Y'][0] = int(step_to_move) + currBBIN['IN']['Y'][0]
                                bbout['IN']['Y'][1] = int(step_to_move) + currBBIN['IN']['Y'][1]

                    if(currBBIN['IN']['D'] == 'Ynegative'):
                                bbout['IN']['Y'][0] = -1*int(step_to_move) + currBBIN['IN']['Y'][0]
                                bbout['IN']['Y'][1] = -1*int(step_to_move) + currBBIN['IN']['Y'][1]
                
                if(str.split(str(currBB.instrlist[0][0]))[0]== "backward"):
                    step_to_move = str.split(str(currBB.instrlist[0][0]))[1]
                    if(currBBIN['IN']['D'] == 'Xpositive'):
                                bbout['IN']['X'][0] =  currBBIN['IN']['X'][0] - int(step_to_move)
                                bbout['IN']['X'][1] =  currBBIN['IN']['X'][1] - int(step_to_move)

                    if(currBBIN['IN']['D'] == 'Xnegative'):
                                bbout['IN']['X'][0] = int(step_to_move) + currBBIN['IN']['X'][0]
                                bbout['IN']['X'][1] = int(step_to_move) + currBBIN['IN']['X'][1]

                    if(currBBIN['IN']['D'] == 'Ypositive'):
                                bbout['IN']['Y'][0] = currBBIN['IN']['Y'][0] - int(step_to_move)
                                bbout['IN']['Y'][1] = currBBIN['IN']['Y'][1] - int(step_to_move) 
                                
                    if(currBBIN['IN']['D'] == 'Ynegative'):
                                bbout['IN']['Y'][0] = int(step_to_move) + currBBIN['IN']['Y'][0]
                                bbout['IN']['Y'][1] = int(step_to_move) + currBBIN['IN']['Y'][1]

                if(str.split(str(currBB.instrlist[0][0]))[0] == "right"):
                        print("right")
                        if(currBBIN['IN']['D'] == 'Xpositive'):
                            bbout['IN']['D'] = 'Ynegative'
                        elif(currBBIN['IN']['D'] == 'Xnegative'):
                            bbout['IN']['D'] = 'Ypositive'
                        elif(currBBIN['IN']['D'] == 'Ypositive'):
                            bbout['IN']['D'] = 'Xpositive'
                        elif(currBBIN['IN']['D'] == 'Ynegative'):
                            bbout['IN']['D'] = 'Xnegative'


                if(str.split(str(currBB.instrlist[0][0]))== "left"):
                        print("left")
                        if(currBBIN['IN']['D'] == 'Xpositive'):
                            bbout['IN']['D'] = 'Ypositive'
                        elif(currBBIN['IN']['D'] == 'Xnegative'):
                            bbout['IN']['D'] = 'Ynegative'
                        elif(currBBIN['IN']['D'] == 'Ypositive'):
                            bbout['IN']['D'] = 'Xnegative'
                        elif(currBBIN['IN']['D'] == 'Ynegative'):
                            bbout['IN']['D'] = 'Xpositive'
                        
                        
        if(type(currBB.instrlist[0][0])==ChironAST.ConditionCommand):
            print("Condition Command")




        # bbout = copy.deepcopy(currBBIN)
        # print("--------",bbout)
        # print("-----------------",bbout['IN'])
                
        outVal = []
        return outVal

class ForwardAnalysis():
    def __init__(self):
        self.transferFunctionInstance = IntervalTransferFunction()
        self.type = "IntervalTF"

    '''
        This function is to initialize in of the basic block currBB
        Returns a dictinary {varName -> abstractValues}
        isStartNode is a flag for stating whether currBB is start basic block or not
    '''
    def initialize(self, currBB, isStartNode):
        StartBlock = {}
        Xleft=0
        Xright=50
        Yleft=0
        Yright=50
        Negativerange=-500
        if(isStartNode):
            print("initializeFunction -------------------")
            StartBlock = {'OUT' : { }, 'IN' : {'X' : [Xleft,Xright] , 'Y' : [Yleft,Yright] , 'D' : 'Xpositive' }}
        #Your additional initialisation code if any
        return StartBlock

    #just a dummy equallity check function for dictionary
    def isEqual(self, dA, dB):
        for i in dA.keys():
            if i not in dB.keys():
                return False
            if dA[i] != dB[i]:
                return False
        return True

    '''
        Define the meet operation
        Returns a dictinary {varName -> abstractValues}
    '''
    def meet(self, predList):
        print("MeetFunction --------------------")


def analyzeUsingAI(irHandler):
    '''
        get the cfg outof IR
        each basic block consists of single statement
    '''
    # call worklist and get the in/out values of each basic block
    print("Analyze        Function")
    abstractInterpreter = AI.AbstractInterpreter(irHandler)
    bbIn, bbOut = abstractInterpreter.worklistAlgorithm(irHandler.cfg)
    

    #implement your analysis according to the questions on each basic blocks
    

    pass
