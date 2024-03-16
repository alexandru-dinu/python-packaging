from hello_world import hello


def test_say_hello():
    assert hello.say_hello("alex") == "Hello, Alex!"


def test_random_number():
    assert 0 <= hello.get_random_number() <= 1
