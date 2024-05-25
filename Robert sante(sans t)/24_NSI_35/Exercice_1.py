def annee_temperature_minimale(moyenne, ans)-> list:
    max_mo = min(moyenne)
    ou = moyenne.index(max_mo)
    quand = ans[ou]
    return (max_mo, quand)
    
    
    
    
# (12.5, 2016)
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(annee_temperature_minimale(t_moy, annees))
