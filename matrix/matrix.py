from typing import Dict, List


class Matrix:
    _rows: Dict[int, List[int]]

    def __init__(self, matrix_string: str):
        self._rows = {}
        index = 0
        for input_row in [i for i in matrix_string.split("\n")]:
            self._rows.update({index: [int(i) for i in input_row.split(" ")]})
            index += 1

    def row(self, index: int) -> List[int]:
        return self._rows[index-1]

    def column(self, index: int) -> List[int]:
        return [i[index-1] for i in self._rows.values()]
