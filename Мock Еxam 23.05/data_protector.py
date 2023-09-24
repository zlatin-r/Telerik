sequence1 = input().split()
sequence2 = input().split()
instructions = input().split(', ')

for instruction in instructions:
    start, end = map(int, instruction.split())

    if start > end:
        sequence1[:end+1], sequence2[:end+1] = sequence2[:end+1], sequence1[:end+1]
        sequence1[start:], sequence2[start:] = sequence2[start:], sequence1[start:]
    else:
        sequence1[start:end + 1], sequence2[start:end + 1] = sequence2[start:end + 1], sequence1[start:end + 1]

print(' '.join(sequence1))
print(' '.join(sequence2))