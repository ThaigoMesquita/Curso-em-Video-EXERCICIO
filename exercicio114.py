import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('alguem comeu o podim')
else:
    print('pudim acessado')