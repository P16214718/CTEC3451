import csv
import sys
import os
import subprocess
import signal

# sudo apt-get install -y autopsy
# sudo apt install python3
# sudo apt install hdparm
while True:
	
	

        def main():
                
		#FUNCTION 1: LIST DEVICES
		def ListDevices ():
		        myCmd = 'lsblk' #lsblk is the linux command for listing devices
			os.system(myCmd) #This runs the terminal command specified above

		#FUNCTION 2: HDD SANITIZATION	
		def Sanitization ():
		     choiceB = raw_input(""" Please specify what HDD you would like to sanitize
			""")
		     myCmd2 = "sudo dd if=/dev/zero of=/dev/%s bs=1M " % (choiceB)
		     #print(myCmd2)
		     print("Sanitizing: ", choiceB) 
		     print(choiceB)
		     print( "Please be patient this may take a while")
		     os.system(myCmd2)
		     myCmdFormat = "sudo parted /dev/'{0}' --align opt mklabel msdos 0 4G ; sudo mkfs.exfat -n TargetHDD /dev/'{1}' " .format(choiceB, choiceB)
		     os.system(myCmdFormat)
		
		#FUNCTION3  - HDD IMAGING
		def Imaging ():
		     choiceC = raw_input(""" Please specify what HDD you would like to image
			""")
		     myCmdReadOnly = "sudo hdparm -r1 /dev/%s " %(choiceC)       
		     os.system(myCmdReadOnly)
		     myCmd3 = "sudo dd if=/dev/%s of=/media/user/TargetHDD/img.dd conv=notrunc " % (choiceC)
		     os.system(myCmd3)
		     print("HDD imaged to Target HDD directory")
		     
		    #HDD/IMAGE VERIFICATION
		     print ("Verification process will now begin")
		    
		     #Changed this to below: myCmd4 = "sudo sha1sum %s & sha1sum /dev/%s " % choiceD % choiceC
		     myCmdDIR = "cd /home/ ; cd /media/user/TargetHDD "
		     myCmd4 = "sudo sha1sum img.dd >> Hash-Verification.txt & sudo sha1sum /dev/%s >> Hash-Verification.txt " % (choiceC)
		     #This command will output both hash values of the image and evidence into a file called 'Hash-Verification.txt.'
		     os.system(myCmdDIR)
		     os.system(myCmd4)
		
		#FUNCTION4 - DELETED FILE RECOVERY
		def DeletedFileRecovery ():
		     choiceE = raw_input("""Specify which device you would like to recover files from:
		       """)
		        
		     print("List of deleted files: ")
		     # Autopsy (fls) Function to list the deleted files on the specifed device
		     # Prerequisite required - Autopsy Forensic software (TSK)
		     myCmd5 = "sudo fls -r -d -f fat32 /dev/%s " % (choiceE) 
		     print (myCmd5)
		    # myCmd4 = "sudo fls -o 135 -r /home/img.dd"
		     
             print ("Please click CTRL-C to continue")
		     os.system(myCmd5)
                     
                    # Add in my report that I changed it to an automatic CTRL-C after considering the user
		    # myCmd8 = "signal.SIGINT"
		    # os.system(myCmd8) 

			#FUNCTION5.2 - File recovery
		     DeletedFileNo = input("""Specify which files you want to recover by entering it's ID:
		       """)                         
		    #myCmd6 = "sudo icat -f fat32 /dev/%s %s > /home/user/Desktop/file.jpg " % (choiceE) , (DeletedFileNo)
                     myCmd6 = "sudo icat -f fat32 /dev/'{0}' , '{1}' > /home/user/Desktop/file.jpg " .format(choiceE, DeletedFileNo)
		     os.system(myCmd6)

		#FUNCTION5 - KEYWORD SEARCH
		def KeywordSearch ():
		     choiceF = raw_input("""Specify what you would like to search for on the device specified above:
		       """)
		    # myCmd7 = "sudo fls -r -d -f fat32 /dev/%s | grep %s" % (choiceE) , (choiceF)
		     os.system(myCmd7)
	
		 #MENU


		def menu():
		    
		    print("************Welcome to Ryan's Application**************")
		    print()

		choice = raw_input("""
				      A: List Devices
				      B: HDD Sanitization
				      C: HDD Imaging & Verification	
				      D: Recover Deleted files
				      E: Keyword Search
				      F: Exit

				      Please enter your choice: """)
		#FUNCTION 1: LIST DEVICES
		if  choice == "A" or choice == "a" :

		     ListDevices()

		#FUNCTION 2: HDD SANITIZATION
		elif choice == "B" or choice == "b":
		     
		     Sanitization()
			
		#FUNCTION3  - HDD IMAGING
		elif choice == "C" or choice == "c":
		     
		     Imaging()

		     
		 #FUNCTION4  - DELETED FILE RECOVERY
		elif choice =="D" or choice == "d":
		     #print("Ensure you are in the same directory as your 'img.dd' file")
		   
		     DeletedFileRecovery()
		       
		
		#FUNCTION5 - KEYWORD SEARCH
		elif choice =="E" or choice == "e":
		     
		     KeywordSearch()

		#FUNCTION6 - Exit
		elif choice=="F" or choice=="F":

		     sys.exit(0)
		         

		else:
		     print("You must only select either A or B")
		     print("Please try again")
		  
		menu()

	    

	main()
