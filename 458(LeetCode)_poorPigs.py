import imp
from math import *
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        
        T = minutesToTest/minutesToDie
        return int(ceil(log(buckets)/log(T+1)))