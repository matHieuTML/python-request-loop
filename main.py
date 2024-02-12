import requests

# Dans des variables, on stocke les informations nécessaires la requête
url = "https://your-url.com/"
data = {
    'inputName': 'Votre Nom',
    'inputEmail': 'votre@email.com',
    'InputContent': 'Votre message ici'
}
files = {}
times = 20



#Ici on boucle sur une requete : POST 

#for _ in range(times):
   #response = requests.post(url, data=data, files=files)
    
    #if response.status_code == 200:
        #print("Message envoyé avec succès!")
    #else:
        #print(f"Erreur lors de l'envoi du message. Code de statut : {response.status_code}")
        #print(response.text)



#Ici on boucle sur une requete : GET 
for _ in range(times):
    response = requests.get(url)
    if response.status_code == 200:
        print("Connexion réussie")
    else:
        print(f"Erreur lors de l'envoi du message. Code de statut : {response.status_code}")
        print(response.text)