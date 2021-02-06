import pytest

from .task import task10


class Case:
    def __init__(self, name: str, s: str, t: str, answer: int):
        self._name = name
        self.s = s
        self.t = t
        self.answer = answer

    def __str__(self) -> str:
        return 'task10_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        s='84532',
        t='34852',
        answer=True,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task10(case: Case) -> None:
    answer = task10(
        s=case.s,
        t=case.t,
    )
    assert answer == case.answer
