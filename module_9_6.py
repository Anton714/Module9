def all_variants(text):
    i, j = 0, 0
    while i in range(len(text)):
        j = 0
        while j in range(len(text) - i):
            yield text[j:j + i + 1]
            j += 1
        i += 1


a = all_variants("abcd")
for i in a:
    print(i)