from solutions.CHK import checkout_solution



class TestCheckout():
    def test_one_a(self):
        assert(checkout_solution.checkout("A") == 50)

    def test_two_a(self):
        assert(checkout_solution.checkout("AA") == 100)

    def test_three_a(self):
        assert(checkout_solution.checkout("AAA") == 130)

    def test_five_a(self):
        assert(checkout_solution.checkout("AAAAA") == 200)

    def test_one_b(self):
        assert(checkout_solution.checkout("B") == 30)

    def test_two_b(self):
        assert(checkout_solution.checkout("BB") == 45)

    def test_three_b(self):
        assert(checkout_solution.checkout("BBB") == 75)

    def test_c(self):
        assert(checkout_solution.checkout("C") == 20)

    def test_d(self):
        assert(checkout_solution.checkout("D") == 15)

    def test_e(self):
        assert(checkout_solution.checkout("E") == 40)

    def test_e_deal(self):
        # (40 + 40) + 0 (B is free)
        assert(checkout_solution.checkout("EEB") == 80)

    # def test_all(self):
    #     # Assume input is like: "ABCABC" maybe?
    #     assert(checkout_solution.checkout("ABCD") == 115)

    # def test_empty_string(self):
    #     assert(checkout_solution.checkout("") == 0)

    # def test_invalid(self):
    #     assert(checkout_solution.checkout("F") == -1)

    # def test_wrong_type(self):
    #     assert(checkout_solution.checkout(0) == -1)


