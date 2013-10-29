#!/usr/bin/python

#######################################################################
####################         IP Scrape          #######################
#######################################################################

#######################################################################
#######################     Configuration     #########################
#######################################################################
##								    
##	N.B Currently uses gmail, modify server settings to suit    
##								    
##	Enter email details. Look for comments 			    
##	(Plain text password :o shock horror)			    
##								    
##	Create blank current_ip.txt in same directory as script	    
##								    
##	Configure error log printing if desired			    
##								    
##	Set up cron job if desired				    
##								    
######################################################################


import smtplib
import os
from subprocess import Popen, PIPE  
  
process = Popen(["wget http://ipecho.net/plain -O - -q ; echo"], stdout=PIPE, shell=True)
(output, err) = process.communicate()
exit_code=process.wait()

if err is None:

	with open('current_ip.txt', 'r+') as file:
		current_ip = file.read()
		new_ip = (current_ip != output)
		if(new_ip):
			file.seek(0)
			file.write(output)
			file.truncate()
	file.closed




	if(new_ip):
		fromaddr = 'IP BOT <IP_BOT@RPI>' 
		toaddr  = ##### email address to notify ####
		msg = 'External IP change detected. \n\nNew IP: %s\n\n\nIP BOT' % (output)
		subj = 'External IP change: %s' % (output)  
		message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (fromaddr, toaddr, subj, msg)  
		username = #### email username ####  
		password = #### email password ####

		try:    
			server = smtplib.SMTP('smtp.gmail.com:587')  
			server.starttls()  
			server.login(username,password)  
			server.sendmail(fromaddr, toaddr, message)  
			server.quit()
		except SMTPException:
			print "Error" #add error log check if desired

