oui = "Vietnam"
print(oui[::])


def liste_octets(adresse):
    return [int(i) for i in adresse.split(".")]

print(liste_octets('192.168.0.1'))