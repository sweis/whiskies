import math

# Outputs a list of whiskies in order of closeness to Oban

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

with open("whiskies.txt") as data:
    lines = [l.strip().split(',') for l in data]

header = map(lambda l: l.strip().lower(), lines[0])
whiskies = { }

for l in lines[1:]:
    whiskies[l[1].lower()] = dict(zip(header, l))

oban = whiskies["oban"]
scores = []
for w in whiskies:
    scores.append((taste_comp(oban, whiskies[w]), w))

scores.sort()
for s in scores:
    print s[1].capitalize(), s[0]
