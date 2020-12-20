from DS import ListNode


class Solution:
    def detectCycle_one(self, head: ListNode) -> ListNode:
        """
        Intuitive solution, simply check if the value has been seen
        """
        visited = set()  # node: index
        ptr = head
        while ptr:
            if ptr in visited:
                return ptr
            else:
                visited.add(ptr)
                ptr = ptr.next
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        """
        From the two pointer solution of Linked List Cycle
        The solution is from https://leetcode.com/problems/linked-list-cycle-ii/discuss/44793/O(n)-solution-by-using-two-pointers-without-change-anything
        If found a meeting point, one pointer start from the start, the other pointer starts from the meeting point
        the next time them meet, it is the head of the cycle
        """
        if not head:
            return
        slow = fast = head
        counter = 0
        found = False
        while fast and fast.next:
            counter += 1
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                found = True
                break

        if found:  # if a cycle is found after counter iterations
            head_finder = head
            while slow != head_finder:
                slow = slow.next
                head_finder = head_finder.next
            return head_finder
        else:
            return None


if __name__ == '__main__':
    import DS

    arr = [3, 2, 0, -4]
    head = DS.arr2LinkedNode(arr)
    start = head.next
    i = head
    while i.next:
        i = i.next
    i.next = start
    sol = Solution()
    ans = sol.detectCycle(head)
    print(ans.val)