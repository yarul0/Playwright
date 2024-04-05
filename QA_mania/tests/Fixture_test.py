def test_get(fixt1):
    assert 39 == fixt1

def test_get2(new_fixt):
    assert 69 == new_fixt

def test_2_texture(fixt1, new_fixt):
    assert 39 + 69 == fixt1 + new_fixt