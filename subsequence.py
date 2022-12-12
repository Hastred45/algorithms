def subsequence(substring, whole_line):
    position = -1
    for i in substring:
        position = whole_line.find(i, position + 1)
        if position == - 1:
            return False
    return True


substring = input()
whole_line = input()

print(subsequence(substring, whole_line))
