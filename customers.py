"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""    

    def __init__(self,first_name,last_name,email,password):      
        self.first_name=first_name                
        self.last_name=last_name
        self.email=email                
        self.password=password      


def read_customers_from_file(filepath):
    """Dictionary will be {email: customer}
    """

    customers = {}

    with open("customers.txt") as file:
        for line in file:
            (first_name,
             last_name,
             email,
             password) = line.strip().split("|")

            customers[email] = Customer(first_name,
                                                 last_name,
                                                 email,
                                                 password)

    return customers
    

def get_by_email(email):
    """Return a customer, given their email."""

    return customers[email]

customers = read_customers_from_file("customers.txt")