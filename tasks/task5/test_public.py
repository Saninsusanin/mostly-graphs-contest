import pytest

from .task import task5


class Case:
    def __init__(self, name: str, expression: str, answer: bool):
        self._name = name
        self.expression = expression
        self.answer = answer

    def __str__(self) -> str:
        return 'task5_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='case1',
        expression='|(&(1,0,1),!(1))',
        answer=False,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task5(case: Case) -> None:
    answer = task5(
        expression=case.expression,
    )
    assert answer == case.answer
