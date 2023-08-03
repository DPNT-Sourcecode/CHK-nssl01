from solutions.CHK.checkout_solution import checkout

# class TestShop():
#     def test_add_item(self):
#         shop = checkout_solution.Shop()
#         to_add = checkout_solution.Item()
#         shop.add_item()

# class TestA():
#     def test_a(self):
#         expected = {
#             "A": 50,
#             "AA": 100,
#             # 3 for 130
#             "AAA": 130,
#             # 3 for 130 + 1 for 50
#             "AAAA": 180,
#             # 5 for 200
#             "AAAAA": 200,
#             # 8 for 200 + 3 for 130
#             "AAAAAAAA": 330
#         }


#         for input, price in expected.items():
#             a = checkout_solution.ItemA(amount=len(input))
#             assert(a.total_price() == price)

# class TestB():
#     def test_b(self):
#         expected = {
#             "B": 30,
#             ## 2 B for 45
#             "BB": 45,
#             # 3 for 30 + 45
#             "BBB": 75,
#             # 4 for 45 + 45
#             "BBBB": 90,
#             # 5 for 45 + 45 + 30
#             "BBBBB": 120,
#             # 8 45 * 4
#             "BBBBBBBB": 180
#         }


#         for input, price in expected.items():
#             b = checkout_solution.ItemB(amount=len(input))
#             assert(b.total_price() == price)

# class TestC():
#     def test_c(self):
#         for i in range(5):
#             c = checkout_solution.ItemC(amount=i)
#             assert(c.total_price() == i * 20)

# class TestD():
#     def test_d(self):
#         for i in range(5):
#             d = checkout_solution.ItemD(amount=i)
#             assert(d.total_price() == i * 15)


# class TestE():
#     def test_e(self):
#         for i in range(5):
#             e = checkout_solution.ItemE(amount=i)
#             assert(e.total_price() == i * 40)


# class TestF():
#     def test_f(self):
#         expected = {
#             "F": 10,
#             "FF": 20,
#             # 3 for 2
#             "FFF": 20,
#             # 3 for 2 + 1
#             "FFFF": 30,
#             # 3 for 2 + 2
#             "FFFFF": 40,
#             # 6 for 4 (2 * 3 for 2)
#             "FFFFFF": 40,
#         }


#         for input, price in expected.items():
#             f = checkout_solution.ItemF(amount=len(input))
#             assert(f.total_price() == price)


class TestCheckout:
    def test_one_a(self):
        assert checkout("A") == 50

    def test_two_a(self):
        assert checkout("AA") == 100

    def test_three_a(self):
        assert checkout("AAA") == 130

    def test_five_a(self):
        assert checkout("AAAAA") == 200

    def test_one_b(self):
        assert checkout("B") == 30

    def test_two_b(self):
        assert checkout("BB") == 45

    def test_three_b(self):
        assert checkout("BBB") == 75

    def test_c(self):
        assert checkout("C") == 20

    def test_d(self):
        assert checkout("D") == 15

    def test_e(self):
        assert checkout("E") == 40

    def test_two_e(self):
        assert checkout("EE") == 80

    def test_e_deal(self):
        # (40 + 40) + 0 (B is free)
        assert checkout("EEB") == 80

    def test_e_deal_with_2_b(self):
        # E: 40
        # E: 40
        # 2B: 30 + 0 (one is free)
        assert checkout("EEBB") == 110

    def test_f(self):
        expected = {
            "F": 10,
            "FF": 10,
            "FFF": 20,
            "FFFF": 20,
        }

        for input, price in expected.items():
            assert checkout(input) == price

    def test_h(self):
        expected = {
            "H": 10,
            "H" * 2: 20,
            "H" * 3: 30,
            "H" * 4: 40,
            "H" * 5: 45,
            # 5H for 45 + 3 * 10 = 75
            "H" * 8: 75,
            "H" * 10: 80,
        }

        for input, price in expected.items():
            assert checkout(input) == price

    def test_k(self):
        expected = {
            "K": 80,
            "K" * 2: 150,
            "K" * 3: 230,
            "K" * 4: 300,
        }

        for input, price in expected.items():
            assert checkout(input) == price

    def test_n(self):
        assert checkout("NNN") == 120
        assert checkout("NNNM") == 120

    # 3R get one Q free
    def test_r(self):
        # 50 * 3 + 30
        assert checkout("RRR") == 150
        assert checkout("RRRQ") == 150
        assert checkout("RRRQQ") == 180

    def test_u(self):
        # 50 * 3 + 30
        assert checkout("U") == 40
        assert checkout("UU") == 80
        assert checkout("UUU") == 80
        assert checkout("UUUU") == 120

    def test_all(self):
        # Assume input is like: "ABCABC" maybe?
        assert checkout("ABCDEF") == 165

    def test_empty_string(self):
        assert checkout("") == 0

    def test_invalid(self):
        assert checkout(">") == -1

    def test_wrong_type(self):
        assert checkout(0) == -1

    # Previous failed tests
    def test_failed(self):
        assert checkout("EEEEBB") == 160

    def test_2_failed(self):
        assert checkout("BEBEEE") == 160

    def test_3_failed(self):
        # Rerranged, AA BB CC DD EE
        # 2A: 100
        # 2B: (45 - 30) 15
        # 2C: 40
        # 2D: 30
        # 2E: 80
        # total: 265?
        # E deal is considered before B's deal runs
        assert checkout("ABCDEABCDE") == 280

    def test_deploy_4_failed_1(self):
        assert (checkout("UUU") == 120)


