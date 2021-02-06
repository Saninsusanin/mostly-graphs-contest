from typing import List

import pytest

from .task import task4


class Case:
    def __init__(self, name: str, file_names: List[str], answer: List[str]):
        self._name = name
        self.file_names = file_names
        self.answer = answer

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        file_names=["pes", "fifa", "gta", "pes(2019)"],
        answer=["pes", "fifa", "gta", "pes(2019)"],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = task4(
        file_names=case.file_names,
    )
    assert answer == case.answer
