"""
Flyweight Coding Exercise
"""
from typing import Union


class Sentence:
    """
    Sentence class
    """

    def __init__(self, plain_text: str):
        self.words: list[str] = plain_text.split(" ")
        self.tokens: list[Union[None, 'Sentence.WordToken']] = [None] * len(
            self.words
        )

    class WordToken:
        """
        Word token class
        """

        def __init__(self) -> None:
            self.capitalize: bool = False

    def __getitem__(self, index: int) -> Union[None, 'Sentence.WordToken']:
        word_token = self.tokens[index]
        if word_token is None:
            word_token = self.WordToken()
            self.tokens[index] = word_token
        return word_token

    def __str__(self) -> str:
        result: list[str] = []
        for idx, word in enumerate(self.words):
            token = self.tokens[idx]
            if token and token.capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return " ".join(result)
