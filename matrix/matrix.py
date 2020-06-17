class Matrix:
    matrix_strings = ""

    def __init__(self, matrix):
        self.matrix_strings = matrix

    def row(self, index):
        return list(map(lambda x: int(x),
                        self.matrix_strings.split("\n")[index-1].split(" ")))

    def column(self, index):
        return list(map(lambda r: int(r.split(" ")[index-1]),
                        self.matrix_strings.split("\n")))
