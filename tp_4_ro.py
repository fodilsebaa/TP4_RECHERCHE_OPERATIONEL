import random as r
import numpy as np
#exercice1
# question 1: fonction qui permet de simuler un « lancer de dé ».


def lancer_dé():
    #randrange est une fonction prédifinie de la bibliothéque random pour simuler des chifres aleatoirs 
    return r.randrange(1, 7)

# question 2:fonction qui simule le lancer de dé « n » fois


def lancé_n_fois(n):
    resultat = []
    for i in range(n):
        resultat.append(lancer_dé())
    print(resultat)
    print("le nombre de six dans ce example est:")
    print(nb_apparition_de_6(resultat))

# question 3:fonction qui calcule le nombre d'apparition de 6 dans le lancé


def nb_apparition_de_6(resultat):
    return resultat.count(6)

# question 4:fonction de lancer un dé jusqu'à ce que l'on obtienne un « 6 » et calcul et affiche le nombre des lancés avant lobtention de 6


def lancé_jusqua_lapparition_de_6(n):
    res = []
    k=0
    while True:
        d = lancer_dé()
        res.append(d)
        k=k+1
        if d == 6:
            break
    print(res)
    print(k-1)

# question 5:fonction qui Simule le tirage d’une pièce de monnaie « n » fois


def lancé_dune_piece_n_fois(n):
    resultat = []
    for i in range(n):
        d=r.randrange(0, 2)
        resultat.append(d)
    return resultat
#exercice 2
# question 1:une fonction qui vérifié si un vecteur de taille n est un vecteur stochastique ou non


def verifie_vecteur_stochatique(v):
    if sum(v) == 1:
        return True
    else:
        return False

# question 2: une fonction qui vérifie si une matrice carrée T de taille n*n est une matrice stochastique ou non

#dabord on va definir une fonction qui verifie si une matrice est carée ou non

def verifie_matrice_caree(mat):
    for v in mat:
        if len(v) != len(mat):
            return False
        else:
            continue
    return True

#fonction de verification matrice stochastique
def verifie_matrice_stochatique(matrice):
    a= verifie_matrice_caree(matrice)
    if a == False:
        return IndexError("la Matrice entré n'est pas une matrice carée")
    for v in matrice:
        if verifie_vecteur_stochatique(v) == False:
            return False
        else:
            continue
    return True

# question 3 fonction qui calcule la puissance d'une matrice


def puissance_dune_matrice(mat, puissance):
    if verifie_matrice_caree(mat) == False:
        return IndexError("la Matrice entré n'est pas une matrice carée")
    if verifie_matrice_stochatique(mat) == False:
        return IndexError("la Matrice entré n'est pas une matrice stochatique")

    np_matrice = np.array(mat)
    pui = np.linalg.matrix_power(np_matrice, puissance)

    return pui
#fonction main
def main():
    print("lancé un dé:")
    print(lancer_dé())
    print("lancé un dé n fois:")
    n=3
    lancé_n_fois(n)
    print("le tirage d’une pièce de monnaie « n » fois:")
    print(lancé_dune_piece_n_fois(n))
    print("lancé un dé jusqua l'obtention dun 6:")    
    lancé_jusqua_lapparition_de_6(n)
    v=[1,0,0]
    print("verifie_vecteur_stochatique:")
    print(v)
    k=verifie_vecteur_stochatique(v)
    if(k):
        print("le vecteur est stochastique")
    else:
        print("le vecteur est non stochastique")
    print("verifie si une matrice est carée:")
    mat=[[1,0,0],
         [0,1,0],
         [0,0,1]]
    print(mat)
    k=verifie_matrice_caree(mat)
    if(k):
        print("matrice est carée")
    else:
        print("matrice est non carée")
        
    print("verifie_matrice_stochatique:")
    print(mat)
    k=verifie_matrice_stochatique(mat)
    if(k):
        print("matrice est stochastique")
    else:
        print("matrice est non stochastique")
    print(" calcul puissance_dune_matrice:")
    puissance=2
    print(mat)
    print("a la puissance de")
    print(puissance)
    pui=puissance_dune_matrice(mat, puissance)
    print(pui)
     
if __name__=="__main__":
    main()
