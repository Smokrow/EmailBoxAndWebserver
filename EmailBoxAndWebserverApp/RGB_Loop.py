from .Function_RGB import Class_EmailKonto
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import socket
import poplib
from rgbmatrix import Adafruit_RGBmatrix


def draw_Message(message, Color1, Color2):
    text_width, text_height = fnt.getsize(message)
    img = Image.new('RGBA', (text_width + 10, 16), Color2)
    draw = ImageDraw.Draw(img)
    draw.text((5, (16 - text_height) / 2), message, Color1, font=fnt)
    for n in range(32, -img.size[0], -1):
        matrix.Clear()
        matrix.SetImage(img.im.id, n, 0)
        time.sleep(0.05)


# festlegen der Gesamten Grund

Konto = Class_EmailKonto.EmailKontoBox('pythontest1@outlook.de', 'simpsons1', 'pop-mail.outlook.com')
Konto.load_colors()
Konto.load_messages()
Konto.error_log("Hi")

matrix = Adafruit_RGBmatrix(16, 1)
fnt = ImageFont.truetype("Ticketing.ttf", 14)
random.seed()
Colors = ((255, 0, 0, 0),
          (0, 255, 0, 0),
          (0, 0, 255, 0),
          (255, 255, 0, 0),
          (0, 255, 255, 0),
          (255, 0, 255, 0),
          (255, 255, 255, 0))

draw_Message("Willkommen", (255, 255, 255), (0, 0, 0))

Konto.error_log("draw Welcome error")
t = time.time()
Konto.load_messages()
Konto.update_message_file()
Konto.delete_old_messages()
Konto.load_messages()

while True:

    try:

        if time.time() - t > 120.0:
            Konto.update_message_file()
            Konto.delete_old_messages()
            Konto.load_messages()


        Emails = Konto.get_messages()
        spec_color = Konto.get_colors()
        final_Message = []
        if (Emails == []):
            draw_Message("Keine Nachrichten", (255, 0, 0), (0, 0, 0))
        else:
            for x in Emails:
                Message = x[0]
                Color = Colors[random.randint(0, len(Colors) - 1)]
                Addresse = x[1]

                for y in spec_color:
                    if (y[0] == Addresse):
                        Color = (y[1], y[2], y[3])
                draw_Message(Message.decode("utf-8"), Color, (0, 0, 0))
    except socket.error as error1:
        time.sleep(10)
        print("Socket error")
        Konto.error_log("Socket error")
    except TypeError as error1:
        draw_Message("Probleme mit der E-Mail Verbindung. Bitte die Emailadresse checken", (255, 0, 0), (0, 0, 0))
        print("Little Problem here")










