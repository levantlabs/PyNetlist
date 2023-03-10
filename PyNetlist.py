#Python based netlist generator
#Created by Manar El-Chammas
#Purpose is to generate spice netlists using python primitives
#Gen1: Targets skywaterpdk-130nm

class PyNetlist:

    def __init__(self, PDKname, netlistname):
        self.PDKname = PDKname
        self.netlistname = netlistname

        #Load PDK details

    def netlistHeader(self, header):
        self.netlistHeader = header

    def addElement(self, elemType, elemName, nets, parameters, constraints):
        '''Add element to netlist
        elemType is either device or module
        nets is the list of nets that this connects to
        parameters are additional parameters
        constraints are additional constaints'''




#Class of devices that contains details on different primitives
class Devices:

    def __init__(self, deviceType, connections, properties):
        self.test = 1

#Modules or circuits that are treated as a whole
class Modules:

    def __init__(self, name):
        #Defines name for module
        self.name = name

        
        
