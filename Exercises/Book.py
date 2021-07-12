#Library Managment System
class booksys:
    def __init__(self):
        self.numbook=0
        self.id=[] 
        self.name=[]
        self.author=[]
        self.isbn=[]
        self.pages=[]
    def load_content(self):
        s=0
        data=open('Books.book','r')
        for x in data:
            s=s+1
            self.id.append(x.split()[0])
            self.name.append(x.split()[1])
            self.author.append(x.split()[2])
            self.pages.append(x.split()[3])
            self.isbn.append(x.split()[4])
        self.numbook=s
    def __getbook__(self,id):
        s=0
        for i in range(len(self.id)):
            if(id == self.id[i]):
                s=s+1
                print('Book Id:'+self.id[i])
                print('Book Name:'+(self.name[i]).replace('_','  '))
                print('Book Author:'+self.author[i])
                print('Book ISBN:'+self.isbn[i])
                print('Book pages:'+self.pages[i])
        if(s==0):
            print('Cannot Find Book')
    def __addbook__(self,id,name,author,isbn,pages):
        s=" "
        file=open('C:/users/sa/desktop/practice/Books.book','a')
        name.replace('  ','_')
        file.write('\n'+id+s+name+s+author+s+pages+s+isbn)
        print('You Should Restart The System to full item accsess')

syst=booksys()
syst.load_content()#load data from file
print('Number of Book in database is:'+str(syst.numbook))
syst.__addbook__('11','AI_IN_Python','Hasan_Saleh','1999024','3000')
