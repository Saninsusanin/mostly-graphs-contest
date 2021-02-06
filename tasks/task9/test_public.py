from typing import List

import pytest

from .task import task9


class Case:
    def __init__(self, name: str, n: int, plots: List[List[int]], answer: int):
        self._name = name
        self.n = n
        self.plots = plots
        self.answer = answer

    def __str__(self) -> str:
        return 'task9_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        n=3,
        plots=[
            [3, 1, 6, 4, 1],
            [1, -2, 2, -3, 1],
            [-2, -2, -1, -3, 2]
        ],
        answer=2,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task9(case: Case) -> None:
    answer = task9(
        n=case.n,
        plots=case.plots,
    )
    assert answer == case.answer
