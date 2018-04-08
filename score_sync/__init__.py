import configparser
from shutil import copyfile
from urllib import request
import os



# Colors for terminal output. Makes things pretty. (Ripped from Propane)
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'
    CYAN = '\033[36m'


def start():

    # Establish relative path for config.ini and other operations
    dir = os.path.dirname(__file__) + "/"

    # Initialize the parser and set the config file
    config = configparser.RawConfigParser()

    configFile = config.read(dir + "config.ini")

    # Get config data
    clientMode = config.getboolean("General", "clientMode")

    serverMode = config.getboolean("General", "serverMode")

    serverOutDir = config.get("General", "serverOutDir")

    serverToConnect = config.get("General", "serverToConnect")

    if(clientMode or serverMode):
        # At least one mode is set, so let user know we are going to start syncing!
        print(bcolors.BLUE + bcolors.BOLD + "===Syncing scores===" + bcolors.ENDC)
    else:
        # Inform user they need to change configs first
        print(bcolors.FAIL + bcolors.BOLD + "Score Sync has not been configured as client or server!" + bcolors.ENDC)
        print(bcolors.FAIL + bcolors.BOLD + "Please check the config.ini in order to enable this PropAcc." + bcolors.ENDC)

    if(clientMode):
        print(bcolors.YELLOW + "Client is attempting to retrieve score from specified server..." + bcolors.ENDC)

        
        copyfile("propane_scores.txt", "/tmp/scores.bak")
        fileDidCopy = os.path.isfile("/tmp/scores.bak")


        if(fileDidCopy):
            try:
                copyfile("/dev/null", "propane_scores.txt")
                request.urlretrieve(serverToConnect + "scores", "propane_scores.txt")
                
                backUpExists = os.path.isfile("/tmp/scores.bak")
                
                if(backUpExists):
                    print(bcolors.YELLOW + "Cleaning up scores.bak from /tmp..." + bcolors.ENDC)
                    copyfile("/tmp/scores.bak", "propane_scores.txt")
                    os.remove("/tmp/scores.bak")
                    backUpExists = os.path.isfile("/tmp/scores.bak")

                    if(backUpExists):
                        print(bcolors.FAIL + "Failed to delete scores.bak from /tmp! Clean up was not successful..." + bcolors.ENDC)
                    else:
                        print(bcolors.GREEN + "Clean up successful!" + bcolors.ENDC)
                    print(bcolors.GREEN + bcolors.BOLD + "Score file retrieved, scores have been sync'd!" + bcolors.ENDC)

            except IOError:
            
                print(bcolors.FAIL + bcolors.BOLD + "Could not retrieve score file, check the config.ini to make sure the server is correct!" + bcolo$
            
                backUpExists = os.path.isfile("/tmp/scores.bak")
            
                if(backUpExists):
                    copyfile("/tmp/scores.bak", "propane_scores.txt")
                    os.remove("/tmp/scores.bak")
        else:

            print(bcolors.FAIL + bcolors.BOLD + "Could not create scores.bak in /tmp please review your config.ini and file permissions. Scores were $


    if(serverMode):
        print(bcolors.YELLOW + "Server is copying the score file to the specified directory..." + bcolors.ENDC)
       
        # Copy score to server output directory
        copyfile("propane_scores.txt", serverOutDir + "/scores")

        # Verify file copied
        fileDidCopy = os.path.isfile(serverOutDir + "/scores")
  
        if(fileDidCopy):
            print(bcolors.GREEN + bcolors.BOLD + "Score file succesfully copied to the directory '" + serverOutDir + "'!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + bcolors.BOLD + "Score file was not copied, please check config.ini to insure the settings are correct!" + bcolors.ENDC)
    # Nice little separator just for aesthetic
    print(bcolors.BLUE + bcolors.BOLD + "====================" + bcolors.ENDC)
