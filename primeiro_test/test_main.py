def incrementacao(x):
    return x + 1

def decrementacao(x):
    return x - 1

def functions(func, x):
    return func(x)

# Função Teste
def test_inc():
    assert functions(incrementacao, 2) == 3

def test_dec():
    assert functions(decrementacao, 2) == 1