#!/usr/bin/env python3
"""
__author__  = "Blaze Sanders"
__email__   = "blaze.d.a.sanders@gmail.com"
__company__ = "Robotic Beverage Technologies, Inc"
__status__  = "Development"
__date__    = "Late Updated: 2020-07-08"
__doc__     = "Class to define OTA commuications architecture for 30K+ Tapomatic kiosk"
"""

# Allow program to create GMT and local timestamps
from time import gmtime, strftime

# Allow program to READ Comma Separated Value files
import csv 

LOW_LIQUID_MESSAGE = 0
PHYSICAL_DAMAGE_MESSAGE = 1
LOW_POWER_MESSAGE = 2
DULL_KNIFE_MESSAGE = 3
VERISON_MESSAGE = 4

# Power CONSTANTS
ON = 1
OFF = 0


class MissionControl():	

	totalCoconutsVended = 0
	totalTapsUsed = 0
	totalFlavorOzUsed = 0
	totalHealthOzUsed = 0
	totalCoirFiberRemoved = 0
	currentHealthPercentage = 100.0
	
	def __init__(self, kioskID, version, key):
		"""
		
		Key arguments:
		kioskID -- Unique ID for every prototype or production Tapomatic manufactured
		version -- Verison on software that should be running on a Tapomatic
		key -- Security key for ALL Tapoamtics to allow Over-The-Air (OTA) updates
		
		Return value:
		New MissionControl() object
		"""
		
		currentProgramFilename = os.path.basename(__file__)
		self.DebugObject = Debug(True, currentProgramFilename)
		
		self.kioskID = kioskID    
		self.version = version
		self.key = key 
		
		
	def ReportLiquidLevel(self, lType, internalBottleLocation, kioskID):
	    """
	    Report the current liquid level as percentage 
    	
    	Key arguments:
        lType -- Type of liquid add-on to inject into thr coconut
        internalBottleLocation -- Position starting with 0 that a bottle is from the left side of kiosk as you move right
        kioskID -- Unique ID for every prototype or production Tapomatic manufactured

    	Return value:
    	liqPercentage -- Percent that a 750 mL botle is full
    	"""
    		
	    return liqPercentage
	    
	
	
	def ReportLowLiquidLevel(self, lType, internalBottleLocation, kioskID):
	    """
	    High priority alert that the current liquid level is below 20%
	    
	    Key arguments:
	    lType -- Type of liquid add-on to inject into the coconut
	    internalBottleLocation -- Position starting with 0 that a bottle is from the left side of kiosk as you move right
	    kioskID -- Unique ID for every prototype or production Tapomatic manufactured
	    
	    Return value:
	    liqPercentage -- Percent (less then 20%) that a 750 mL botle is full
	    """
	    
	    return liqPercentage
    
    
	
	def GetKioskGPSlocation(self, kioskID):
	    """
	    Determine the GPS location using celluar towers (not a GPS satilite receiver) or a hard coded value in non-volitile memory 
	    Update to RavenDB Implemention in August 20200
	    
	    Key arguments:
	    kioskID -- Unique ID for every prototype or production Tapomatic manufactured
	    
	    Return value:
	    gpsData -- Lattitude, Longitude, and Altitude data
	    """
	    
	    
	    # Hard coded locations that have TERRIBLE cell service 
	    try:
	        f = open(kioskLocation.csv, 'rb')  # open only in read mode.
	        data = f.read(DATA_BUFFER_SIZE) # Read for Buffer Size.
	    except:
	        this.DebugObject.Dprint("Could not open {}, ensure the filepath is correct.")
	        
	    print("TODO RavenDB or TextFile?")
    	
    

	def GetKioskLocationName(self, kioskID):
	    """
	    
	    
	    Key arguments:
	    kioskID -- Unique ID for every prototype or production Tapomatic manufactured
	    
	    Return value:
	    locationName -- Human readable String variable describing the location
	    """
	    
	    #Read CVS and take 2nd entry (0, Vinny's Home, 2728 Brookstone Court Las Vegas NV 89117, 36.1416584, -115.2958079;)
	    return locationName
    	
    	
	
	def ReportHealthPercentage(self):
	    """
    	
    	
    	Key arguments:
    	
    	Return value:
    	
    	"""
    		
	    return currentHealthPercentage
    	
		
	
	def ReportPowerState(self):
	
	    return 1
	    	
	def ReportTapUsage(self):
	    """
	    
	    
	    Return value:
	    totalTapsUsed -- Total number of CoirTek taps removed from tap ring since last count. Power cycling machine should NOT reset this variable.
	    """
	    
	    return totalTapsUsed
	
		
	def ReportCoconutUsage(self):
	    """
	    
	    Return value:
	    totalCoconutsUsed -- Total number coconuts tapped since last count. Power cycling machine should NOT reset this variable.
	    """
	    
	    return totalCoconutsUsed
  
	
	def ReportKnifeStatus(self):
	    """
	    TODO REMOVE in v2020.1
	    
	    Return value:
	    sharpness -- Interger, from 0 to MAX_CUTTING_SURFACES 
        """
        	
	    return -1    
        	
	
	def ConnectToDSDservive(self, serviceName):
	    """
	    Rob's sale CRM and accounting sysytem EDI 944 https://www.jobisez.com/edi/tp/guide.aspx?doc=/edi-igs/3m/Wins-944-3060.pdf

	    Key arguments:
	    serviceName -- String, 
	    
	    Return value:
	    status -- Interger, HTML error code
	    """
		
	def SetEDI944(self):
	    """
	    
	    """
	    
	    return -1

	
	def GetEDI944(self):
	    """
	    
	    """
	    
	    return -1

	
	def StartOTA(self, verison):
	    """
	    Update kiosk to version specified or newish version if invalid version number is given
	    
	    Key arguments:
		version -- Verison on software that should be running on a Tapomatic
		
		Return value:
		??? --	    
	    """
	    
	    if(verison > 2020.0):
	        self.DebugObject.Dprint("Tracking your IP address, this in not public code :)")
	    elif(version == 2020.0):
	        #OLD Tapomatic CodeBase FilePath
	        oldFilepath = "~/Tapomatic/v" + version
	        #NEW Tapomatic CodeBase FilePath
	        newVersion = version + 0.1
	        check_call("mkdir newVersion", shell=True)
	        newFilepath = "~/Tapomatic/v" + version
	        check_call("cd newVersion", shell=True)
	        
	        #TODO Start downloading code with wget or CURL
	        # https://curl.haxx.se/docs/manpage.html
	        # https://stackoverflow.com/questions/15034471/using-git-and-curl-command-line
	        # curl https://github.com/ROBO-BEV/Tapomatic        
	        
	        check_call("wget https://github.com/ROBO-BEV/Tapomatic/tree/master/v2020.1", shell=True) 
	        #url = "https://github.com/ROBO-BEV/Tapomatic/tree/master/" + newVersion       
            #wget url
	    
	    elif(verison < 2020.0):
	        self.DebugObject.Dprint("This is old code that ia on longer supported on this hardware.")	    
	    else:
	        self.DebugObject.Dprint("Invalid version number updating to v2020.0")
		
    	
	def StopOTA(self):
	    """
	    
	    Key arguments:
	    
	    Return value:
	    
	    """
	    
	    return -1

	
	def UnitTest():
	    """
	    Test object creatation and .key file reading
	    
	    Return value:
	    DEBUG.OK if all tests pass
	      
	    """
	    
	    print("START MissionControl.py UnitTest()")
	    
	    try:
	        filename = ".key"
	        f = open(filename, 'rb')            # Open only in read mode.
	        data = f.read(DATA_BUFFER_SIZE)     # Read for Buffer Size.	    
	    except:
	        this.DebugObject.Dprint("Could not open {}, ensure the filepath is correct.")
	    
	    	    
	    prototypeKioskID = 0                                                                                                                        	    
	    GoodMissionControlObject = MissionControl(prototypeKioskID, 2020.0, f)
	    GoodMissionControlObject.ReportLiquidLevel(CocoDrink.ORANGE_FLAVOR, 0, prototypeKioskID)
	    
	    #BadMissionControlObject = MissionControl(1, 2020.2, ".key")
	    
	    print("END UnitTest()")	    
	    
	    return DEBUG.OK


if __name__ == "__main__":

    try:
        passedTest = MissionControl.UnitTest()    
    except NameError:
        print("UnitTest() failed - Have a nice day :)")
    
    print("END MissionControl.py MAIN")
