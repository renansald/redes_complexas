import gzip
import json


def readFileJson(pathFile):
    """
    This function read a json file and sava datas in a dictionary

    :param pathFile: File will be read
    :return : A list
    :rtype : Voids
    """

    try:
        list = []
        with gzip.open(pathFile, "r") as file:
            for lines in file:
                list.append(json.loads(lines.strip()))
        return list
    except Exception as e:
        print(f'Uma exceção ocorreu\n {e}')


def CreateFileTsv(list=None):
    """
    This function create a .tsv file with the dictionary recived as param

    :param dictionary: Reciver a dictionary;
    :type dictionary: Dictionary 
    :return : Do a screen print message os success or fail case dictionary is None;
    :rtype : Void
    """

    try:
        if list is None:
            print("O dicionário é vazio")
            return
        with open("haddadPosts.tsv", "w") as file:
            file.write(
                "id\tmessage\tcreated_time\tshares\tangryReactions\n")
            for iten in list:
                id = iten["id"]
                message = iten["message"].replace(
                    "\n", " ") if "message" in iten.keys() else None
                created_time = iten["created_time"]
                shares = iten["shares"]["count"] if "shares" in iten.keys(
                ) else "0"
                angryReactions = iten["reactions_angry"]["summary"]["total_count"]
                file.write(
                    f'{id}\t{message}\t{created_time}\t{shares}\t{angryReactions}\n')
        print("Arquivo .tsv criado com sucesso\n\n")
    except Exception as e:
        print(f'Uma exceção ocorreu\n {e}')


def main():
    pathFile = "../DataBase/posts_presidenciaveis/haddad/all_posts.json.gz"
    list = readFileJson(pathFile)
    CreateFileTsv(list)


if __name__ == "__main__":
    main()
