def censor_text(sentence):
    with open('input.txt', 'r', encoding='utf-8') as f:
        banned = f.read().split()

    lower_sentence = sentence.lower()
    result = list(sentence)

    for bad in banned:
        bad_lower = bad.lower()
        start = 0
        while True:
            pos = lower_sentence.find(bad_lower, start)
            if pos == -1:
                break
            for i in range(pos, pos + len(bad_lower)):
                result[i] = '*'
            start = pos + 1

    print(''.join(result))
    
    
text = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!'
censor_text(text)
