"""
Name: <Queen Hamilton, II>
<sales_force>.py

Problem: This program creates a SalesForce class

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


from sales_person import SalesPerson


class SalesForce:
    """
    Creates a SalesForce object; manages SalesPerson objects
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        """
        Reads data from a file and creates a list of SalesPerson objects
        """
        with open(file_name, "r") as file:
            for line in file:
                employee_id, name, sales = line.split(", ")
                sales_person = SalesPerson(employee_id, name)
                sales_list = sales.split(" ")
                for num in sales_list:
                    sales_person.enter_sale(num)
                self.sales_people.append(sales_person)
            file.close()

    def quota_report(self, quota):
        """
        Returns a list displaying whether each SalesPerson object has met the entered quota
        """
        report_list = []
        for person in self.sales_people:
            person_list = [person.get_id(), person.get_name(), person.total_sales(),
                           person.met_quota(quota)]
            report_list.append(person_list)
        return report_list

    def top_seller(self):
        """
        Returns a list of SalesPerson objects that have the greatest total sales overall
        """
        top = [self.sales_people[0]]
        for i in self.sales_people:
            if top[0].compare_to(i) == -1:
                top = [i]
            elif not top[0].compare_to(i):
                top.append(i)
        return top

    def individual_sales(self, employee_id):
        """
        Returns the SalesPerson object that has the entered employee id or None type if the
        object doesn't exist
        """
        id_dict = {}
        for person in self.sales_people:
            id_dict[int(person.get_id())] = person
        if employee_id in id_dict:
            return id_dict.get(employee_id)
