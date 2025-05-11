import argparse

def input_handler(path:str)->bool:
    try:
        with open(path) as _:
            if path[-4:] != ".csv":
                print("Invalid input flag. Provide valid file.")
                return False
    except FileNotFoundError:
        print("Invalid input flat. Provide valid path.")
        return False

    return True

def main():
    parser =argparse.ArgumentParser()
    parser.add_argument('-i','--input', type=str, help="Pass input path as flag")
    args = parser.parse_args()
    path = args.input
    input_handler(path)


if __name__ == "__main__":
    main()
