class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split() automatically removes leading/trailing whitespace
        # and collapses multiple spaces into a single separator
        words = s.split()
             # Reverse the list of words and join them with a single space
        return " ".join(words[::-1])