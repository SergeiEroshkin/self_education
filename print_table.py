
table_data = [['apples', 'oranges', 'cherries','banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
def printTable(argument):
    col_widths = [0] * len(table_data)
    col_widths[0] = max([len(x) for x in table_data[0]])
    col_widths[1] = max([len(x) for x in table_data[1]])
    col_widths[2] = max([len(x) for x in table_data[2]])
    for item in range(4):
        print argument[0][item].rjust(max(col_widths)) + argument[1][item].rjust(max(col_widths)) + \
              argument[2][item].rjust(max(col_widths))


print printTable(table_data)