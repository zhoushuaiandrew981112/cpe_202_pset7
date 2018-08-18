from pset7 import *

import unittest

class Test_Pset7(unittest.TestCase):

    def test_insertion_sort(self):
        act_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = insertion_sort(act_lst)
        exp_tup = (0, 0)
        self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [1, 0, 2]
        exp_lst = [0, 1, 2]
        act_tup = insertion_sort(act_lst)
        exp_tup = (1, 1)
        self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)
        
        act_lst = [1, 2, 3, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = insertion_sort(act_lst)
        exp_tup = (3, 3)
        self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = insertion_sort(act_lst)
        exp_tup = (45, 45)
        self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = insertion_sort(act_lst)
        exp_tup = (6, 6)
        self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

    def test_selection_sort(self):

        act_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = selection_sort(act_lst)
        #exp_tup = (45, 10)
        #self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [1, 0, 2]
        exp_lst = [0, 1, 2]
        act_tup = selection_sort(act_lst)
        #exp_tup = (3, 3)
        #self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)
        
        act_lst = [1, 2, 3, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = selection_sort(act_lst)
        #exp_tup = (6, 4)
        #self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = selection_sort(act_lst)
        #exp_tup = (45, 10)
        #self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = selection_sort(act_lst)
        #exp_tup = (6, 4)
        #self.assertEqual(act_tup, exp_tup)
        self.assertEqual(act_lst, exp_lst)

    def test_bubble_sort(self):

        act_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = bubble_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [1, 0, 2]
        exp_lst = [0, 1, 2]
        act_tup = bubble_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)
        
        act_lst = [1, 2, 3, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = bubble_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = bubble_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = bubble_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

    def test_qiuck_sort(self):

        l = [0, 1, 2, 3]
        i = partition(l, 0, len(l) - 1)
        self.assertEqual(i[0], 3)

        l = [3, 4, 1, 0, 2, 5]
        i = partition(l, 0, len(l) - 1)
        self.assertEqual(i[0], 5)

        l = [1, 3, 2, 5, 6, 4]
        i = partition(l, 0, len(l) - 1)
        self.assertEqual(i[0], 3)
 
        l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        i = partition(l, 0, len(l) - 1)
        self.assertEqual(i[0], 0)

        l = [0, 2, 4, 6, 1, 3, 5, 7]
        i = partition(l, 0, len(l) - 1)
        self.assertEqual(i[0], 7)

        act_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        c_s = quick_sort_helper(act_lst, 0, len(act_lst) - 1, 0, 0)
        self.assertEqual(c_s, (45, 54))

        act_lst = [1, 0, 2]
        c_s = quick_sort_helper(act_lst, 0, len(act_lst) - 1, 0, 0)
        self.assertEqual(c_s, (3, 4))

        act_lst = [1, 2, 3, 0]
        c_s = quick_sort_helper(act_lst, 0, len(act_lst) - 1, 0, 0)
        self.assertEqual(c_s, (6, 3))

        act_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        c_s = quick_sort_helper(act_lst, 0, len(act_lst) - 1, 0, 0)
        self.assertEqual(c_s, (45, 29))

        act_lst = [3, 2, 1, 0]
        c_s = quick_sort_helper(act_lst, 0, len(act_lst) - 1, 0, 0)
        self.assertEqual(c_s, (6, 5))

        act_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = quick_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [1, 0, 2]
        exp_lst = [0, 1, 2]
        act_tup = quick_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)
        
        act_lst = [1, 2, 3, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = quick_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        act_tup = quick_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3]
        act_tup = quick_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

    def test_merge_sort(self):

        act_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        c_s = merge(act_lst, [], [])
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_l_r(act_lst, [], [], 0, 0, 0, 0, 0)
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_sort_helper(act_lst)
        self.assertEqual(c_s, (34, 34)) 
        act_tup = merge_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [1, 0, 2]
        exp_lst = [0, 1, 2]
        c_s = merge(act_lst, [], [])
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_l_r(act_lst, [], [], 0, 0, 0, 0, 0)
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_sort_helper(act_lst)
        c_s = merge_sort_helper(act_lst)
        self.assertEqual(c_s, (5, 5)) 
        act_tup = merge_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)
        
        act_lst = [1, 2, 3, 0]
        exp_lst = [0, 1, 2, 3]
        c_s = merge(act_lst, [], [])
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_l_r(act_lst, [], [], 0, 0, 0, 0, 0)
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_sort_helper(act_lst)
        c_s = merge_sort_helper(act_lst)
        self.assertEqual(c_s, (8, 8)) 
        act_tup = merge_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        c_s = merge(act_lst, [], [])
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_l_r(act_lst, [], [], 0, 0, 0, 0, 0)
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_sort_helper(act_lst)
        c_s = merge_sort_helper(act_lst)
        self.assertEqual(c_s, (34, 34)) 
        act_tup = merge_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)

        act_lst = [3, 2, 1, 0]
        exp_lst = [0, 1, 2, 3]
        c_s = merge(act_lst, [], [])
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_l_r(act_lst, [], [], 0, 0, 0, 0, 0)
        self.assertEqual(c_s, (0, 0)) 
        c_s = merge_sort_helper(act_lst)
        c_s = merge_sort_helper(act_lst)
        self.assertEqual(c_s, (8, 8)) 
        act_tup = merge_sort(act_lst)
        self.assertEqual(act_lst, exp_lst)





if __name__ == "__main__":
    unittest.main() 
