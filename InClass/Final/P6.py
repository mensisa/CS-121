def firstVowel(word):
    if word[0] != "y":
        for i in range(0, len(word)):
            if word[i] in "aeiouy":
                return i
                break
    else:
        for i in range(0, len(word)):
            if word[i] in "aeiou":
                return i
                break


def pigLatin(word):
    n = firstVowel(word)
    if n == 0:
        return word[n:] + "yay"
    else:
        return word[n:] + word[0:n] + "ay"


def main():
    s = str(input("Enter a sentence to translate: "))
    items = s.split()
    words = [x for x in items]
    for word in words:
        print(pigLatin(word), end=" ")

main()
