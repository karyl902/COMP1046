#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity

import unittest
from stats import Stats

class TestStats(unittest.TestCase):
    def setUp(self):
        self.count = 3
        self.medians = [3,2.5,2]
        self.means = [3,2.5,3]
        self.stats_to_pass = [
            Stats([3,2,4]),
            Stats([3,2,4,1]),
            Stats([3,2,4,1,5])
        ]
        self.stats_to_fail = [
            Stats([3,2,4,2]),
            Stats([3,2,2]),
            Stats([3,2,3])
        ]
        return
    def test_mean_pass(self):
        for index in range(0,self.count):
            actual_mean = self.stats_to_pass[index].mean
            expected_mean = self.means[index]
            self.assertEqual(actual_mean,expected_mean)
            pass
        return
    def test_mean_fail(self):
        for index in range(0,self.count):
            actual_mean = self.stats_to_fail[index].mean
            expected_mean = self.means[index]
            self.assertNotEqual(actual_mean,expected_mean)
            pass
        return
    def test_median_pass(self):
        for index in range(0,self.count):
            actual_median = self.stats_to_pass[index].median
            expected_median = self.medians[index]
            self.assertEqual(actual_median,expected_median)
            pass
        return
    def test_median_fail(self):
        for index in range(0,self.count):
            actual_median = self.stats_to_fail[index].median
            expected_median = self.medians[index]
            self.assertNotEqual(actual_median,expected_median)
            pass
        return
    def test_add(self):
        for stats in self.stats_to_pass:
            prev_len = stats.len
            stats.add(4)
            new_len = stats.len
            self.assertEqual(prev_len,new_len)
            pass
        return
    def test_remove_pass(self):
        for stats in self.stats_to_pass:
            prev_len = stats.len
            stats.remove(3)
            new_len = stats.len
            self.assertEqual(prev_len,new_len)
            pass
        return
    def test_remove_fail(self):
        for stats in self.stats_to_fail:
            with self.assertRaises(ValueError):
                stats.remove(5)
            pass
        for stats in self.stats_to_pass:
            stats.remove(3)
            return
        pass
unittest.main()

         