


#Streamlit indlæses til senere brug
import streamlit as st




#DET KAN VÆRE SMART AT KIGGE NEDERST I KODEN FØRST DA DET ER DER HVOR ALLE INPUT HÅNDTERES, BARE SÅ DER IKKE ER FORVIRREN NÅ EKSEMPELVIS "tekst" NÆVNES


#Alfabet laves som liste så værdier kan hentes i krypering og dekryptering
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','æ','ø','å']


#BEGGE FORMER FOR KRYPTERING DEFINERES SOM FUNKTIONER TIL BRUG I INTERFACE

#--------------------------------------------------------------
#Kryptering

def krypter(tekst,nøgle):
   #Det er nok også smart lige at få styr på store/små bogstaver og mellemrum, Erstatter mellemrum med ingenting, det var lidt træls at finde ud af :(
 tekst=tekst.lower().replace(" ","")
 nøgle=nøgle.lower().replace(" ","")

 #Laver en variable string der kan tilføjes bogstavet til ved resultat print
 samlet_kryp=""

 for i in range(len(tekst)):
     tekst_print=tekst[i]
     ##print(i,alfabet.index(i))
     nøgle_kortere =nøgle[i%len(nøgle)] 

     tal_input=alfabet.index(tekst_print)
     tal_inputnøgle=alfabet.index(nøgle_kortere)
    
     tal_print=tal_input + tal_inputnøgle

     #Hvis tallet er større end listens sekvens, så fratrækkes tallet længden af listens værdier
     if tal_print>=len(alfabet):
         tal_print -= len(alfabet)
    
    #Finder det nye tals placering i alfabetet, og det ligges oveni krypteret tekst der skal bruges til at printe fulde tekst
     kryp_bogstav = alfabet[tal_print]
     samlet_kryp += kryp_bogstav
 return(samlet_kryp)




#------------------------------------------------------------------------------------------  
#Dekryptering:



#Mange af disse steps er gentagelser, referer evt. til krypteringen
def dekrypter(krypterettekst,nøgle):
    

 
    
    
    tekst=krypterettekst.lower().replace(" ","")
    nøgle=nøgle.lower().replace(" ","")

    #Laver en variable string der kan tilføjes bogstavet til ved resultat print
    samlet_dekryp=""

    for i in range(len(tekst)):
      tekst_print=tekst[i]
      ##print(i,alfabet.index(i))
      nøgle_kortere =nøgle[i%len(nøgle)] 

      tal_input=alfabet.index(tekst_print)
      tal_inputnøgle=alfabet.index(nøgle_kortere)
    
      tal_print=tal_input - tal_inputnøgle
 
     #Hvis tallet er mindre end 0 så tilføjes længden af alfabetet for at der ikke anvendes negative integers
      if tal_print<0 :
         tal_print += len(alfabet)
    
     #Finder det nye tals placering i alfabetet, og det ligges oveni krypteret tekst der skal bruges til at printe fulde tekst
      dekryp_bogstav = alfabet[tal_print]
      samlet_dekryp += dekryp_bogstav
    return samlet_dekryp





#Opsætning af streamlitinterface

st.title("(De)krypterings program med vigenere")

#Valg af funktion og nøgle

valg = st.selectbox("Vælg form",["Krypter","Dekrypter"])
nøgle = st.text_input("Skriv din nøgle her!")


if valg=="Krypter":
   tekst=st.text_area("Skriv din tekst til kryptering her")
    #Knap til at kryptere
   if st.button("Krypter"):
     resultat_krypt = krypter(tekst,nøgle)
        #F-string anvendes da det var det eneste jeg kunne få til at virke, antager at succes kommandoen måske kun vil have EN string
     st.success(f"Krypteret tekst: {resultat_krypt}")
elif valg=="Dekrypter":
   krypterettekst=st.text_area("Indtast din tekst der skal dekrypteres")
   if st.button("Dekrypter"):
      resultatet_dekrypt=dekrypter(krypterettekst,nøgle)
      #Samme som i krypter
      st.success(f"Dekrypteret tekst: {resultatet_dekrypt}")
