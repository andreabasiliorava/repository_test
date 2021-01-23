from hypothesis import given, example
import hypothesis.strategies as st

from functions import encode
from functions import decode


@given(s=st.text())
@example(s='')
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s