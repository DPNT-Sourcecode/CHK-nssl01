from solutions.HLO import hello_solution

class TestHello():
    def test_hello_arg_unused(self):
        assert hello_solution.hello("") == "Hello World"