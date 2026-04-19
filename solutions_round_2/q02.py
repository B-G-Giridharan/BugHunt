def create_multipliers():
    return [lambda x, i=i: x * i for i in range(3)]

def test_multipliers():
    funcs = create_multipliers()
    return [f(10) for f in funcs]

print(test_multipliers(), flush=True)