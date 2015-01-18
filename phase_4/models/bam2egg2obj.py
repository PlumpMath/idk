import subprocess
import os

directory = ''
debug = False

bam_models_list = []
egg_models_list = []

commands = '''\nFollowing commands are available:

    debug - enables debug
    setDir - allows you to set working directory for converter  
    bam2egg - converts all .bam files to .egg in specified directory
    egg2obj - converts all .egg files to .obj in specified directory
    bam2obj - converts all .bam to .egg and then those to .obj
    exit - quits the program
'''

def setDir():
        global directory
        new_dir = raw_input("\n enter new dir> ")
        directory = new_dir

def bam2obj():
    bam2egg(bam_models_list)
    egg2obj(egg_models_list)
    
    
def bam2egg(bam_models_list):
    for filename in os.listdir(str(directory)):
        if filename.endswith('.bam'):
            bam_models_list.append(filename)
    
    if debug == True:
        print bam_models_list   
    
    for model_name in bam_models_list:
        try:

            if debug == True:       
                print 'Working on: ' + model_name
            
            infile = directory + '\\' + model_name
            outfile = directory + '\\' + model_name + '.egg'

            return_code = subprocess.check_output(['bam2egg', infile, outfile])

            if debug == True:
                print return_code

        except:
            print 'error'
            return 1
            
def egg2obj(egg_models_list):
    
    for filename in os.listdir(directory):
        if filename.endswith('.egg'):
            egg_models_list.append(filename)

    if debug == True:
        print egg_models_list
    
    for model_name in egg_models_list:
        try:
            if debug == True:
                print 'Working on: ' + model_name
            
            infile = directory + '\\' + model_name
            outfile = directory + '\\' + model_name + '.obj'

            return_code = subprocess.check_output(['egg2obj', infile, outfile])
            if debug == True:
                print return_code

        except:
            print 'error'
            return 1
                
print "\ntype 'help' for options or 'exit' to quit "
print "Before you start you need to set working dir by using 'setDir'"

while True:
    user_input = raw_input("\n> ")
    
    if len(user_input) != 0:
        
        if user_input == "help":
            print commands

        if user_input == "bam2egg":
            bam2egg(bam_models_list)
            
        if user_input == "egg2obj":
            egg2obj(egg_models_list)
            
        if user_input == "setDir":
            setDir()
            
        if user_input == "debug":
            debug = True
            print 'debug mode on'
               
        if user_input == "bam2obj":
            bam2obj()
         
        if user_input == "exit":
            break
    else:
        break
