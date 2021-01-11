from typing import Dict, List


class Matrix:
    def __init__(self, matrix_string: str):
        self._rows = []
        for r in [i for i in matrix_string.splitlines()]:
            self._rows.append([int(x) for x in r.split(" ")])

    def row(self, index: int) -> List[int]:
        return self._rows[index - 1].copy()

    def column(self, index: int) -> List[int]:
        return [i[index - 1] for i in self._rows]
