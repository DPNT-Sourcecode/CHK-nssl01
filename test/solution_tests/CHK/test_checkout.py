from solutions.CHK import checkout_solution



class TestCheckout():
    def test_price(self):
        # Assume input is like: "ABCABC" maybe?
        assert(checkout_solution.checkout("ABC") == 100)
