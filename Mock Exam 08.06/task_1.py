kindergarten = input()
kids = int(input())
spots = int(kindergarten[-2:])
max_points = 0
other = []
accepted = []


if spots > 0:

    first_name = input().split(' ')
    first_kid = first_name[0]
    first_kid_points = int(first_name[1])

    for child in range(kids-1):
        name = input().split(" ")
        kid_points = int(name[1])
        kid_name = name[0]

        if first_kid_points < kid_points:
            accepted.insert(0, first_kid)
            first_kid_points = kid_points
            first_name = kid_name
        else:
            accepted.append(first_name)

    accepted.extend(other)
    result = accepted[:spots]
    result2 = accepted[spots:]
