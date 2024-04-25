id = input("entrez votre pseudo")

mdp = input("entrez votre mot de passe")

taille_mdp = len(mdp)

if taille_mdp >= 6:
    print("bonne taille de mot de passe")

else:
    print("mot de passe trop court")