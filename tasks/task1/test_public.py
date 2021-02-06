from typing import List

import pytest

from .task import task1


class Case:
    def __init__(self, name: str, n: int, m: int, edges: List[List[int]], answer: int):
        self._name = name
        self.n = n
        self.m = m
        self.edges = edges
        self.answer = answer

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        n=3,
        m=6,
        edges=[
            [0, 1, 10],
            [0, 2, 1],
            [1, 2, 2]
        ],
        answer=13,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        n=case.n,
        m=case.m,
        edges=case.edges,
    )
    assert answer == case.answer
