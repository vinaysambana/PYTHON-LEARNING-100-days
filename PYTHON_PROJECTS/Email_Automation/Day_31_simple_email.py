'''
Email Automation Using Python ---> Set up Gmail App Password (2-step Verification ON)
---> We create a project specific Password

we will be using SMTP Library(Simple Mail Transfer Protocol)
'''
import smtplib
#Now we need to connect to the server ---> Gmail
server = smtplib.SMTP("smtp.gmail.com",587)
print(server)
#Start the connection
server.starttls()
#give your login Credentials
server.login("vinaysambana1@gmail.com","lcqt edia vsfo djbn")
print("Success")
#give your desired message
message = "This is the First mail sent using Python"
server.sendmail("vinaysambana1@gmail.com","sambanasailaja@gmail.com",message)
server.close()
print("Mail Sent")































