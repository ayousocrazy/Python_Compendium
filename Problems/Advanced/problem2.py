"""
Text Token Stream
Create a class TokenStream(text) that:
-Iterates over each word (splitting manually)
-Skips multiple spaces
-Works both as an iterator and generator-like class

Usage:
    for token in TokenStream("hello   world this is python"):
        print(token)
"""

class TokenStream:
    def __init__(self, txt):
        self.text = txt
        self.i = 0
        self.n = len(txt)

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < self.n and self.text[self.i] == " ":
            self.i += 1

        if self.i >= self.n:
            raise StopIteration

        word = ""
        while self.i < self.n and self.text[self.i] != " ":
            word += self.text[self.i]
            self.i += 1

        return word

# TEST
print("Test:")
txt = "   hello   world this            is python     "
for token in TokenStream(txt):
    print(token)