#Programma che usa un oggetto di WrapperDB
from ClasseWrapperDB import WrapperDB         

# CREO OGGETTO WRAPPER--------------------------------------------------------
#wrp = WrapperDB()
wrp = WrapperDB("213.140.22.237\\SQLEXPRESS", "CRD2122", "xxx123##", "CRD2122")

print()
print("\n***** TEST elencoPost *****")
print(wrp.elencoPost(as_dict = True))
print("*****************************")


print()
print("\n***** TEST singoloPost *****")
print(wrp.singoloPost(1))
print("******************************")


print()
print("\n***** TEST daiLikeAPost *****")
print("Prima:")
print(wrp.singoloPost(1))
wrp.daiLikeAPost(6)
print("Dopo:")
print(wrp.singoloPost(1))
print("*******************************")


print()
print("\n***** TEST inserisciPost *****")
parametri = ("ABUSOLDI", "piovono madonne!!!")
wrp.inserisciPost(parametri)
print(wrp.elencoPost(as_dict = True))
print("********************************")


#print()
#print("\n***** TEST eliminaPost *****")
#print("Prima:")
#print(wrp.elencoPost(as_dict = True))
#wrp.eliminaPost(3)
#print("Dopo:")
#print(wrp.elencoPost(as_dict = True))
#print("******************************")



print()
print("\n***** TEST elencoCommenti *****")
print(wrp.elencoCommenti())
print("*****************************")


print()
print("\n***** TEST singoloCommento *****")
print(wrp.singoloCommento(id))
print("******************************")

print()
print("\n***** TEST aggiungiCommenti *****")
parametri = (3,"ABUSAWED", "sì")
wrp.aggiungiCommenti(parametri)
print(wrp.elencoCommenti(as_dict = True))
print("********************************")
