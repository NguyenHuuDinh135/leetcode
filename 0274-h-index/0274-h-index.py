class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Có nghĩa là trong các bài báo có trích dẫn thì nó trích dẫn ít nhất h lần
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1 :
                h = i + 1
            else: 
                break
        return h