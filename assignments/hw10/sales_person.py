"""
Name: <Queen Hamilton, II>
<sales_person>.py

Problem: This program creates a SalesPerson class

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


class SalesPerson:
    """
    The class creates a Sales Person object for employee information
    """
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """
        Returns the object's employee id
        """
        return self.employee_id

    def get_name(self):
        """
        Returns the object's name
        """
        return self.name

    def set_name(self, name):
        """
        Sets the object's name
        """
        self.name = name

    def enter_sale(self, sale):
        """
        Adds a single float to the sales list
        """
        self.sales.append(float(sale))

    def total_sales(self):
        """
        Returns the sum of all the object's sales
        """
        return sum(self.sales)

    def get_sales(self):
        """
        Returns the object's sales as a list of floats
        """
        return self.sales

    def met_quota(self, quota):
        """
        Returns a boolean regarding whether the object met the entered quota
        """
        return self.total_sales() >= quota

    def compare_to(self, other):
        """
        Returns -1, 1, or 0 if the object is less, more, or equal to the entered one, respectfully.
        """
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
