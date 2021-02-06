from typing import List

import pytest

from .task import task3


class Case:
    def __init__(self, name: str, n: int, edges: List[List[int]], probabilities: List[float], start: int, end: int,
                 answer: float):
        self._name = name
        self.n = n
        self.edges = edges
        self.probabilities = probabilities
        self.start = start
        self.end = end
        self.answer = answer

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        n=3,
        edges=[
            [0, 1],
            [1, 2],
            [0, 2]
        ],
        probabilities=[0.5, 0.5, 0.2],
        start=0,
        end=2,
        answer=0.25000,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = task3(
        n=case.n,
        edges=case.edges,
        probabilities=case.probabilities,
        start=case.start,
        end=case.end,
    )
    assert answer == case.answer
