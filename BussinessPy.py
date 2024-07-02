'''
    © 2024 <nicolaspauer20@gmail.com>

    BussinessPy - Python Bussiness Data Analitics

    Make abstraction to easy up data managment about
    enterprises and bussiness.
'''


class Product():

    '''
        © 2024 <nicolaspauer20@gmail.com>

        BussinessPy.Product class

        Define an product abstraction with the next data:

            * BussinessPy.Product.name, str, name of one enterprise product

            * BussinessPy.Product.price, float, price greater than zero for that product

            * BussinessPy.Product.demand, int, a number greater or equal one with the product importace

            * BussinessPy.Product.enterprises, list, BussinessPy.Customer objects that sell, buy or would do it that product

            * BussinessPy.Product.customers, list, BussinessPy.Customer objects that buy or would buy the product

        Methods:

            * BussinessPy.Product.getPrice(), return float with the product price

            * BussinessPy.Product.discount(customer:BussinessPy.Customer), return float with the discount for customer

            * BussinessPy.Product.newEnterprise(enterprise:BussinessPyEnterprise), add a new Enterprise object to BussinessPy.Product.enterprises list

            * BussinessPy.Product.betterProducts(), give a list with 5 winnings products

            * BussinessPy.Product.betterEnterprises(), give a list with the enterprise that make or sell that products
    '''

    def __init__(self, name:str, price:float):

        self.name:str = name

        self.price:float = price

        self.demand:int = 1

        self.enterprises:list = []

        self.customers:list = []

    def getPrice() -> float:

        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinessPy.Product class

            Return the price as real (float) number, greater demand or market
            bigger price.
        '''
        # Set the market size
        market = (self.enterprises.__len__() + self.customers.__len__())

        if (market < 1):
        # Fix if the list don't added new items to the lists
            market = 1
        # Give a possible result for the price that could be re offered
        return (self.price * self.demand) / market)

    def discount(self, customer:Customer) -> float:

        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinessPy.Product class

            Apply discount to product if the price is so high for the customer
            incomes.

            Return the price with discount as real (float).
        '''
        # Get the over price doing of this way to better reading
        over = (self.getPrice() / customer.incomes)
        # Like this is more easier understand that get the right price and how do it
        return (self.getPrice() / over)

    def newEnterprise(self, enterprise:Enterprise):

        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinessPy.Product class

            Add a new enterprise maker or trader of that product to the list.
        '''
        self.enterprises.append(enterprise)

    def betterProducts(self) -> list:

        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinessPy.Product class

            Return a 5 items list with the better products for the customer.
        '''

        result = []

        for product in self.products:

            if (result.__len__() == 5):

                break

            else:

                if (product.getPrice() <= (result[result.__len__() - 1])):
                # Add the cheaper products
                    result.append(product)

        # Sort from cheaper to more expensive price

        index = 0

        for product in result:

            if (product.getPrice() < result[index + 1]):

                aux = result[index]

                result[index] = product

                result[index + 1] = aux

            index += 1

            if (index == 4):

                break

        return result

    def betterEnterprises(self) -> list:
        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinessPy.Product class

            Return a 5 items list with the better enterprises for the customer.
        '''
        
        result = []

        for product in self.products:

            for enterprise in self.enterprises:

                if ((enterprise.products.__contains__(product)) and (result.__len__() < 5)):

                    result.append(product)

        return result

class Customer():

    '''
        © 2024 <nicolaspauer20@gmail.com>

        BussinessPy.Customer class

        Define an customer abstraction with the next data:

            * BussinessPy.Customer.name, str, name of one customer from the enterprise bussiness

            * BussinessPy.Customer.age, int, The age of the customer from 1 to 100

            * BussinessPy.Customer.incomes, float, how much money wins the customer

            * BussinessPy.Customer.enterprises, list, BussinesPy.Enterprise objects that sell, buy or would do it the product to the customer

            * BussinessPy.Customer.products, list, BussinesPy.Product objects to buy or sell
    '''

    def __init__(self, name:str, age:int):

        self.name:str = name

        self.age:int = age

        self.incomes:float

        self.enterprises:list = []

        self.products:list = []


class Enterprise():

    '''
        © 2024 <nicolaspauer20@gmail.com>

        BussinessPy.Enterprise class

        Define an enterprise abstraction with the next data:

            * BussinessPy.Enterprise.name, str, enterprise name

            * BussinessPy.Enterprise.country, str, enterprise main country

            * BussinessPy.Enterprise.category, str, enterprise main kind of bussiness

            * BussinessPy.Enterprise.wins, float, how much money wins the enterprise

            * BussinessPy.Enterprise.losts, float, how much money losts the enterprise

            * BussinessPy.Enterprise.products, list, enterprise BussinessPy.Product

            * BussinessPy.Enterprise.customers, list, enterprise BussinessPy.Customer objects

            * BussinessPy.Enterprise.related, list, enterprises related with that object BussinessPy.Enterprise

        Methods:

            * BussinessPy.Enterprise.newProduct(p:BussinessPy.Product), add product to BussinessPy.Enterprise.Products list

            * BussinessPy.Enterprise.newEnterprise(), add enterprise to BussinessPy.Enterprise.related list

            * BussinessPy.Enterprise.newCustomer(c:BussinessPy.Customer), add customer to BussinessPy.Enterprise.customers

            * BussinessPy.Enterprise.enterprise(name:str, country:str), create a BussinessPy.Enterprise object and add to BussinessPy.Enterprise.related list

            * BussinessPy.Enterprise.relate(e:BussinessPy.Enterprise), add a BussinessPy.Enterprise object to BussinessPy.Enterprise.related
    '''

    def __init__(self, name:str, country:str):

        
        # Name of the enterprise
        self.name:str = name
        # Country where the enterprise started or stay more related
        self.country:str = country
        # List of products
        self.products:list = []
        # The main kind of bussiness of the enterprise
        self.category:str
        # Enterprise profit

        self.wins:float

        self.losts:float

        # Customers data

        self.customers:list = []

        self.related:list = []

    def newProduct(self, p:Product):

        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinesPy.Enterprise class            

            Add new product to BussinesPy.Enterprise.products list
        '''

        self.products.append(p)

    def newCustomer(self, c:Customer):

        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinesPy.Enterprise class            

            Add new customer to BussinesPy.Enterprise.customers list
        '''

        self.customers.append(c)

    def enterprise(self, name:str, country:str):

        '''
            © 2024 <nicolaspauer20@gmail.com>

            BussinesPy.Enterprise class            

            Add new enterprise relation to BussinesPy.Enterprise.related list
        '''

        obj = Enterprise(name, country)

        self.related.append(obj)

    def relate(self, e:Enterprise):

        '''
             © 2024 <nicolaspauer20@gmail.com>

            BussinesPy.Enterprise class            

            Add new enterprise relation to BussinesPy.Enterprise.related list
        '''

        self.related.append(e)
