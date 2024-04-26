import pickle
import stock_vbucks


def add(id, mdp):
    try:
        #lis fichier mdp
        file = open('save', 'rb')
        sauvegarde = pickle.load(file)
        file.close()
    except:
        sauvegarde = {}

    #ajoute nouveau mdp + id
    sauvegarde[id] = mdp

    #ecris fichier mdp
    file = open('save', 'wb')
    pickle.dump(sauvegarde, file)
    file.close()


def compare(mdp, mdprecu):
    if mdprecu == mdp:
        compte = stock_vbucks.Compte(id=mdp)
        return
    print("le mot de passe est incorrect")


def connect(idrecu, mdprecu):
    try:
        file = open('save', 'rb')
        sauvegarde = pickle.load(file)
        file.close()

        if idrecu in sauvegarde.keys():
            compare(sauvegarde[idrecu], mdprecu)
        else:
            print("l'identifiant est incorrect")
    except:
        pass
