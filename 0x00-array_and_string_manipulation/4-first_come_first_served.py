#!/usr/bin/python3

import unittest


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    """ Check if we're serving orders first-come, first-served """
    take_order_size = len(take_out_orders)
    dine_in_order_size = len(dine_in_orders)
    served_order_size = len(served_orders)

    if served_order_size != take_order_size + dine_in_order_size:
        return False

    index_take_out_order = 0
    index_dine_in_order = 0
    index_served_order = 0

    for index_served_order in range(served_order_size):
        take_order_done = index_take_out_order >= take_order_size
        dine_in_order_done = index_dine_in_order >= dine_in_order_size

        
        if not take_order_done and served_orders[index_served_order] == take_out_orders[index_take_out_order]:
            index_take_out_order += 1

        elif not dine_in_order_done and served_orders[index_served_order] == dine_in_orders[index_dine_in_order]:
            index_dine_in_order += 1

        else:
            return False
        
        index_served_order += 1
 
    return True



# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)
