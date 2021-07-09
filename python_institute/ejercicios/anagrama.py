text1 = input().lower().replace(" ", "")
text2 = input().lower().replace(" ", "")
text1 = "".join(sorted(text1))
text2 = "".join(sorted(text2))
if text1 == text2:
    print("Anagramas")
else:
    print("No son Anagramas")
