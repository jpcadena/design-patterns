"""
Flyweight Coding Exercise
"""


class Sentence:
    """
    Sentence class
    """

    def __init__(self, plain_text: str):
        self.words: list[str] = plain_text.split(' ')
        self.tokens: list = [None] * len(self.words)

    class WordToken:
        """
        Word token class
        """

        def __init__(self):
            self.capitalize: bool = False

    def __getitem__(self, index: int):
        word_token = self.tokens[index]
        if word_token is None:
            word_token = self.WordToken()
            self.tokens[index] = word_token
        return word_token

    def __str__(self):
        result: list[str] = []
        for idx, word in enumerate(self.words):
            if self.tokens[idx] is not None and self.tokens[idx].capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return ' '.join(result)
