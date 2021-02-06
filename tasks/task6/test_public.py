from typing import List

import pytest

from .task import task6


class Case:
    def __init__(self, name: str, n: int, cost: List[int], answer: str):
        self._name = name
        self.n = n
        self.cost = cost
        self.answer = answer

    def __str__(self) -> str:
        return 'task6_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        n=9,
        cost=[4, 3, 2, 5, 6, 7, 2, 5, 5],
        answer='7772',
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task6(case: Case) -> None:
    answer = task6(
        n=case.n,
        cost=case.cost,
    )
    assert answer == case.answer
