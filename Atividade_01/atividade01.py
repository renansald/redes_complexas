# -*- coding: utf-8 -*-

__Author__ = "Renan Saldanha"

import json


def createFileJson(dictionary=None):
    """
    This function create a json file with the dictionary recived as param

    :param dictionary: Reciver a dictionary;
    :type dictionary: Dictionary 
    :return : Do a screen print message os success or fail case dictionary is None;
    :rtype : Void
    """

    try:
        if dictionary is None:
            print("O dicionário é vazio")
            return
        with open("Drinks.json", "w") as file:
            json.dump(dictionary, file)
        print("Arquivo .json criado com sucesso\n\n")
    except Exception as e:
        print(f'Uma exceção ocorreu\n {e}')


def printDrinks(dictionary=None):
    """
    This function print a formatted table of drinks

    :param dictionary: Reciver a dictionary;
    :type dictionary: Dictionary 
    :return : Do a screen print message with params of dictionary or fail case dictionary is None;
    :rtype : Void
    """

    try:
        if dictionary is None:
            print("Dicionário inválido\n")
            return
        for key in dictionary:
            print("\n\n")
            print(key)
            print(f'\tNome: {dictionary[key]["nome"]}')
            print(f'\tPreço: {dictionary[key]["preco"]}')
            print(f'\tRestrição: {dictionary[key]["restricao"]}')
            print(f'\tTeor Alcoolico: {dictionary[key]["teorAlcoolico"]}')
            print(f'\tQuantidade em Estoque: {dictionary[key]["quantidade"]}')
    except Exception as e:
        print(f'Uma exceção ocorreu\n {e}')


def readFileJson():
    """
    This function read a json file and sava datas in a dictionary

    :return : Do a screen print of file's content;
    :rtype : Void
    """

    try:
        dictionary = {}
        with open("Drinks.json", "r") as file:
            dictionary = json.load(file)
        print(8*"*" + "Minhas Bebidas" + 8*"*")
        printDrinks(dictionary)
        print("\n\n\n\n\n\n" + 8*("*")+"Arquivo JSON"+8*('*')+"\n\n")
        print(dictionary)
    except Exception as e:
        print(f'Uma exceção ocorreu\n {e}')


def CreateFileTsv(dictionary=None):
    """
    This function create a .tsv file with the dictionary recived as param

    :param dictionary: Reciver a dictionary;
    :type dictionary: Dictionary 
    :return : Do a screen print message os success or fail case dictionary is None;
    :rtype : Void
    """

    try:
        if dictionary is None:
            print("O dicionário é vazio")
            return
        with open("Drinks.tsv", "w") as file:
            file.write(
                "id\tnome\tpreco\trestricao\tteorAlcoolico\tquantidade\n")
            for key in dictionary:
                nome = dictionary[key]["nome"]
                preco = dictionary[key]["preco"]
                restricao = dictionary[key]["restricao"]
                teorAlcoolico = dictionary[key]["teorAlcoolico"]
                quantidade = dictionary[key]["quantidade"]
                file.write(
                    f'{key}\t{nome}\t{preco}\t{restricao}\t{teorAlcoolico}\t{quantidade}\n')
        print("Arquivo .tsv criado com sucesso\n\n")
    except Exception as e:
        print(f'Uma exceção ocorreu\n {e}')


def readFileTsv():
    """
    This function read a .tsv file and sava datas in a dictionary

    :return : Do a screen print of file's content;
    :rtype : Void
    """
    try:
        dictionary = {}
        with open("Drinks.tsv", "r") as file:
            str = file.readline()
            keys = str.strip().split("\t")
            str = file.readline()
            while(str):
                values = str.strip().split("\t")
                dictionary[values[0]] = {keys[1]: values[1], keys[2]: values[2],
                                         keys[3]: values[3], keys[4]: values[4], keys[5]: values[5]}
                str = file.readline()
        print(8*"*" + "Minhas Bebidas" + 8*"*")
        printDrinks(dictionary)
        print("\n\n\n\n\n\n" + 8*("*") +
              "Variável dictionary carregada do arquivo .tsv"+8*('*')+"\n\n")
        print(dictionary)
    except Exception as e:
        print(f'Uma exceção ocorreu\n {e}')


def main():
    myDrinks = {}
    myDrinks['1'] = {'nome': 'Gin', 'preco': 20.50,
                     'restricao': 18, 'teorAlcoolico': 5, 'quantidade': 12}
    myDrinks['2'] = {'nome': 'Vodka', 'preco': 50.0,
                     'restricao': 18, 'teorAlcoolico': 80, 'quantidade': 10}
    myDrinks['3'] = {'nome': 'Refrigerante', 'preco': 5.0,
                     'restricao': 3, 'teorAlcoolico': 0, 'quantidade': 50}
    myDrinks['4'] = {'nome': 'Chá Gelado', 'preco': 5.0,
                     'restricao': 4, 'teorAlcoolico': 0, 'quantidade': 100}
    myDrinks['5'] = {'nome': 'Suco', 'preco': 0.98,
                     'restricao': 3, 'teorAlcoolico': 0, 'quantidade': 10}
    createFileJson(myDrinks)
    readFileJson()
    CreateFileTsv(myDrinks)
    readFileTsv()


if __name__ == "__main__":
    main()
