def isPalindrome(head) -> bool:
        reversed_head = head[::-1]
        if head == reversed_head:
            return True
        else:
            return False

print(isPalindrome('azz'))