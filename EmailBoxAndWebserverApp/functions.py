import poplib
import email
import time
from .models import Nachricht




def Email_string_abrufen():
    try:


        # Login und checken der neuen Mails
        pop = poplib.POP3_SSL('pop-mail.outlook.com')
        pop.user('pythontest1@outlook.de')
        pop.pass_("simpsons1")
        Status = pop.stat()

        # Wenn keine neuen Mails da sind wird auch nichts geaendert geguckt
        if (Status[0] != 0):
            # zieht immer die letzte Email und loescht den Rest
            #Msg = pop.retr(1)[1]

            raw_email = b"\n".join(pop.retr(1)[1])
            mail = email.message_from_bytes(raw_email)

            pop.dele(1)
            pop.quit()


            # Durchlaeuft die Mimestruktur und sucht den Payload wenn er "Text/plain" ist

            decoded_message = ''
            for part in mail.walk():

                charset = part.get_content_charset()
                if part.get_content_type() == 'text/plain':
                    part_str = part.get_payload(decode=1)
                    decoded_message += part_str.decode(charset)



            # bearbeitete den String nach
            message_str = decoded_message
            message_list = message_str.split("\n")
            message_final = ""
            for x in message_list:
                if (x != ""):
                    message_final = message_final + x + " "

            raw_message = mail.get("From")
            Mailaddress = ""
            ping = False
            for x in raw_message:
                if (x == ">"):
                    ping = False

                if (ping == True):
                    Mailaddress = Mailaddress + x

                if (x == "<"):
                    ping = True

            print(message_final)
            actual_Message = Nachricht(Nachricht_text=message_final, zeitstempel=float(time.time()), EmailAddresse=Mailaddress,
                                       Showen=True,
                                       zeitstring=time.strftime("%H:%M  %d %b %Y  ", time.gmtime()))
            if(actual_Message.Nachricht_text!=""):
                actual_Message.save()



    except poplib.error_proto as detail:
        print("POP3 Protocol Error", detail)
def Database_bereinigen():
    Message_List = Nachricht.objects.filter(Showen=True)
    for m in Message_List:
        x=m.zeitstempel
        y=float(time.time())
        if(y-x>3600):
            m.Showen=False
            m.save()
