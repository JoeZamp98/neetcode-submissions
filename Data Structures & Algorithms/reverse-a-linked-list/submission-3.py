# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize the current node at the head, and the previous node as none (in the forward running list, the "None" next node should be at the end, so it's inverted here)
        curr_node = head
        prev_node = None

        # Continue in the loop while a valid current node exists
        while curr_node:
            # Create a placeholder for the next node in the original list
            next_node = curr_node.next

            #Reverse the direction of the relationship between the current and previous nodes.  For the first node, this will point at None
            curr_node.next = prev_node
            
            # Increment the pointers - the previous node first shifts up to current, and then the current node is moved to the next node from the placeholder (since we already modified the direction of the pointer on the node itself)
            prev_node = curr_node
            curr_node = next_node

        # Since the while loop breaks when curr_node is None, we'll use the final previous node as the new head
        return prev_node

