def words(txt):
    with open(txt) as word:
        word = word.read().strip().split('\n')
        word = [i.lower() for i in word if i.endswith('я') or i.endswith('а') or i.endswith('ь')]
    return word
