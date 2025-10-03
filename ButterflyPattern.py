rows = 3

# Upper part
for i in range(1, rows + 1):
    print("* " * i + "  " * (rows - i) * 2 + "* " * i)

# Lower part
for i in range(rows - 1, 0, -1):
    print("* " * i + "  " * (rows - i) * 2 + "* " * i)
