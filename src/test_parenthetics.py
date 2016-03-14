# -*- coding: utf-8 -*-

import pytest


TEST_CASES = [
    ("string ()( ( fdf)) ( asdfasdfasd))() ()asdff) )fdafdsf )(dfsasd( ( )) )string", -1),
    ("string ) ) ))))) ) ) )))))() ()() ()) ) ))) )))string", -1),
    ("(((", 1),
    ("(bla bla (bla bla bla) (bla bla bla bla)", 1),
    ("(", 1),
    ("", 0),
    ("This should be a (big fat) zero", 0),

]

@pytest.mark.parametrize('input, output', TEST_CASES)
def test_balanced(input, output):
    from parenthetics import paren_check
    assert paren_check(input) == output
