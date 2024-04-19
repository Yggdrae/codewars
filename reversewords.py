#Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

#Meu:
def reverse_word(text):
    words = text.split(" ")
    newWords = [word[::-1] for word in words]
    newtext = " ".join(newWords)
    return newtext

#Simplificado:
def reverse_words(text):
    return ' '.join(s[::-1] for s in text.split(' '))

print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('apple'))
print(reverse_words('a b c d'))
print(reverse_words('double  spaced  words'))