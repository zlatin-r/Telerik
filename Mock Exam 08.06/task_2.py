large_piece_width = int(input())
large_piece_height = int(input())
small_piece_width = int(input())
small_piece_height = int(input())

h = large_piece_height // small_piece_width
v = large_piece_width // small_piece_height

result = max(h, v)

print(result)