from django.shortcuts import render
from django.template import loader,RequestContext,Context
from django.http import HttpResponse
from time import gmtime,strftime
from datetime import datetime
from .forms import MessageForm
from .models import Nachricht
import subprocess
import os

def main_page(request):
    t = loader.get_template("Home.html")
    return HttpResponse(t.render())

def update_Database():
    Data = open("C:\\Users\\Moritz\\PycharmProjects\\untitled3\\EmailBoxWebserver\\Messages.txt", "r")
    Data_list = Data.read()
    Data_str = str(Data_list)
    Anzahl_Nachrichten = Data_list.count("%%%")
    Message_list = []
    Addresse_list = []
    Timestamp_list = []

    DataBase=Nachricht.objects.all()
    for m in DataBase:
        m.Showen=False
        m.save()

    for x in range(0, Anzahl_Nachrichten):
        Message_begin = Data_str.find("%%%")
        Addresse_begin = Data_str.find("&&&")
        Time_begin = Data_str.find("$$$")
        Message_end = Data_str.find("///")
        Message = Data_str[Message_begin + 3:Addresse_begin]
        Message = Message.splitlines()
        Message = "".join(Message)

        Addresse = Data_str[Addresse_begin + 3:Time_begin]
        Time_new = Data_str[Time_begin + 3:Message_end]
        if (x != Anzahl_Nachrichten - 1):
            Data_str = Data_str[Message_end + 3:len(Data_str)]
        Message = Message.encode("utf-8")
        Message_list.append(Message)
        Addresse_list.append(Addresse)
        Timestamp_list.append(strftime("%H:%M  %d %b %Y  ", gmtime(int(float(Time_new)))))

        actual_Message=Nachricht( Nachricht_text=Message,zeitstempel=float(Time_new),EmailAddresse=Addresse,Showen=True,zeitstring=strftime("%H:%M  %d %b %Y  ", gmtime(int(float(Time_new)))))

        if Nachricht.objects.filter(zeitstempel= Time_new):

            m=Nachricht.objects.get(zeitstempel=float(Time_new))
            m.Showen=True
            m.save()

        else:
            actual_Message.save()

def rewrite_Database():
    Message_List = Nachricht.objects.filter(Showen=True)
    Data = open("C:\\Users\\Moritz\\PycharmProjects\\untitled3\\EmailBoxWebserver\\Messages.txt", "w")

    for m in Message_List:
        Message=m.Nachricht_text
        Sender=m.EmailAddresse
        Zeit=m.zeitstempel
        x = "%%%" + Message + "&&&" + Sender + "$$$" + str(Zeit) + "///"
        Data.write(x)
    Data.flush()
    Data.close()


def Colors(request):
    color_list=100
    context = RequestContext(request, {"color_list": color_list})
    t = loader.get_template("Colors.html")
    return HttpResponse(t.render(context))

def Errorlogfunc(request):
    error_list=100
    context = RequestContext(request, {"error_list": error_list})
    t = loader.get_template("Errorlog.html")
    return HttpResponse(t.render(context))

def Messages_HTML(request):


    if request.method == 'GET':
        meldung_checked=True
        update_Database()

        Message_List=Nachricht.objects.filter(Showen=True)
        Form_List=[]
        for m in Message_List:
            temp=MessageForm(instance = m)
            Form_List.append((temp))


        context=RequestContext(request, {"message_active": meldung_checked,"message_list": Message_List })
        t = loader.get_template("Messages.html")
        return HttpResponse(t.render(context))

def Delete_Message(request,id):
    meldung_checked=True
    print(id)
    m=Nachricht.objects.get(pk=id)
    m.Showen=False
    m.save()
    rewrite_Database()
    Message_List = Nachricht.objects.filter(Showen=True)
    context = RequestContext(request, {"message_active": meldung_checked, "message_list": Message_List})
    t = loader.get_template("Messages.html")
    update_Database()
    return HttpResponse(t.render(context))

def reboot(request):
    t = loader.get_template("Reboot.html")
    os.system("sudo shutdown -r now")
    return HttpResponse()

def shutdown(request):

    t = loader.get_template("Reboot.html")
    os.system("sudo shutdown -h now")
    return HttpResponse()
