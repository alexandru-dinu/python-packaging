import hello_world


def test_say_hello():
    assert hello_world.hello("alex") == "Hello, Alex!"


def test_random_number():
    assert 0 <= hello_world.random_number() <= 1
