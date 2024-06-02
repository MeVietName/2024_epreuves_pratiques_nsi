class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    # def est_reservee(self):
    #     """renvoie True si l'adresse IP est une adresse
    #     réservée, False sinon"""
    #     reservees = ["193.168.0.0", "192.168.0.255" ] 
    #     return self.adresse in reservees
    
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = [ '192.168.0.0', '192,168.0,255' ] 
        return self.adresse in reservees 

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets()
        if octets[3] == 254: 
            return None
        octet_nouveau = octets[3] + 1
        return AdresseIP('192.168.0.' + str(octet_nouveau))
    
adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0') 

# adresse1 = AdresseIP("192.168.0.1")
# adresse2 = AdresseIP("192.168.0.2")
# adresse3 = AdresseIP("192.168.0.0")

# [192, 168, 0, 1]
print(adresse1.liste_octets())

# False
print(adresse1.est_reservee())

# True
print(adresse3.est_reservee())

# ici car on sait que l'adresse suivante existe '192.168.0.3'
print(adresse2.adresse_suivante().adresse) # acces valide à adresse