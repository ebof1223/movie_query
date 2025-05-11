import csv
import argparse

def input_handler(path:str)->bool:
    try:
        with open(path) as _:
            if path[-4:] != ".csv":
                print("Invalid input flag. Provide valid file.")
                return False
    except FileNotFoundError:
        print("Invalid input path. Provide valid path.")
        return False

    return True

def main():
    parser = argparse.ArgumentParser()
    #TODO: validate flags
    parser.add_argument('--input', type=str)
    parser.add_argument('--year-after', type=str)
    parser.add_argument('--genre', type=str)
    parser.add_argument('--rating-above', type=int)
    parser.add_argument('--director', type=str)
    parser.add_argument('--actor', type=str)
    parser.add_argument('--runtime-more-than', type=str)
    parser.add_argument('--gross-min', type=int)

    args = parser.parse_args()
    path = args.input or ""
    input_handler(path)
    
    with open(path) as imdb_top_1000:
        reader = csv.DictReader(imdb_top_1000)
        sorted_by_rating = sorted(
            list(reader), key=lambda h:float(h["imdb_rating"]), reverse=True
        )
        for item in sorted_by_rating:
            if args.year_after:
                if not item["released_year"].isdigit() or item["released_year"] <= args.year_after:
                    continue
            if args.genre:
                if args.genre not in item["genre"]:
                    continue
            if args.rating_above:
                if float(item["imdb_rating"])<= args.rating_above:
                    continue
            if args.director:
                if item["director"] is not args.director:
                    continue
            if args.actor:
                if args.actor not in [
                    item["star_1"],item["star_2"], item["star_3"], item["star_4"]
                ]:
                    continue
            if args.runtime_more_than:
                if int(item["runtime"].replace(" min", "")) <= args.runtime_more_than:
                    continue
            if args.gross_min:
                if item["gross"] or 0 <= args.runtime_more_than:
                    continue
            print(item)

main()
