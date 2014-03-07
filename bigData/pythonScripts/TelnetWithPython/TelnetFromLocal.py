import telnetlib
import getpass

class TelnetConnection():
    C_RETURN = "\n"
    DEBUG_LEVEL = 0

    def __init__(self, hostname="localhost", username=None, password=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.telDescriptor = None

    def telnetConnAndLoginCommandList(self, commandList):
        try:
            self.telDescriptor = telnetlib.Telnet(self.hostname)
            self.telDescriptor.set_debuglevel(self.DEBUG_LEVEL)
            print self.telDescriptor.read_until("login: ")
            self.telDescriptor.write(self.username + self.C_RETURN)
            if self.password:
                print self.telDescriptor.read_until("Password: ")
                self.telDescriptor.write(self.password + self.C_RETURN)

            for commands in commandList:
                self.telDescriptor.write(commands + self.C_RETURN)
            self.telDescriptor.write("exit" + self.C_RETURN)
            data = self.telDescriptor.read_all()

        except:
            return "ERROR"
        return data


    def telnetConnAndLoginSingleCommand(self, command):
        try:
            self.telDescriptor = telnetlib.Telnet(self.hostname)
            self.telDescriptor.set_debuglevel(self.DEBUG_LEVEL)
            print self.telDescriptor.read_until("login: ")
            self.telDescriptor.write(self.username + self.C_RETURN)
            if self.password:
                print self.telDescriptor.read_until("Password: ")
                self.telDescriptor.write(self.password + self.C_RETURN)
            command = command + self.C_RETURN
            self.telDescriptor.write(command)
            data = self.telDescriptor.read_eager()
        except:
            return "ERROR"
        return data


    def telnetConnAndLogin(self):
        try:
            self.telDescriptor = telnetlib.Telnet(self.hostname)
            self.telDescriptor.set_debuglevel(self.DEBUG_LEVEL)
            print self.telDescriptor.read_until("login: ")
            self.telDescriptor.write(self.username + self.C_RETURN)
            if self.password:
                print self.telDescriptor.read_until("Password: ")
                self.telDescriptor.write(self.password + self.C_RETURN)
        except:
            print "ERROR"

    def telnetExeSingleCommand(self, command):
        self.telDescriptor.write(command + self.C_RETURN)
        returnData = self.telDescriptor.read_eager()
        print returnData
        return returnData


    def telnetConnAndLoginReadEagerCommand(self, commandList):
        try:
            self.telDescriptor = telnetlib.Telnet(self.hostname)
            self.telDescriptor.set_debuglevel(self.DEBUG_LEVEL)
            print self.telDescriptor.read_until("login: ")
            self.telDescriptor.write(self.username + self.C_RETURN)
            if self.password:
                print self.telDescriptor.read_until("Password: ")
                self.telDescriptor.write(self.password + self.C_RETURN)

            for commands in commandList:
                self.telDescriptor.write(commands + self.C_RETURN)
                readingEagerly = self.telDescriptor.read_eager()
                print readingEagerly

            self.telDescriptor.write("exit" + self.C_RETURN)

            data = self.telDescriptor.read_all()
        except:
            return "ERROR"
        return data


    def telnetClose(self):
        self.telDescriptor.close()

tn = TelnetConnection("localhost","ahmed","Ahmed@123")
commandList = ["ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date",
               "ls", "ls -l", "ps", "ls -a", "who", "whoami", "uname -a", "uname -n", "date"]

#tn.telnetConnAndLogin()
#for command in commandList:
#    print tn.telnetExeSingleCommand(command)


fileOperation = open('CommandOutputFile.txt','w+')
item = tn.telnetConnAndLoginReadEagerCommand(commandList)
fileOperation.write(item)

data = tn.telnetConnAndLoginCommandList(commandList)
print(data)
fileOperation.write(data)


fileOperation.close()
tn.telnetClose()


'''

HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

telnetConnection = telnetlib.Telnet(HOST)
telnetConnection.read_until("login: ")
telnetConnection.write(user+"\n")
if password:
    telnetConnection.read_until("Password: ")
    telnetConnection.write(password+"\n")

telnetConnection.write("ls\n")
telnetConnection.write("ls -l\n")
telnetConnection.write("exit\n")
print telnetConnection.read_all()

'''
'''
HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()
'''

