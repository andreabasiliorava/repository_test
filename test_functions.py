from hypothesis import given
import hypothesis.strategies as st

from functions import encode
from functions import decode


@given(st.text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s