# PART B-- THE MODULE

# Function a

##Formats the code into two collumns and prints it in a table like format.

def table_print(headers, data, width=10):
    output = "{:<{}} {:<{}}"

    print(output.format(headers[0], width, headers[1], width))

    print("-" * (width + 1) * 2)

    for item1, item2 in data:
        print(output.format(item1, width, item2, width))
    print()

# Function b

##Sorts the values in descedning order.

def insertion_sort(values, pos):
    for i in range(1, len(values)):
        j = i
        while j > 0 and values[i][pos] < values[j-1][pos]:
            j -= 1
        values.insert(j,values.pop(i))

# Function c

##Tallies the data as there are multiple instances of the similar data within the nested list. This solves that and brings each related together into a singular piece.

def tallied_data(user_list, col_query, col_tally):
    temp = {}
    for row in user_list:
        if row[col_query]  in temp:
            temp[row[col_query]] += int(row[col_tally])
        else:
            temp[row[col_query]] = int(row[col_tally])

    data = list(temp.items())
    insertion_sort(data, 1)
    data.reverse()
                
    return data

