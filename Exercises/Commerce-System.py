import os
class Item:
    def __init__(self):
        self.id=["product_id"]
        self.name=["product"]
        self.price=["100$"]
        self.des=["nothing"]
        self.quan=[0]
    def additem(self,id,name,price,des,quan):
        self.id.append(id)
        self.name.append(name)
        self.price.append(price)
        self.des.append(des)
        self.quan.append(quan)
    def info(self,id):
        s=0
        for i in range(len(self.id)) :
            if(id in self.id[i]):
                s=s+1
                print('Product Id:'+str(id))
                print('Product Name:'+str(self.name[i]))
                print('Product Price:'+str(self.price[i]))
                print('Product Description:'+str(self.des[i]))
                print('Product quantity:'+str(self.quan[i]))
        if(s==0):
            print('Cannot Find the Product!')
general=Item()
general.additem('000001','Chips Doritos Tomato','3$','Chips','100000')
general.additem('000002','Chips Doritos Barbarika','5$','Chips','10')
general.additem('000003','Chips Doritos Salt','2$','Chips','1000')
general.additem('000004','Chips Doritos Onion','1$','Chips','1000')
general.additem('000005','Chips Mareb Peanut','5$','Chips','10')
general.additem('000006','Chips Mareb Torbida','1$','Chips','1000000000')
os.system('cls')
a=input('enter the id of product to search:')
general.info(a)
