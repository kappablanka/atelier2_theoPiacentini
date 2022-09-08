
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
            max_liste_parametre = list[i]
    return max_liste_parametre


def ind_max(liste_parametre: list[int]) -> int:
    """
    Fonction donnant l'élément maximum de la liste_parametre passée en paramètre
    :param liste_parametre: (list[int]) liste_parametre passé en paramètre
    :return: (int) retourne l'indice de l'élément maximum de la liste_parametre
    """
    if len(liste_parametre) == 0:
        return -1

    max_liste_parametre = liste_parametre[0]
    i_max = -1
    for i in range(1, len(liste_parametre)):
        if liste_parametre[i] > max_liste_parametre:
            max_liste_parametre = list[i]
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
    for i in range(1, len(liste_parametre)):
        if liste_parametre[i-1] > liste_parametre[i]:
            return False
    return True


def est_triee_2(liste_parametre: list[int]) -> bool:
    """
    Fonction testant si une liste est triée papr ordre croissant
    :param liste_parametre: (list[int]) liste dont on testera si elle est triée
    :return: (bool) variable répondant à la question: est triée ?
    """
    flag_est_triee = True
    i = 1
    while i < len(liste_parametre) and flag_est_triee:
        if liste_parametre[i - 1] > liste_parametre[i]:
            flag_est_triee = False

    return flag_est_triee

# La meilleure fonction est la première si l'on utilise un return direct comme ici sinon c'est la deuxième.


def position_tri(liste_triee: list[int], e: int) -> int:
    """
    Fonction donnant la position d'un élément e dans une liste_parametre trié
    :param liste_triee: (list[int]) liste_parametre dans laquelle on cherche la position de l'élément e
    :param e: (int) element dont on cherchera la position dans la liste_parametre
    :return: (int) position de l'élément e
    """
    m = len(liste_triee) // 2
    if liste_triee[m] == e:
        return m
    elif liste_triee[m] < e:
        return position_tri(liste_triee[:m-1], e)
    else:
        return m + position_tri(liste_triee[m+1: len(liste_triee)], e)


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
            liste_T.append(i)
        else:
            return False

    return True

