from typing import List

import pytest

from .task import task8


class Case:
    def __init__(self, name: str, equations: List[str], answer: int):
        self._name = name
        self.equations = equations
        self.answer = answer

    def __str__(self) -> str:
        return 'task8_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        equations=["c==c", "b==d", "x!=z"],
        answer=True,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task8(case: Case) -> None:
    answer = task8(
        equations=case.equations,
    )
    assert answer == case.answer
