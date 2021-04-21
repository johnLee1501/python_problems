def reverse_words_order_and_swap_cases(sentence):
    result = []
    words = sentence.split()
    words.reverse()
    for word in words:
        result.append(word.swapcase())
    return " ".join(result)


if __name__ == '__main__':
    sentence = input()
    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
