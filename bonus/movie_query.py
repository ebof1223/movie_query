import csv
import argparse
import json

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

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    parser.add_argument('--year-after', type=str)
    parser.add_argument('--genre', type=str)
    parser.add_argument('--rating-above', type=float)
    parser.add_argument('--director', type=str)
    parser.add_argument('--actor', type=str)
    parser.add_argument('--runtime-more-than', type=str)
    parser.add_argument('--gross-min', type=int)
    parser.add_argument('--votes-min', type=int)
    parser.add_argument('--output-format', type=str)
    parser.add_argument('--output-file', type=str)
    parser.add_argument('--export-log', type=str)

    args = parser.parse_args()
    path = args.input or ""

    if not input_handler(path):
        return 1
    results = []
    with open(path) as imdb_top_1000:
        reader = csv.DictReader(imdb_top_1000)
        sorted_by_rating = sorted(
            list(reader), key=lambda h:float(h["imdb_rating"]), reverse=True
        )
        print(reader.fieldnames)
        for item in sorted_by_rating:
            if args.year_after and (not item["released_year"].isdigit() or item["released_year"] <= args.year_after):
                continue
            if args.genre and args.genre not in item["genre"]:
                    continue
            if args.rating_above and float(item["imdb_rating"])<= args.rating_above:
                    continue
            if args.director and args.director != item["director"]:
                    continue
            if args.actor and args.actor not in [item["star_1"],item["star_2"], item["star_3"], item["star_4"] ]:
                continue
            if args.runtime_more_than and int(item["runtime"].replace(" min", "")) <= args.runtime_more_than:
                    continue
            if args.gross_min and item["gross"].isdigit() and int(item["gross"]) <= args.gross_min:
                continue
            if args.votes_min and item["no_of_votes"].isdigit() and int(item["no_of_votes"]) <= args.votes_min:
                continue
            results.append(item)
            print(list(item.values()))
     
    if args.output_format:
        output_filename = args.output_file or "filtered_movies"
        if args.output_format == "csv":
            if ".csv" not in output_filename:
                output_filename += ".csv"
            with open(output_filename, "w") as out:
                if not results:
                    return 0
                writer = csv.DictWriter(out, fieldnames=results[0].keys())
                writer.writeheader()
                writer.writerows(results)
        elif args.output_format == "json":
            if ".json" not in output_filename:
                output_filename += ".json"
            with open(output_filename, "w") as out:
                json.dump(results, out)
        else:
            print("Invalid output format provided, no output file generated")

    if args.export_log:
        output_filename = args.export_log or "filtered_movies.txt"
        with open(output_filename, 'w') as out:
            if not results:
                return 0
            for header in results[0].keys():
                out.write(header)
                out.write("  ")
            out.write("\n")
            for result in results:
                out.write("  ".join(list(result.values())))
                out.write("\n")
    return 0

main()
