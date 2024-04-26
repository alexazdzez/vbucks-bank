import pickle


def add_vucks(mdp, code):
    try:
        #lis fichier vbucks
        file = open('savevbucks', 'rb')
        savevbucks = pickle.load(file)
        file.close()
    except:
        savevbucks = {}

    #ajoute nouveau vbucks
    savevbucks[code] = mdp

    #ecris fichier vbucks
    file = open('savevbucks', 'wb')
    pickle.dump(savevbucks, file)
    file.close()


def read_vbucks(mdp):
    try:
        print("debut")
        file = open('savevbucks', 'rb')
        savevbucks = pickle.load(file)
        file.close()

        if mdp in savevbucks.keys():
            print(savevbucks[mdp])
    except:
        pass
        print("echek")
