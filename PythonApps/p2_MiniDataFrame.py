def load_CSV(file_path):
    with open(file_path, 'r') as f:
        header = f.readline().strip().split(',')
        def key_func(value):
            try:
                return float(value)
            except ValueError:
                return value
        # zip creates a tuple of (header, value) pairs for each line
        # dict casts them as (key, value)
        data = [dict(zip(header, [key_func(val) for val in line.strip().split(',')])) for line in f.readlines() if line]
    return data

def filter_data(data, column, value):
    return [row for row in data if row[column] == value]

def sort_data(data, column):
    sorted_rows = sorted(data, key = lambda r:r[column])
    return sorted_rows

#Here I return a column if no index provided or a dict if there is one
def select_column(data, column, indicies = None):
    if not indicies:
        return [x[column] for x in data]
    else:
        return [{"id":x[indicies],"value":x[column]} for x in data]

def get_Mean(data, column):
    calc_column = select_column(data, column)
    mean = 0 
    try:
        mean = sum(calc_column)/len(calc_column)
    except Exception as e:
        print(e)
        return None
    return mean

def save_CSV(data, path):
    header = list(data[0].keys())
    lines = []
    lines.append(",".join(header))
    for row in data:
        lines.append(",".join([str(row[k]) for k in header]))
        
    with open(path, 'w') as f:
        f.write("\n".join(lines))

#currently I don't know what does group by exactly do
#but this is more for learning data structer so it's good for now
class Group:
    def __init__(self, data, columns):
        self.group = {}
        groupKies = [row[columns[0]] for row in data]
        groupValues = columns[1:]
        self.group = {key:[] for key in set(groupKies)}
        for row in data:
            self.group[row[columns[0]]].append({x:row[x] for x in groupValues})
    def get_sum(self, column):
       return { groupedKey:sum([x[column] for x in groupedValDics]) for groupedKey, groupedValDics in self.group.items() }

    def get_mean(self, column):
        sum = self.get_sum(column)
        return {k:sum[k]/len(self.group[k]) for k in self.group}


# Testing
data = load_CSV('data/testCSV.csv')
save_CSV(select_column(sort_data(data, "name"),'name','id'), 'data/testOutCSV.csv')
#print(select_column(sort_data(data, "name"),'name')) ##print column of sorted Names
#print(get_Mean(data,"age")) print mean of age
#print(Group(data, ['city','age', 'name']).group) #print grouped data
print(Group(data, ['city','age']).get_mean('age')) #Get mean age for each city