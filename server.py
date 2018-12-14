from bottle import route, run, template, request, get, static_file

# import csv
# import pprint
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.ticker import FuncFormatter
# from collections import OrderedDict
# from collections import Counter
#
# from collections import defaultdict

sits = 0

@route('/chair/<chair_id>')
def rpi(chair_id):
    global sits
    print(f"Received from chair {chair_id}")
    sits += 1
    return


@route('/')
def index():
    return template('index', count=sits if sits < 24 else 24)


@get('/get_count')
def get_count():
    return str(sits)


@get('/css/<filename>')
def stylesheets(filename):
    return static_file(filename, root='css/')


@get('/js/<filename>')
def js(filename):
    return static_file(filename, root='js/')


@get('/webfonts/<filename>')
def js(filename):
    return static_file(filename, root='webfonts/')


@get('/imgs/<filename>')
def js(filename):
    return static_file(filename, root='imgs/')

# def humphery_data():
#     columns = defaultdict(list)  # each value in each column is appended to a list
#
#     with open('example.csv') as f:
#         reader = csv.DictReader(f)  # read rows into a dictionary format
#         for row in reader:  # read a row as {column1: value1, column2: value2,...}
#             for (k, v) in row.items():  # go over each column name and value
#                 columns[k].append(v)  # append the value into the appropriate list
#                 # based on column name k
#     group_data = columns['value']
#     group_names = columns['name']
#     fig, ax = plt.subplots()
#     b = ax.barh(group_names, group_data, color='#6699CC')
#     # for rect in b:
#     #     w=rect.get_width()
#     #     ax.text(w,rect.get_y()+rect.get_height()/2,'%d'%int(w),ha='left',va='center')
#     ax.set_yticks(range(len(group_names)))
#     ax.set_yticklabels(group_names)
#     plt.show()
#     # print(columns['name'])
#     # print(columns['value'])
#     # group_data = list(data[]['value'])
#     # group_names = list(data[]['name'])
#     # group_mean = np.mean(group_data)
#     # fig, ax = plt.subplots()
#     # ax.barh(group_names, group_data)


run(host='', port=8080)
