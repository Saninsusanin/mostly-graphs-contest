from typing import List

import pytest

from .task import task2


class Case:
    def __init__(self, name: str, n: int, dependencies: List[List[int]], keys: List[List[int]], answer: List[bool]):
        self._name = name
        self.n = n
        self.dependencies = dependencies
        self.keys = keys
        self.answer = answer

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        n=3,
        dependencies=[
            [1, 2],
            [1, 0],
            [2, 0]
        ],
        keys=[
            [1, 0],
            [1, 2]
        ],
        answer=[True, True],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(
        n=case.n,
        dependencies=case.dependencies,
        keys=case.keys,
    )
    assert answer == case.answer
