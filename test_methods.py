import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    a = 5
    b = 8

    output = methods.soma(a,b)

    assert output == 13


def test_multiplicacao():
    a = 7
    b = 9

    output = methods.multiplicacao(a,b)

    assert output == 63

def test_elevaQuadrado():
    a = 8

    output = methods.elevaQuadrado(a)

    assert output == 64

def test_divisao():
    a = 12
    b = 2

    output = methods.divisao(a,b)

    assert output == 6

def test_subtrai():
    a = 9
    b = 3

    output = methods.subtrai(a,b)

    assert output == 6