sentence = "This is a common interview question"

chars = list(sentence.lower())
print(chars)
charsdic = {}
for c in chars:
    if c in charsdic.keys():
        charsdic.update({c: charsdic[c] + 1})
    else:
        charsdic[c] = 1
print(charsdic)

print(max(charsdic, key=lambda k: charsdic[k]))