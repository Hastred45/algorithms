def canConstruct(ransomNote, magazine):
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

seq_a = 'aaaj'
seq_b = 'bajawa'

print(canConstruct(seq_a, seq_b))