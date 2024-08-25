d={}

if __name__=="functions":
    print("Product Details")


def get_product_details():
    while True:
        pname=input("Product Name :")
        Purchase_cost=input("Purchase Cost :")
        d[pname]=Purchase_cost
        choice =input("do you want to enter one more product y/n?")
        if choice =='n':
            break

def print_product_details():
    print(d)

get_product_details()
print_product_details()



