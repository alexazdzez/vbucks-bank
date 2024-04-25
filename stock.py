import pickle
import stock_vbucks


def add(id, mdp):

    file = open('save', 'wb')
    sauvegarde = {
        id : mdp
    }
    pickle.dump(sauvegarde, file)
    file.close()


def connect(idrecu, mdprecu):
    try:
        file = open('save', 'rb')
        sauvegarde = pickle.load(file)
        id = sauvegarde[0]
        mdp = sauvegarde[1]
        file.close()
        compar(idrecu, mdprecu, id, mdp)
    except:
        pass


def compar(idrecu, mdprecu, id, mdp):
    if idrecu == id and mdprecu == mdp:
            stock_vbucks.v_bucks()
            return
    print("l'identifiant ou le mot de passe est incorrect")