class Book:
    book_count=0

    def __init__(self, name,author,category,international):
        self.name = name
        self.author = author
        self.category = category
        self.status = None # thats explain how book is rented or not
        self.international=international
        self.bookID = None
        self.rent = None
        Book.book_count+=1

    def setCategori(self,category):
        if self.category==None:
            self.category=category
            print("The category is assigned to {}".format(category))
        else:
            print("The Category had been assigned earlier and it is {}".format(self.category))

    def rentbook(self,member):  # its task is in charge of validating membrance and having book or not
        if self.status==None:
            self.status= member
            print("this book is available and  now rented to {}".format(member))
        else:
            print("This book was already rented to {}".format(self.status))


    #------------------------------------------------------------------------------------------------------
class BookIrani(Book):
    persianBook_count=0    #(can)t use!!
    def __init__(self,name, author, category, international=False):
        Book.__init__(self,name,author,category,international)
        self.pub_year=None
        self.edition=None
        self.serial=None
        self.translator_name=None
        self.publisher=None
        self.price=None
        self.serial=None
        BookIrani.persianBook_count+=1

    def set_Pub_year(self,pub_yaer):
        if self.pub_year==None:
            self.pub_year=pub_yaer
        return  pub_yaer
    def set_Publisher(self,publisher):
        if self.publisher==None:
            self.publisher=publisher
        return publisher
    def set_Price(self,price):
        if self.price==None:
            self.price=price
        return price
    def set_Serial(self,serial):
        if self.serial==None:
            self.serial=serial
    # def display_Pcount(self):
    #     print("we have {} books in our library".format(Book.persianBook_count))

class BookInternational(Book):
    def __init__(self,name,author,category,international=True):
        Book.__init__(self, name, author, category, international)
        self.translator_name=None
        self.edition=None
    def setTranslator(self,translator_name):
        if  self.international==True:
            self.translator_name = translator_name
            print('the translator has been assigned to {}'.format(translator_name))
        else:
            print("This book is not international and there is no need to translator.")


b1=BookIrani('Divane Hafez','Hafez Shirazi',None,0)
b1.setCategori('Poetry')
b1.setCategori('Science')