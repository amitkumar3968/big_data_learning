import telnetlib
import getpass
import  time

HOST = "localhost"
user = "ahmed"
password = "Ahmed@123"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")


#tn.write("sudo su"+"\n")
#tn.write("ls -l"+"\n")
#data = ''
#while data.find('#') == -1:
#    data = tn.read_very_eager()
#print data

try:
    tn.write("cdc; ls -l\r\n")
except:
    print("Error")
time.sleep(1)
print tn.read_eager()
#tn.write("ls -a\r\n")
#time.sleep(1)
#print tn.read_very_eager()

tn.write("exit\r\n")

sess_op = tn.read_all()
#print sess_op