/*
思路：通过字典统计两个字符串中各个字符出现的频率，最后通过比较字典是否相等得出结果。
*/

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return Counter(s) == Counter(t)
        
/*
思路：先排序，后比较。sorted()函数对所有可迭代的对象进行排序操作。其与sort()的区别是：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
*/
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return return sorted(s) == sorted(t)
