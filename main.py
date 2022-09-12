import matplotlib.pyplot as plt


def somme_1(liste_parametre: list[int]) -> int:
    """
        Fonction sommant les élements d'une liste_parametre à l'aide d'une boucle for basé sur les indices
        :param liste_parametre: (list[int]) liste_parametre d'ints
        :return: int somme des élements de la liste_parametre
    """
    somme = 0
    for i in range(len(liste_parametre)):
        somme += liste_parametre[i]
    return somme


def somme_2(liste_parametre: list[int]) -> int:
    """
        Fonction sommant les élements d'une liste_parametre à l'aide d'une boucle for basé sur les élements
        :param liste_parametre: list[int] liste_parametre d'ints
        :return: int somme des élements de la liste_parametre
    """
    somme = 0
    for e in liste_parametre:
        somme += e
    return somme


def somme_3(liste_parametre: list[int]) -> int:
    """
    Fonction sommant les élements d'une liste_parametre à l'aide d'une boucle while
    :param liste_parametre: list[int] liste_parametre d'ints
    :return: int somme des élements de la liste_parametre
    """
    somme = 0
    i = 0
    while i < len(liste_parametre):
        somme += liste_parametre[i]
        # ne pas oublié d'ajouté 1 à i !
        i += 1
    return somme


def test_exercice1():
    print("TEST SOMME, somme_1()")
    # test liste_parametre vide
    print("Test liste_parametre vide : ", somme_1([]))
    # test somme 11111
    S = [1, 10, 100, 1000, 10000]
    print("Test somme 1111 : ", somme_1(S))


def test_exercice2():
    print("TEST SOMME, somme_2()")
    # test liste_parametre vide
    print("Test liste_parametre vide : ", somme_2([]))
    # test somme 11111
    S = [1, 10, 100, 1000, 10000]
    print("Test somme 1111 : ", somme_2(S))


def test_exercice3():
    print("TEST SOMME, somme_3()")
    # test liste_parametre vide
    print("Test liste_parametre vide : ", somme_3([]))
    # test somme 11111
    S = [1, 10, 100, 1000, 10000]
    print("Test somme 1111 : ", somme_3(S))


test_exercice1()
test_exercice2()
test_exercice3()


def moyenne(liste_parametre: list[int]) -> float:
    """
    Fonction calculant la moyenne des élements de la liste_parametre
    :param liste_parametre: (list[int]) liste_parametre d'ints
    :return: (float) moyenne des élements de la liste_parametre
    """
    if len(liste_parametre) > 0:
        return somme_2(liste_parametre) / len(liste_parametre)
    else:
        return 0


def nb_sup_1(liste_parametre: list[int], e: int) -> int:
    """
    Fonction retournant le nombre d'éléments dans une liste_parametre donné supérieur à une variable donnée à l'aide
    d'une boucle
    for basée sur des indices
    :param e: (int) élément à comparer
    :param liste_parametre: (list[int]) liste_parametre dont on établira le nombre d'éléments superieur à e
    :return: (int) nombre d'éléments supérieur à e.
    """

    nb_elements_superieur_e = 0
    for i in range(len(liste_parametre)):
        if liste_parametre[i] > e:
            nb_elements_superieur_e += 1
    return nb_elements_superieur_e


def nb_sup_2(liste_parametre: list[int], e: int) -> int:
    """
    Fonction retournant le nombre d'éléments dans une liste_parametre donné supérieur à une variable donnée à l'aide
    d'une boucle
    for basée sur les éléments
    :param e: (int) élément à comparer
    :param liste_parametre: (list[int]) liste_parametre dont on établira le nombre d'éléments superieur à e
    :return: (int) nombre d'éléments supérieur à e.
    """

    nb_elements_superieur_e = 0
    for elt_liste_parametre in liste_parametre:
        if elt_liste_parametre > e:
            nb_elements_superieur_e += 1
    return nb_elements_superieur_e


def moy_sup(liste_parametre: list[int], e: int) -> float:
    """
    Fonction retournant la moyenne des éléments d'une liste_parametre supérieures à un élément donné
    :param e: (int) élément à comparer
    :param liste_parametre: (list[int]) liste_parametre dont on établira la moyenne des éléments supérieurs à e
    :return: (float) moyenne des éléments supérieurs à e.
    """
    if len(liste_parametre) == 0:
        return 0
    somme = 0
    for elt_liste_parametre in liste_parametre:
        if elt_liste_parametre > e:
            somme += elt_liste_parametre
    return somme / len(liste_parametre)


def val_max(liste_parametre: list[int]) -> int:
    """
    Fonction donnant l'élément maximum de la liste_parametre passée en paramètre
    :param liste_parametre: (list[int]) liste_parametre passé en paramètre
    :return: (int) élément maximum de la liste_parametre
    """
    if len(liste_parametre) == 0:
        return -1
    max_liste_parametre = liste_parametre[0]

    for i in range(1, len(liste_parametre)):
        if liste_parametre[i] > max_liste_parametre:
            max_liste_parametre = liste_parametre[i]
    return max_liste_parametre


def ind_max(liste_parametre: list[int]) -> int:
    """
    Fonction donnant l'élément maximum de la liste_parametre passée en paramètre
    :param liste_parametre: (list[int]) liste_parametre passé en paramètre
    :return: (int) retourne l'indice de l'élément maximum de la liste_parametre
    """
    if len(liste_parametre) == 0:
        return -1
    elif len(liste_parametre) == 1:
        return liste_parametre[0]

    max_liste_parametre = liste_parametre[0]
    i_max = -1
    for i in range(1, len(liste_parametre)):
        if liste_parametre[i] > max_liste_parametre:
            max_liste_parametre = liste_parametre[i]
            i_max = i
    return i_max


def position_1(liste_parametre: list[int], e: int) -> int:
    """
    Fonction donnant la position d'un élément e dans une liste_parametre à l'aide d'une boucle for basée sur des indices
    :param liste_parametre: (list[int]) liste_parametre dans laquelle on cherche la position de l'élément e
    :param e: (int) element dont on cherchera la position dans la liste_parametre
    :return: (int) position de l'élément e
    """
    for i in range(len(liste_parametre)):
        if liste_parametre[i] == e:
            return i
    return 0


def position_2(liste_parametre: list[int], e: int) -> int:
    """
    Fonction donnant la position d'un élément e dans une liste_parametre à l'aide d'une boucle for basée sur les
    éléments
    :param liste_parametre: (list[int]) liste_parametre dans laquelle on cherche la position de l'élément e
    :param e: (int) element dont on cherchera la position dans la liste_parametre
    :return: (int) position de l'élément e
    """
    position = 0
    i = 0
    flag_elt_trouve = False
    while i < len(liste_parametre) or flag_elt_trouve:
        if liste_parametre[i] == e:
            position = i
            flag_elt_trouve = True
        i += 1
    return position


def nb_occurence(liste_parametre: list[int], e: int) -> int:
    """
        Fonction donnant le nombre d'occurence dans une liste paramètre
        :param liste_parametre: (list[int]) liste_parametre dans laquelle on cherche la position de l'élément e
        :param e: (int) element dont on cherchera le nombre occurrence dans la liste parametre
        :return: (int) position de l'élément e
    """
    nb_occurence_e = 0
    for elt_liste in liste_parametre:
        if elt_liste == e:
            nb_occurence_e += 1
    return nb_occurence_e


def est_triee_1(liste_parametre: list[int]) -> bool:
    """
    Fonction testant si une liste est triée papr ordre croissant
    :param liste_parametre: (list[int]) liste dont on testera si elle est triée
    :return: (bool) triée ?
    """
    if len(liste_parametre) == 0:
        return True
    elif len(liste_parametre) == 1:
        return True
    for i in range(1, len(liste_parametre)):
        if liste_parametre[i - 1] > liste_parametre[i]:
            return False
    return True


def est_triee_2(liste_parametre: list[int]) -> bool:
    """
    Fonction testant si une liste est triée papr ordre croissant
    :param liste_parametre: (list[int]) liste dont on testera si elle est triée
    :return: (bool) variable répondant à la question: est triée ?
    """
    if len(liste_parametre) == 0:
        return True
    elif len(liste_parametre) == 1:
        return True

    flag_est_triee = True
    i = 1
    while i < len(liste_parametre) and flag_est_triee:
        if liste_parametre[i - 1] > liste_parametre[i]:
            flag_est_triee = False
        i += 1

    return flag_est_triee


# La meilleure fonction est la première si l'on utilise un return direct comme ici sinon c'est la deuxième.


def position_tri(liste_triee: list[int], e: int) -> int:
    """
    Fonction donnant la position d'un élément e dans une liste_parametre trié
    :param liste_triee: (list[int]) liste_parametre dans laquelle on cherche la position de l'élément e
    :param e: (int) element dont on cherchera la position dans la liste_parametre
    :return: (int) position de l'élément e
    """
    m = (len(liste_triee) + 1) // 2
    if liste_triee[m] == e:
        return m
    elif liste_triee[m] > e:
        return position_tri(liste_triee[:m], e)
    else:
        return m + position_tri(liste_triee[m: len(liste_triee)], e)


def a_repetition(liste_parametre: list[int]) -> int:
    """
    Fonction renvoyant True si une liste contient une répétition de valeur et False sinon
    :param liste_parametre:
    :return:
    """
    liste_T = []
    i = 0
    while i < len(liste_parametre):
        if liste_parametre[i] not in liste_T:
            liste_T.append(liste_parametre[i])
        else:
            return True
        i += 1

    return False


def testeur_de_fonction_sur_listes_1_arg(funct, jeu_de_tests, triee=False):
    """
    Fonction permettant de tester la fonction message_imc()
    :return: void
    """
    if not triee:
        for e in jeu_de_tests:
            print(f"{funct.__name__}({e}) = {funct(e)}")
        print("\n")
    else:
        for e in jeu_de_tests:
            e_triee = sorted(e)
            print(f"{funct.__name__}({e_triee}) = {funct(e_triee)}")
        print("\n")


def testeur_de_fonction_sur_listes_2_arg(funct, jeu_de_tests, triee=False):
    """
    Fonction permettant de tester la fonction message_imc()
    :return: void
    """
    if not triee:
        for e in jeu_de_tests:
            print(f"{funct.__name__}({e[0]}, {e[1]}) = {funct(e[0], e[1])}")
        print("\n")
    else:
        for e in jeu_de_tests:
            e0_triee = sorted(e[0])
            print(f"{funct.__name__}({e0_triee}, {e[1]}) = {funct(e0_triee, e[1])}")
    print("\n")


JEU_DE_TESTS_1 = [[-3, 1, 2, -5, 4]]

JEU_DE_TESTS_2 = [([55, 80, 60, 110, 25], 1),
                  ([-3, 1, 2, -5, 4], 1),
                  ([], 1)]

JEU_DE_TESTS_3 = [([55, 80, 60, 110, 25], 80),
                  ([-3, 1, 2, -5, 4], 1)]

JEU_DE_TESTS_4 = [[55, 80, 60, 110, 25],
                  [-3, 1, 2, -5, 4],
                  [],
                  [-3, 1, 1, 2, -5, 4],
                  [55, 25, 60, 110, 25, 25]]

JEU_DE_TESTS_5 = [[1, 2, 3, 4, 5],
                  [5, 5, 5, 5, 4]]

print("\n")

testeur_de_fonction_sur_listes_1_arg(somme_1, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_1_arg(somme_2, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_1_arg(somme_3, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_2_arg(nb_sup_1, JEU_DE_TESTS_2)

testeur_de_fonction_sur_listes_2_arg(nb_sup_2, JEU_DE_TESTS_2)

testeur_de_fonction_sur_listes_2_arg(moy_sup, JEU_DE_TESTS_2)

testeur_de_fonction_sur_listes_1_arg(val_max, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_1_arg(ind_max, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_2_arg(nb_occurence, JEU_DE_TESTS_2)

testeur_de_fonction_sur_listes_1_arg(est_triee_1, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_1_arg(est_triee_1, JEU_DE_TESTS_1, triee=True)

testeur_de_fonction_sur_listes_1_arg(est_triee_2, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_1_arg(est_triee_2, JEU_DE_TESTS_1, triee=True)

testeur_de_fonction_sur_listes_2_arg(position_tri, JEU_DE_TESTS_3, triee=True)

testeur_de_fonction_sur_listes_1_arg(a_repetition, JEU_DE_TESTS_1)

testeur_de_fonction_sur_listes_1_arg(a_repetition, JEU_DE_TESTS_4)


def separer(liste_parametre: list) -> list:
    """
    Fonction retournant une liste triée par (nombres négatifs à gauche, zéro au milieu, positifs à droite
    :param liste_parametre: list à triée
    :return: liste triée
    """
    lsep = [0] * len(liste_parametre)
    i = 0
    j = len(liste_parametre) - 1
    for e in liste_parametre:
        if liste_parametre[i] < 0:
            lsep[i] = e
            i += 1
        else:
            lsep[j] = e
            j -= 1
    return lsep


testeur_de_fonction_sur_listes_1_arg(separer, JEU_DE_TESTS_1)


# Partie 2


def histo(liste_f: list[int]):
    """
    Fonction comptabilisant le nombre d'apparitions de chaque valeur de la liste f passé en paramètre
    :param liste_f: liste d'int passé en paramètre
    :return: retourne l'histogramme de la liste f
    """
    liste_h = [0] * (max(liste_f) + 1)
    for e in liste_f:
        liste_h[e] += 1
    return liste_h


testeur_de_fonction_sur_listes_1_arg(histo, JEU_DE_TESTS_5)


def est_injective(liste_f: list[int]) -> bool:
    """
    Fonction vérifiant si la fonction représentée par la liste f est injective
    :param liste_f: liste passée en paramètre représentant une fonction
    :return: booléen donnant la réponse à la question est injective ?
    """
    for e in histo(liste_f):
        if e > 1:
            return False
    return True


testeur_de_fonction_sur_listes_1_arg(est_injective, JEU_DE_TESTS_5)


def est_surjective(liste_f: list[int]) -> bool:
    """
    Fonction vérifiant si la fonction représentée par la liste f est surjective
    :param liste_f: liste passée en paramètre représentant une fonction
    :return: booléen donnant la réponse à la question est injective ?
    """
    for e in histo(liste_f):
        if e < 1:
            return False
    return True


testeur_de_fonction_sur_listes_1_arg(est_surjective, JEU_DE_TESTS_5)


def est_bijective(liste_f: list[int]) -> bool:
    """
    Fonction vérifiant si la fonction représentée par la liste f est bijective
    :param liste_f: liste passée en paramètre représentant une fonction
    :return: booléen donnant la réponse à la question est injective ?
    """
    for e in histo(liste_f):
        if e != 1:
            return False
    return True


testeur_de_fonction_sur_listes_1_arg(est_bijective, JEU_DE_TESTS_5)


def affiche_histo(liste_f: list[int]):
    """
    Fonction affichant une représentation graphique de l'histogramme associé à la liste
    :param liste_f: liste passée en paramètre représentant une fonction
    :return: void
    """
    liste_h = histo(liste_f)
    max_occ = max(liste_h)
    print(f"liste_f = {liste_f}")
    print("histogramme : ")
    for i in range(max_occ):
        for e in liste_h:
            if e >= max_occ:
                print("| #", end='')
            else:
                print("|  ", end='')
        max_occ -= 1

        print("|")

    print("")
    for i in range(max(liste_f) + 1):
        print(f"| {i}", end='')
    print("|")
    print("\n")


testeur_de_fonction_sur_listes_1_arg(affiche_histo, JEU_DE_TESTS_5)


def affiche_histo_plt(liste_f: list[int]):
    """
    Fonction affichant une représentation graphique de l'histogramme associé à la liste à l'aide de la librairie
    matplotlib.pyplot
    :param liste_f: liste passée en paramètre représentant une fonction
    :return: void
    """
    liste_h = histo(liste_f)
    max_occ = max(liste_h)
    plt.hist(liste_f, bins=max_occ)
    plt.title("Histogramme")
    plt.show()


def agencement(nb_emlacement: int, l_objets: list[int]) -> list[list[int]]:
    """
    Fonction permettant d'agencer les objets de plusieurs vitrines de manière à ce qu'aucun objet du même type ne soit
    dans le même vitrine, si cela est possible
    :param nb_emlacement: nombre de vitrines disponible
    :param l_objets: liste représantant tous les objets à afficher
    :return: agencement possible des objets
    """
    histogramme_l_objets = histo(l_objets)
    if max(histogramme_l_objets) > nb_emlacement:
        return [[0]]
    organisations_vitrines = []
    while histogramme_l_objets != [0] * len(histogramme_l_objets):
        vitrine = []
        for i in range(len(histogramme_l_objets)):
            if histogramme_l_objets[i] > 0:
                vitrine.append(i)
                histogramme_l_objets[i] -= 1

        organisations_vitrines.append(vitrine)
    return organisations_vitrines


JEU_DE_TESTS_6 = [(4, [1, 2, 2, 3, 4, 5, 5])]
testeur_de_fonction_sur_listes_2_arg(agencement, JEU_DE_TESTS_6)


def test_present(present: callable):
    """
    Fonction testant les fonctions present
    :param present: fonction que l'on teste
    :type present: callable
    :return:
    :rtype:
    """
    if not present([], 0):
        print("SUCCES : test liste vide")
    else:
        print("ECHEC : test liste vide")

    if present([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1):
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")

    if present([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 1):
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")

    if present([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 1):
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")

    if not present([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1):
        print("SUCCES : test absence")
    else:
        print("ECHEC : test absence")

    print("")


# VERSION 1
def present1(L, e):
    for i in range(0, len(L), 1):
        if (L[i] == e):
            return (True)
        else:
            return (False)
    return (False)


# VERSION 2
def present2(L, e):
    b = True
    for i in range(0, len(L), 1):
        if (L[i] == e):
            b = True
        else:
            b = False
    return b


# VERSION 3
def present3(L, e):
    b = True
    for i in range(0, len(L), 1):
        return (L[i] == e)


# VERSION 4
def present4(L, e):
    b = False
    i = 0
    while i < len(L) and b:
        if L[i] == e:
            b = True
    return b


print("test present 1")
test_present(present1)

print("test present 2")
test_present(present2)

print("test present 3")
test_present(present3)

print("test present 4")
test_present(present4)


# version 1:
# retourne faux si le premier élément n'est pas bon

# version 2:
# si le dernier n'est pas le même le résultat est faux

# version 3:
# Je ne sais même pas quoi dire

# version 4:
# On ne rentre pas dans la boucle !

def test_pos(pos: callable):
    """
    Fonction testant les fonctions present
    :param pos: fonction que l'on teste
    :type pos: callable
    :return:
    :rtype:
    """
    if not pos([], 0):
        print("SUCCES : test liste vide")
    else:
        print("ECHEC : test liste vide")

    if pos([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1) == [0]:
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")

    if pos([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 1) == [9]:
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")

    if pos([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 1) == [4]:
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")

    if not pos([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1):
        print("SUCCES : test absence")
    else:
        print("ECHEC : test absence")

    print("")


#VERSION 1
def pos1(L, e) :
    Lres = list(L)
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres += [i]
    return Lres

# VERSION 2
def pos2(L, e) :
    Lres = list(L)
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[i] = i
    return Lres

# VERSION 3
def pos3(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres

# VERSION 4
def pos4(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    j=0
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[j]= i
    return Lres


print("test pos 1")
test_present(present1)

print("test pos 2")
test_present(present2)

print("test pos 3")
test_present(present3)

print("test pos 4")
test_present(present4)

# version 1:
# definition Lres fausse

# version 2:
# definition de Lres fausse

# version 3:
# mauvais append

# version 4:
# j ne bouge pas