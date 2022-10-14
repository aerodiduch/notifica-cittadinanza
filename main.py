import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import re
import smtplib
from email.message import EmailMessage

######### Modificame chango
sender_mail = 'aerodiduch@gmail.com' # tu email, ejemplo nombre@sujeto.com
sender_passwd = 'passwd' # esto se supone que te lo explique por whatsapp
lista_correos = ["receptor1@servicio1.com","receptor2@servicio2.com","receptor3@servicio3.com"] # aca van la lista de recibidores en el formato "email@receptor.com", "email2@receptor2.com" etc
########################

def mandar_mail(mensaje, url):
    try:
        for correo in lista_correos:
            msg = EmailMessage()
            
            cuerpo_email = '''
            COINCIDENCIA ENCONTRADA:
            {} 
            
            {}
            '''.format(mensaje, url)
            
            msg.set_content(cuerpo_email) 
            msg['Subject'] = "[AVISO] RECONSTRUCCIÓN DE CIUDADANIA" #o whatever que quieras que sea la 
            msg['From'] = sender_mail #aca es tu correo
            msg['To'] = correo #cada correo de los que esten en lista_correo

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_mail, sender_passwd)
            server.send_message(msg)
            server.quit()
    except:
        pass

base_url = 'https://consbuenosaires.esteri.it'
url = 'https://consbuenosaires.esteri.it/consolato_buenosaires/it/la_comunicazione/dal_consolato'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links_avisos = []
descripcion_tabla = soup.find_all('td', {"class":"desc_lista"})

for elemento in descripcion_tabla:
    coso = elemento.find("a")["href"]
    links_avisos.append(coso)

mensaje_limpio = [mensaje.get_text() for mensaje in descripcion_tabla]
info_conjunta = dict(zip(mensaje_limpio, links_avisos))


for mensaje in info_conjunta.keys():
    coincidencia = re.search("(TURNI CITTADINANZA)|(RICOSTRUZIONE)|(CIUDADANÍA)|(CIUDADANIA)|(RECONSTRUCCIÓN)|(RECONSTRUCCIÓN)|(CITTADINANZA)|(AVVISO)", mensaje, flags=re.I)
    if coincidencia:
        url = base_url + info_conjunta[mensaje]
        mandar_mail(mensaje, url)






