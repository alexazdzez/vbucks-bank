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


def connect(idrecu, mdprecu):
    try:
        file = open('save', 'rb')
        sauvegarde = pickle.load(file)
        file.close()

        if idrecu in sauvegarde.keys():
            compare(mdprecu, sauvegarde[idrecu])
        else:
            print("l'identifiant ou le mot de passe est incorrect")
    except:
        pass


def compare(mdprecu, mdp):
    if mdprecu == mdp:
            stock_vbucks.v_bucks()
            return
    print("l'identifiant ou le mot de passe est incorrect")