import urllib.request
for i in range(25,32):
    logo = urllib.request.urlopen("http://kadm.kmath.ru/files/alggeom{0}.pdf".format(i)).read()
    f = open("alg{0}.pdf".format(i), "wb")
    f.write(logo)
    f.close()
