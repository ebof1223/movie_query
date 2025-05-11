import csv

def input_hanlder(path:str)->bool:
    try:
        with open(path) as _:
            if path[-4:] != ".csv":
                print("Invalid file. Provide valid file.\n")
                return False
    except FileNotFoundError:
        print("Invalid path. Provide valid path.\n")
        return False

    return True

def main():
    # path = input("Enter path for csv to input: ")
    path = "./imdb_top_1000.csv"
    while not input_hanlder(path):
        path = input("Enter path for csv to input: ")


    with open(path) as idmb_top_1000:
        csv_reader = csv.DictReader(idmb_top_1000)
        for line in csv_reader:
            print(line)


if __name__ == "__main__":
    main()
