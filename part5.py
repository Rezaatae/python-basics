import re

patterns = ["term1", "term2"]

text = "this is a string with term1, not the other"

for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern, text):
        print("MATCH")
    else:
        print("NO MATCH")


match = re.search("term1", text)

print(match.start())

print(re.split(" ", text))



print(re.findall("match", "test phrase match in middle"))


def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")


test_phrase = "sdsd....ssdddd..sdddsdd....dsds....dssss...sddddd"

test_patterns = ["sd+"]

multi_re_find(test_patterns,test_phrase)