def run():
    my_list = [1, 'Hello', 4.2]
    my_dict = {'firstname':'','lastname':'Rios'}

    super_list=[
        {'firstname':'','lastname':'Rios'},
        {'firstname':'Emanuel','lastname':'Rios'},
        {'firstname':'Israel','lastname':'Rios'},
        {'firstname':'Fernanda','lastname':'Rios'},
        {'firstname':'Facundo','lastname':'Rios'},
        {'firstname':'Eloisa','lastname':'Rios'},
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5,6],
        'integar_nums': [1,2,-21,15]
    }

    for items in super_list:
        print(items)
       
if __name__ == '__main__':
    run()