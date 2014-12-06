import argparse
import math

# Outputs a list of whiskies in order of closeness to the input

flavors = [ "body", "spicy", "malty", "tobacco",
            "smoky", "honey", "nutty", "floral",
            "medicinal", "sweetness", "fruity"]

def taste_comp(whiskie, another_whiskie):
    diff_tally = 0
    for flavor in flavors:
        val = int(whiskie[flavor])
        another_val = int(another_whiskie[flavor])
        diff_squared = math.pow((val - another_val), 2)
        diff_tally += diff_squared
    return diff_tally

def compare(whisky_name, source_file):
    with open(source_file) as data:
        lines = [l.strip().split(',') for l in data]

    header = map(lambda l: l.strip().lower(), lines[0])
    whiskies = { }

    for l in lines[1:]:
        whiskies[l[1].lower()] = dict(zip(header, l))

    if not whiskies.has_key(whisky_name):
        print("{} is not in source file {}".format(whisky_name, source_file))
        print("Supported whiskies are:")
        print " ".join(sorted(whiskies))
        return

    whisky = whiskies[whisky_name]
    scores = []
    for w in whiskies:
        scores.append((taste_comp(whisky, whiskies[w]), w))

    scores.sort()
    print("Top 10 closest matches to {}:".format(whisky_name.capitalize()))
    for s in scores[1:10]:
        print("\t{} ({})".format(s[1].capitalize(), s[0]))
    print("Least closest matches to {}:".format(whisky_name.capitalize()))
    for s in scores[-10:]:
        print("\t{} ({})".format(s[1].capitalize(), s[0]))

def main():
    parser = argparse.ArgumentParser("Find closest whisky matches")
    parser.add_argument("whisky",
        help="The whisky to match",
        default="lagavulin")
    parser.add_argument("-s", "--source",
        help="Source file",
        default="whiskies.txt")
    args = parser.parse_args()
    compare(args.whisky, args.source)

if __name__ == "__main__":
    main()
