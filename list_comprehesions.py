def run ():
    # my_list = []
    # for i in range(1,101):
    #     if i % 3 !=0:
    #         my_list.append(i**2)
    # print(str(my_list)+'\n')
    # squares = [i**2 for i in range(1,101) if i%3 !=0]    
    # print(squares)
    lista = [i for i in range(1,10000) if i %4 ==0 and i%6 ==0 and i%9==0]
    print(lista)
if __name__ == '__main__':
    run()