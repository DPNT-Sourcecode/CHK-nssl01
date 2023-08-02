from solutions.CHK import checkout_solution



class TestCheckout():
    def test_one_a(self):
        assert(checkout_solution.checkout("A") == 50)

    def test_price(self):
        # Assume input is like: "ABCABC" maybe?
        assert(checkout_solution.checkout("ABC") == 100)

    def test_invalid(self):
        assert(checkout_solution.checkout("F") == -1)

