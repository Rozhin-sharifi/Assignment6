def read_from_database():
    try:
        products=[]
        f=open("Assignment6\data_base.csv","r")
        big_text=f.read()
        product_list=big_text.split('\n')
        print(product_list)

        for i in range(len(product_list)):
            info= product_list[i].split(',')
            products.append({'id':info[0], 'name':info[1], 'price':info[2], 'count':info[3]})
    
    except Exception as e:
        print(e)
        products=[]

    return(products)

def add():

    id= input('enter id: ')
    for product in products:
        if product['id']==id:
            print('duplicate products!')
            break
    else:
        name= input('enter name: ')
        price= input('enter price: ')
        count= input('enter count: ')
        products.append({'id':id, 'name':name, 'price':price, 'count':count})
        

def search(a):

    user_input= a
    for product in products:
        if product['id']==user_input or product['name']==user_input:
            return (product)
            break
    else:
        print('not found!')


def edit(a,b,c):

    user_input1=a
    user_input2=b 
    user_input3=c 
    for product in products:
        if product['id']==user_input1 or product['name']==user_input1:
            if user_input2=='id':
                product['id']= user_input3
            elif user_input2=='name':
                product['name']= user_input3
            elif user_input2=='price':
                product['price']= user_input3
            elif user_input2=='count':
                product['count']= user_input3   
            break
    else:
        return ('not found!')

def remove():

    user_input= input('please enter name or id to remove.. ')
    for product in products:
        if product['id']==user_input or product['name']==user_input:
            products.remove(product)
            break
    else:
        print('not found!')

def buy(a,n):
    i=0
    shopping_list=[]
    number_of_items=[]
    s=search(a)
    if s=='not found':
         print ("not found")
    else:
        shopping_list.append(s)
        number_of_items.append(int(n))
        if int(shopping_list[i]['count'])>number_of_items[i]:
            d=int(shopping_list[i]['count'])-number_of_items[i]
            b='count'
            edit(a,b,d)
            return(shopping_list[i]['name'],shopping_list[i]['price'],number_of_items[i])
            i+=1
def show_all():

    for product in products:
        print(product)

def my_exit():

    f=open("Assignment6\data_base.csv","w")
    for i in range(len(products)):
        if i<len(products)-1:
          f.write(str(products[i]['id']+','+products[i]['name']+','+products[i]['price']+','+products[i]['count']+'\n'))
        else:
          f.write(str(products[i]['id']+','+products[i]['name']+','+products[i]['price']+','+products[i]['count']))
    exit()
def show_menu():

    print('welcome to rozhin store')
    print('1-add new product')
    print('2-search')
    print('3-edit')
    print('4-remove')
    print('5-buy')
    print('6-show all')
    print('7-exit')


products=read_from_database()

show_menu()

while True:
    choice=input('enter your choice: ')
    if choice=='1':
        add()
    elif choice=='2':
        a=input('please enter name or id to search.. ')
        s=search(a)
        print(s)
    elif choice=='3':
        a=input('please enter name or id to edit.. ')
        b=input('please enter the product feature to edit.. ')
        c=input('please enter the edition.. ')
        edit(a,b,c)
    elif choice=='4':
        remove()
    elif choice=='5':
        shopping_list=[]
        while True:
            a=input('please enter name or id to buy.. ')
            n=input('please enter the count.. ') 
            add=buy(a,n)
            shopping_list.append(add)
            continue_shopping=input('continue shopping?(y/n)..')
            if continue_shopping=='y':
                continue
            else:
                print(shopping_list)
                break
    elif choice=='6':
        show_all()
    elif choice=='7':
        my_exit()
