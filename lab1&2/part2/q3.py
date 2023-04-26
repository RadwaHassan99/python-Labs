def are_all_numbers_unique(seq):
    return len(seq) == len(set(seq))


seq1 = [1, 5, 7, 9]
seq2 = [2, 4, 5, 5, 7, 9]

print(are_all_numbers_unique(seq1))  # Output: True
print(are_all_numbers_unique(seq2))  # Output: False
