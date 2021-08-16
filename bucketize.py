def bucketize(sentence, length):
    words = sentence.split()
    buckets = []
    phrase = ""

    for word in words: 
        print(word)
        print(phrase)
        if len(word) > length:
            return
        elif len(phrase) + len(word) < length:
            if len(phrase) == 0:
                phrase = word
            else:
                phrase += " " + word
        else:
            buckets.append(phrase)
            phrase = ""
    if len(phrase) > 0:
        buckets.append(phrase)
    else:
        buckets.append(words[len(words) - 1])
    return buckets