import pickle

def add(id, mdp):
    print("")

    file = open('save', 'wb')
    sauvegarde = [
                id,
                mdp,
            ]
    pickle.dump(sauvegarde, file)
    file.close()

def connect(idr, mdpr):
    try:
        file = open('save', 'rb')
        sauvegarde = pickle.load(file)
        id = sauvegarde[0]
        mdp = sauvegarde[1]
        file.close()
        compar(idr, mdpr,  id, mdp)
    except:
        pass

def compar(idr, mdpr, id, mdp):
    if "idr" == "id":
        if "mdpr" == "mdp":
            print("vous êtes connecter")
        else:
            print("le mot de passe n'est pas bon")
    else:
        print("l'identifiant n'est pas bon")
