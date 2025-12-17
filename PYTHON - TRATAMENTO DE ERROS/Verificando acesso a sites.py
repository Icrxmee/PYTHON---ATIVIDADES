import urllib
import urllib.request

try: 
    site = urllib.request.urlopen('https://www.pudim.com.br')

except:
    print("Site não encontrado ou sem acesso.")

else:

    print("TUDO OK")