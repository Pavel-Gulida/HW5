import string

punctuation = string.punctuation + " "
hashtag = input("Enter a hashtag: ")
hashtag = hashtag.title()
for letter in punctuation:
    for i in range(hashtag.count(letter)):
        j = hashtag.find(letter)
        hashtag = hashtag[:j] + hashtag[j+1:]

hashtag = hashtag[:140]
hashtag = "#" + hashtag


print(hashtag)
