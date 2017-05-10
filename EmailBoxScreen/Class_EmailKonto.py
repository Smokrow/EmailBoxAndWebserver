import poplib
import email
import os.path
import smtplib
import time 
import socket

class EmailKontoBox(object):
    Account=""
    PW=""
    POP3=""
    Emails=[]
    Colors=[]
   
    
    def error_log(self,message):
        Data=open("errorlog.txt","a")
        t=time.strftime("%a, %d %b %Y %H:%M:%S ", time.gmtime())
        out=str(t)+"Error:"+message+"\n"
        Data.write(out)
        Data.close()
    def __init__(self,Account,PW,POP3):
        self.Account=Account
        self.PW=PW
        self.POP3=POP3
        self.error_log("Hallo")

    def Email_string_abrufen (self):
        try:
            #Login und checken der neuen Mails
            pop=poplib.POP3_SSL(self.POP3)
            pop.user(self.Account)
            pop.pass_(self.PW)
            Status=pop.stat()
            
    
            #Wenn keine neuen Mails da sind wird auch nichts geaendert geguckt
            if (Status[0]!= 0):
                #zieht immer die letzte Email und loescht den Rest
                Msg=pop.retr(1)[1]
                pop.dele(1)
                pop.quit()
                #speichert und decodiert diese Email ab
                Data =open("Emailpuffer.txt","w")
                Str=b"".join(Msg)
                for i in range(0,len(Msg)):
                    k=Msg[i].decode("utf8")
                    Data.write(k)
                    Data.write("\n")
                Data.close()
                #macht aus der Datei ein Emailobject
                Data =open("Emailpuffer.txt","r")
                mail=email.message_from_file(Data)
                Data.close()

                #Durchlaeuft die Mimestruktur und sucht den Payload wenn er "Text/plain" ist
                raw_message=b""
                for part in mail.walk():
                    if part.get_content_type() == 'text/plain':
                        raw_message=part.get_payload(decode=True) # prints the raw text
                #print("raw")
                #print(raw_message)
                #bearbeitete den String nach
                message_str=raw_message#.decode("utf8")
                #print("message_str")
                #print(message_str)
                message_list=message_str.split("\n")
                #print("message_list")
                #print(message_list)
                message_final=""
                for x in message_list:
                    if(x!=""):
                        message_final=message_final+x+" "

                raw_message=mail.get("From")
                Mailaddress=""
                ping=False
                for x in raw_message:
                    if(x==">"):
                        ping=False

                    if(ping==True):
                        Mailaddress=Mailaddress+x

                    if(x=="<"):
                        ping=True
            
            
                print(message_final)
                return [message_final,Mailaddress]
        
            else:
                pop.quit()
                message_final=""
                Mailaddress=""
                return [message_final,Mailaddress]
        except poplib.error_proto as detail:
            print("POP3 Protocol Error", detail)
            message_final = ""
            Mailaddress = ""
            return [message_final, Mailaddress]




    def save_to_file(self,Message,Sender,Zeit):
        #speichert die Nachricht in der Message.txt ab
        Data=open("Messages.txt","a")
        Message.strip("\n")
        x="%%%"+Message+"&&&"+Sender+"$$$"+str(Zeit)+"///"
        #print(x)
        Data.write(x) 
        Data.close()
        
    

    def update_message_file(self):
        #guckt ob neue Nachrichten anliegen und schreibt diese in die File.
        Message,Addresse=self.Email_string_abrufen()
        #print(Message)
        t=time.time()
        if((Message!=None)):
            if (Message!=""):
                if(Message!=' '):
                        self.save_to_file(Message,Addresse,t)
        

        
    def load_messages(self):
        #laedt die Nachrichten aus der Datei und liest diese in das Objekt ein.
        Data=open("Messages.txt","r")
        Data_list=Data.read()
        Data_list=Data_list
        Data_str=str(Data_list)
        Anzahl_Nachrichten=Data_list.count("%%%")
       
        Data_array=[]
        
        for x in range(0,Anzahl_Nachrichten):
            Message_begin=Data_str.find("%%%")
            Addresse_begin=Data_str.find("&&&")
            Time_begin=Data_str.find("$$$")
            Message_end=Data_str.find("///")
            Message=Data_str[Message_begin+3:Addresse_begin]
            Message=Message.splitlines()
            Message="".join(Message)


            
            Addresse=Data_str[Addresse_begin+3:Time_begin]
            Time=Data_str[Time_begin+3:Message_end]
            if(x!=Anzahl_Nachrichten-1):
                Data_str=Data_str[Message_end+3:len(Data_str)]
            Data_array.append([Message,Addresse,Time])
      
        
        self.Emails=Data_array
        
    def get_messages(self):
        #gibt das Message attribute wieder nachdem es geladen wurde.
        self.load_messages()
        return self.Emails

    def delete_old_messages(self):
        self.load_messages()
        for x in self.Emails:
            print(x)
            if((time.time()-float(x[2]))>216000.0):
                self.Emails.remove(x)
        Data=open("Messages.txt","w")
        Data.close()
        for x in self.Emails:
            self.save_to_file(x[0],x[1],x[2])

    def print_messages(self):
        for x in self.Emails:
            print(x)

    def get_colors(self):
        return self.Colors

    def set_colors(self,mx):
        self.Colors=x

    def load_colors(self):
        
        
        file=open("Colors.txt","r")
        Color_String=file.read()
        Color_list=Color_String.split("\n")
        Color_list.remove("")
        for x in range(0,len(Color_list)):
            temp=Color_list[x]
            temp=temp.split("=")
            
            temp[1]=temp[1].split(",")
            temp2=[temp[0],int(temp[1][0]),int(temp[1][1]),int(temp[1][2])]
            Color_list[x]=temp2   
        
        self.Colors=Color_list
    
                
            
    
    
        
                
           
