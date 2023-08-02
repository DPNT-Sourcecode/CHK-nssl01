from solutions.CHK import checkout_solution

class TestA():
    def test_a(self):
        expected = {
            "A": 50,
            "AA": 100,
            # 3 for 130
            "AAA": 130,
            # 3 for 130 + 1 for 50
            "AAAA": 180,
            # 5 for 200
            "AAAAA": 200,
            # 8 for 200 + 3 for 130
            "AAAAAAAA": 330
        }


        for input, price in expected.items():
            a = checkout_solution.ItemA(amount=len(input))
            assert(a.total_price() == price)

class TestB():
    def test_b(self):
        expected = {
            "B": 30,
            ## 2 B for 45
            "BB": 45,
            # 3 for 30 + 45
            "BBB": 75,
            # 4 for 45 + 45
            "BBBB": 90,
            # 5 for 45 + 45 + 30
            "BBBBB": 120,
            # 8 45 * 4
            "BBBBBBBB": 180
        }


        for input, price in expected.items():
            b = checkout_solution.ItemB(amount=len(input))
            assert(b.total_price() == price)

class TestC():
    def test_c(self):
        for i in range(5):
            c = checkout_solution.ItemC(amount=i)
            assert(c.total_price() == i * 20)

class TestD():
    def test_d(self):
        for i in range(5):
            d = checkout_solution.ItemD(amount=i)
            assert(d.total_price() == i * 15)


class TestE():
    def test_e(self):
        for i in range(5):
            e = checkout_solution.ItemE(amount=i)
            assert(e.total_price() == i * 40)

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

    def test_two_e(self):
        assert(checkout_solution.checkout("EE") == 80)

    def test_e_deal(self):
        # (40 + 40) + 0 (B is free)
        assert(checkout_solution.checkout("EEB") == 80)

    def test_e_deal_with_2_b(self):
        # (40 + 40) + 30 + 0 (one B is free)
        # always favour the customer, so 2B gets the deal + one free?
        # E: 40
        # E: 40
        # 2B: 30 + 30, but with the E deal... 45 - 30?
        # checkout should always return an int, so no 45/2
        assert(checkout_solution.checkout("EEBB") == 95)

    def test_all(self):
        # Assume input is like: "ABCABC" maybe?
        assert(checkout_solution.checkout("ABCDE") == 155)

    def test_empty_string(self):
        assert(checkout_solution.checkout("") == 0)

    def test_invalid(self):
        assert(checkout_solution.checkout("F") == -1)

    def test_wrong_type(self):
        assert(checkout_solution.checkout(0) == -1)

    def test_failed(self):
        assert(checkout_solution.checkout("EEEEBB") == 160)

    def test_2_failed(self):
        assert(checkout_solution.checkout("BEBEEE") == 160)

    def test_3_failed(self):
        # Rerranged, AA BB CC DD EE
        # 2A: 100
        # 2B: (45 - 30) 15
        # 2C: 40
        # 2D: 30
        # 2E: 80
        # total: 265?
        # E deal is considered before B's deal runs
        assert(checkout_solution.checkout("ABCDEABCDE") == 280)


# - {"method":"checkout","params":["BEBEEE"],"id":"CHK_R2_027"}, expected: 160, got: 145
#  - {"method":"checkout","params":["ABCDEABCDE"],"id":"CHK_R2_038"}, expected: 280, got: 265






