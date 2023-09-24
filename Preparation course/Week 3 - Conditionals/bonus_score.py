score = int(input())

if 1 <= score <= 3:
    score *= 10
elif 4 <= score <= 6:
    score *= 100
elif 6 <= score <= 9:
    score *= 1000
else:
    score = "invalid score"

print(score)