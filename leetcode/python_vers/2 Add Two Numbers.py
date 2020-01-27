"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

The pseudocode is as following:
- Initialize current node to dummy head of the returning list.
- Initialize carry to 0.
- Initialize p and q to head of l1 and l2 respectively.
- Loop through lists l1 and l2 until you reach both ends.
    - Set x to node p's value. If p has reached the end of l1, set to 0.
    - Set y to node q's value. If q has reached the end of l2, set to 0.
    - Set sum = x + y + carry.
    - Update carry = sum / 10.
    - Create a new node with the digit value of (sum mod 10) and set it to current node's next, then advance current node to next.
    - Advance both p and q.
- Check if carry = 1, if so append a new node with digit 1 to the returning list.
- Return dummy head's next node.
"""

# Definition for singly-linked list node.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list
class LinkedList(object):
    """Singly-linked list
            (len) -> (val0) -> (val1) -> ...
        :head [ListNode] Stores the length of the LinkedList.
        :len [int] Length of the LinkedList.
    """
    def __init__(self):
        self.head = ListNode(0)
        self.len = self.head.val

    def init_with_vals(self, vals):
        """Given values and initialize a linked list.
           :vals [iterable] Values to be stored in the lined list.
           :return [ListNode] Head node.
        """
        if len(vals) == 0:
            return self.head
        p, q = self.head, ListNode(vals[0])
        for i, val in enumerate(vals[1:]):
            p.next = q
            q = ListNode(val)
            p = p.next
            self.head.val += 1
        p.next = q
        self.head.val += 1
        return self.head

    def push(self, val):
        """Push a ListNode to the end of the LinkedList
            :val [any type]
        """
        p = self.head
        while p.next:
            p = p.next
        p.next = ListNode(val)
        self.head.val += 1

    def push_vals(self, vals):
        """Push multiple ListNodes to the end of the LinkedList
            :vals [iterable]
        """
        for i, val in enumerate(vals):
            self.push(val)
        return self.head

    def print_nodes(self):
        """Display the structure of LinkedList
        """
        node = self.head
        print("(%d): " %(node.val), end="")
        node = node.next
        while node.next:
            print('%d -> ' %(node.val), end="")
            node = node.next
        print("%d" %(node.val))

# Solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_node = ListNode(1)
        cur_node = head_node
        carry = 0
        p, q = l1, l2
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10
            new_node = ListNode(sum % 10)
            cur_node.next = new_node
            cur_node = new_node
            p = p.next if p else None
            q = q.next if q else None
        if carry == 1:
            new_node = ListNode(1)
            cur_node.next = new_node
        return head_node.next

if __name__=="__main__":
    l1 = LinkedList().init_with_vals([2, 4, 3])
    l2 = LinkedList().init_with_vals([5, 6, 4])
    s = Solution().addTwoNumbers(l1.next, l2.next)
    while s.next:
        print("%d -> " %(s.val), end="")
        s = s.next
    print("%d" %(s.val))
    # 7 -> 0 -> 8
