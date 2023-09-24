number_targets = int(input())

G_speed = float(input()) * number_targets
G_latency = float(input()) * 2
P_speed = float(input()) * number_targets
P_latency = float(input()) * 2

G_time = G_speed + G_latency
P_time = P_speed + P_latency

if G_time < P_time:
    print("George")
elif P_time < G_time:
    print("Peter")
elif G_time == P_time:
    print("Draw")
