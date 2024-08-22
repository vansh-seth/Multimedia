def justify(text, L):
    words = text.split()
    result = []
    line = []
    length = 0
    for word in words:
        if length + len(word) + len(line) > L:
            for i in range(L - length):
                line[i % (len(line) - 1 or 1)] += ' '
            result.append(''.join(line))
            line, length = [], 0
        line.append(word)
        length += len(word)
    result.append(' '.join(line).ljust(L))
    return '\n'.join(result)
text = "The quick brown fox jumps over the lazy dog."
L = 17
jtext = justify(text, L)
print(jtext)
