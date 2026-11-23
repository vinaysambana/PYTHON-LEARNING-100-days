'''
#File handling --> open()

#File and Directory operations are essential to store the data
#Python provides built - in function -- open()

#mode of operations -- 'r','w','r+','w+'
#open(filename,mode) default mod 'r'

try:
    file = open('file.txt',"r")
    print(file)
    #print(file.read()) #reads the entire content
    #print(file.readline()) #reads a single line
    print(file.readlines()) #read all lines into a list
except Exception as e:
    print(e)

f = open('Testing_File_for File-Handling.txt')
print(f)
f = open('Testing_File_for File-Handling.txt')
print(f.read())
f.close()

#Best practice is we will use with statement
with open('Testing_File_for File-Handling.txt','r') as file:
    print(file.read())

#writing to a File
#'w' mode will create a new file if not existing,else if already exists
#it will override the content
g = open('Testing_File_for File-Handling.txt','w')
print(g)
g.write("Saketh")
g.close()

h = open("testing_file_2","w")
h.write("PFS-VSP-007 is good but Some times Mischevious")
h.write("\n They make it as gang")
logs = ['\nFirst ID','\tVinay','\tAjay']
#h.write(logs) #it needs only text
h.writelines(logs) #writelines(iterable)---> writes an iterable of
#stings(such as list or tuple)
h.close()
print("Done")


statements = ['\nHello World ! WELCOME to Python Full Stack at "CODEGNAN"',
        '\n"PFS-VSP-007" batch Python Trainer is "SAKETH KALEPU SIR"(Co-Founder)']
with open("testing_file_3","w") as file:
    file.writelines(statements)
    #print(file.read()) # I/O Error

#when we use with block,we need not use close()


#Appending to a file ---> if file is already existing no change u can add the
#content,if not new file will be created
with open('testing_file_2','a') as file:
    file.write("\n Students need to finish last week AI Mock Interview")
    file.writelines(["\n Vijay","\t Kaushik","\t Vinay",
                     "\n always chatting"])
    #print(file.read())
    

#Use Case : Logging System
def log_activity(activity):
    """User Logs to be Stored"""
    try:
        with open('log.txt','a') as log_file:
            log_file.write(activity+'\n')
            log_file.read() #it wil get into except block
    except Exception as e:
        print("Error is",e)
    finally:
        print("File Handling is Imortant")
log_activity("Vinay Logged in for AI Mock Interviwe....")
log_activity("Vinay is Testing his Microphone and Camera")
log_activity("Vinay started his AI Mock Interview")
log_activity("Vinay is Writing the Code")
log_activity("Vinay has finished His AI Mock Interview and report has Created")
'''

#r+ ---> read and write ---> Preserves the existing content(data),
#new writes overwrite the characters from the start of the cursor...

'''
with open('Testing_File_for File-Handling.txt','r+') as file:
    file.write("Testing phase")
    print(file.read())


with open('log.txt','r+') as log_file:
    print(log_file.read())
    log_file.write("End of Class")

#Now we will perform write first then read later

with open('log.txt','r+') as log_file:
    log_file.write("PFS-VSP-007")
    print(log_file.read())
#in above case we are performing write first content is overwritten
#from the start of the cursor and when u read it remaining content will
#be shown
#Use Case: Modifying or Updating parts of an exisiting file
'''

#read(): Used to read data from a file.
#write(): Used to write data into a file.

#read() ---> write() ---> reads the entire file and override the file
#write() ---> read() ---> write the entered string into a file by removing
#the already exsiting content in it upto entered "len(str)" and reads the file 











































































