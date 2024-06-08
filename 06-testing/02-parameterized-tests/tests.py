import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string1', [
    ('((()))'),
    ('()'),
    ('(((((((((((((((((((((((())))))))))))))))))))))))'),
    ('()()')
])

def test_matching_parantheses_are_true(string1):
    assert matching_parentheses(string1) , f'Parantheses in string:\n {string1}\n Are all correctly closed'

@pytest.mark.parametrize('string2',[
    ('(()'),
    ('('),
    ('(((((((((((((((((((((((('),
    (')(')
])

def test_matching_parantheses_are_false(string2):
    assert not matching_parentheses(string2), f'Parantheses in string:\n {string2}\n Are not correctly closed'