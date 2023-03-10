#Contains details on the skywater PDK
#There might be a better way to do this vs. a class, such as a spreadsheet
#Should each device be its own object?  There might be additional useful information that can be stored there
#It is possilbe that these closes would inherit functions from others, so that they aren't repeated?

import pandas as pd
class PDK_skywater130():

    def __init__(self, modelList, debug=False):
        self.count_devices_used = 0 #Tracks how many different device types are used
        self.count_devices_instantiated = 0 #Tracks how many devices are instantiated
        self.devices_used_list = [] #Contains list of devices types that have been used
        self.modelList = modelList
        self.modelCount = 0
        self.debug = debug #Used for debugging


        #Parameters for xlsx file column names
        self.genericName = 'GenericName'
        self.PDKDevice = 'PDKDevice'
        self.parameterNumber = 'ParameterNumber'

        self.initializeDeviceList()

    def initializeDeviceList(self):
        #Import with pandas
        temp_models = pd.read_excel(self.modelList)

        if self.debug:
            print(temp_models)

        list_columns = temp_models.columns
        #Check to make sure all the required names exist.
        missingColumn = False
        if self.genericName not in list_columns:
            missingColumn = True
        if self.PDKDevice not in list_columns:
            missingColumn = True
        if self.parameterNumber not in list_columns:
            missingColumn = True

        # Check to make sure the right columns are there
        if missingColumn:
            print('Error:  Device list does not have the right column names.')
            print('Column names are {}, {}, {}.'.format(self.genericName, self.PDKDevice, self.parameterNumber))
            print('EXITING...')
            exit()

        modelNames = temp_models[self.genericName]
        if self.debug:
            print('Model names included are: \n{}'.format(modelNames))

        checkCount = len(set(modelNames))
        if checkCount != len(modelNames):
            print('Error: Device defined multiple times.')
            print('EXITING...')
            exit()

        self.modelNames = modelNames
        #Get parameters for each model name
        #Set up as a dictionary?





    def addDevice(self, deviceName, deviceType, parameterList, constraintsList):
        device = PDK_skywater130_device(name=deviceName, deviceType = deviceType)
        device.createParameters(parameterList)
        device.createConstraints(constraintList)


#PDK_device class



class PDK_skywater130_device():

    def __init__(self, name, deviceType):
        self.name = name
        self.deviceType = deviceType

    def deviceSummary(self):
        print('** Device type = {}.  Device name = {}'.format(self.deviceType, self.name))

    def createParameters(self, parameterList):
        self.parameters = parameterList

    def createConstraints(self, constraintList):
        self.constraints= constraintList
