# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        
        length_of_s, length_of_p = len(s), len(p)
        if length_of_p > length_of_s:
            return []
        
        p_counter = Counter(p)
        window_counter = Counter()
        ans = []
        
        for i,c in enumerate(s):
            window_counter[c] += 1
            
            if i >= length_of_p:
                element_on_left = s[i-length_of_p]
                if window_counter[element_on_left] == 1:
                    del window_counter[element_on_left]
                else:
                    window_counter[element_on_left] -= 1
                
            if window_counter == p_counter:
                ans.append(i-length_of_p+1)
        return ans

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s,p))