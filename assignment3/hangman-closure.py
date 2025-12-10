def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        result = ""
        for ch in secret_word:
            if ch in guesses:
                result += ch
            else:
                result += "_"

        print(result)

        return "_" not in result

    return hangman_closure
