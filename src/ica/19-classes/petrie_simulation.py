"""
Contains a simulation of the Petrie Multiplier that is based on classes.
"""

import random
import math


class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender: str, will_comment: bool):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee to zero.
        """
        self.gender = gender
        self.will_comment = will_comment
        self.comments_received = 0

    def set_commenter_status(self, status: bool):
        """Sets whether this employee will make sexist comments."""
        self.will_comment = status

    def receive_sexist_comment(self):
        """Increments the count of sexist comments received by one."""
        self.comments_received += 1

    def get_gender(self):
        """Returns the gender of the employee."""
        return self.gender

    def get_commenter_status(self):
        """Returns whether the employee will make sexist comments."""
        return self.will_comment

    def get_comments_received(self):
        """Returns the number of comments received by the employee."""
        return self.comments_received

    def __str__(self):
        """
        Produces a printable string format for this employee.
        """
        return (self.gender.rjust(5)
                + ": "
                + str(self.comments_received)
                + " sexist comments received"
                + (" (commenter)" if self.will_comment else ""))


def print_employee_list(lst):
    """
    Given a list of employees, this method will print the details of each employee
    by using the print() method
    """
    for employee in lst:
        print(employee)


def create_employees(total_num):
    """
    Takes in the number of employees to make, builds and returns a list that contains
    that many employees. It ensures that ~80% are men and the rest women.
    """
    num_men = math.floor(total_num * 0.8)
    num_women = total_num - num_men

    employees = []

    # Create male employees
    for _ in range(num_men):
        employees.append(Employee("Man", False))

    # Create female employees
    for _ in range(num_women):
        employees.append(Employee("Woman", False))

    return employees


def create_commenters(lst):
    """
    Given a list of employees, make 20% of each gender be sexist employees. This
    method should not return anything.
    """
    # Separate employees by gender
    men = [emp for emp in lst if emp.get_gender() == "Man"]
    women = [emp for emp in lst if emp.get_gender() == "Woman"]

    # Make 20% of each gender commenters
    for group in [men, women]:
        for emp in group:
            if random.random() < 0.2:
                emp.set_commenter_status(True)


def generate_comments(lst):
    """
    Given a list of employees, have each sexist employee give one sexist comment to
    another employee of the opposite gender, chosen randomly. This method should
    not return anything
    """
    men = [emp for emp in lst if emp.get_gender() == "Man"]
    women = [emp for emp in lst if emp.get_gender() == "Woman"]

    # Men who comment → random woman
    for man in men:
        if man.get_commenter_status():
            chosen = random.choice(women)
            chosen.receive_sexist_comment()

    # Women who comment → random man
    for woman in women:
        if woman.get_commenter_status():
            chosen = random.choice(men)
            chosen.receive_sexist_comment()


def average_comments(lst):
    """
    Returns a tuple that represents the average amount of comments received for men and women
    respectively. Return statement will be in the form (<avg_for_men>, <avg_for_women>)
    """
    men_comments = [emp.get_comments_received() for emp in lst if emp.get_gender() == "Man"]
    women_comments = [emp.get_comments_received() for emp in lst if emp.get_gender() == "Woman"]

    men_avg = sum(men_comments) / len(men_comments) if men_comments else 0
    women_avg = sum(women_comments) / len(women_comments) if women_comments else 0

    return (men_avg, women_avg)


def main():
    """
    Print out information about the average comments
    received by men and women after a simulation has been run
    """
    num_employees_to_generate = 100
    num_comment_rounds = 50

    employee_list = create_employees(num_employees_to_generate)
    create_commenters(employee_list)

    for _ in range(num_comment_rounds):
        generate_comments(employee_list)

    (men_avg, women_avg) = average_comments(employee_list)
    print("  Men received on average ", round(men_avg, 2), "sexist comments")
    print("Women received on average ", round(women_avg, 2), "sexist comments")


if __name__ == "__main__":
    print("<----- Test code for print_employee_list ----->")
    lst = [Employee('Man', True),
           Employee('Man', False),
           Employee('Woman', True),
           Employee('Woman', False)]
    print_employee_list(lst)

    print("\n<----- Test code for create_employees ----->")
    employees = create_employees(10)
    print_employee_list(employees)

    print("\n<----- Test code for create_commenters ----->")
    create_commenters(employees)
    print_employee_list(employees)

    print("\n<----- Test code for generate_comments ----->")
    generate_comments(employees)
    print_employee_list(employees)

    print("\n<----- Test code for average_comments ----->")
    print(average_comments(employees))

    print("\n<----- Run the simulation ----->")
    main()
