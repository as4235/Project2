def test_add():
    from calc import calc
    assert calc.add(1,1) == 2

def test_add_fail():
    from calc import calc
    assert calc.add(1,1) != 3

def test_sub():
    from calc import calc
    assert calc.sub(2,2) == 0

def test_sub_fail():
    from calc import calc
    assert calc.sub(3,1) != 1

def test_mul():
    from calc import calc
    assert calc.mul(2,5) == 10

def test_mul_fail():
    from calc import calc
    assert calc.sub(3,6) != 9

def test_div():
    from calc import calc
    assert calc.div(2,2) == 1

def test_div_fail():
    from calc import calc
    assert calc.div(3,1) != 1

def test_sq():
    from calc import calc
    assert calc.sq(2) == 4

def test_sq_fail():
    from calc import calc
    assert calc.sq(3) != 1

def test_rt():
    from calc import calc
    assert calc.rt(4) == 2

def test_rt_fail():
    from calc import calc
    assert calc.rt(9) != 1