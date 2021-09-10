"""
Name: <Queen Hamilton, II>
<interest>.py

Problem: This program computes the monthly interest charge on a credit card account

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    # 1. input annual interest rate
    annual_interest = eval(input("Enter your annual interest rate: "))
    # 2. input number of days in the billing cycle
    billing_cycle = eval(input("Enter the number of days in your billing cycle: "))
    # 3. input previous net balance
    net_balance = eval(input("Enter your balance before your payment: "))
    # 4. input payment amount
    payment = eval(input("Enter your payment amount: "))
    # 5. input day of the billing cycle that the payment was made
    payment_date = eval(input("What day of your billing cycle did you make this payment? "))
    # 6. Days before the end of the cycle (2. - 5.)
    days_before_end_cycle = billing_cycle - payment_date
    # 7. multiply net balance by days in the billing cycle (3. * 2.)
    balance_by_cycle = net_balance * billing_cycle
    # 8. multiply payment by days before end cycle (4. * 6.)
    payment_by_days = payment * days_before_end_cycle
    # 9. subtract (7.-8.)
    balance_minus_payment = balance_by_cycle - payment_by_days
    # 10. average daily balance = (9./2.)
    average_daily_balance = balance_minus_payment / billing_cycle
    # 11. monthly interest rate = (1. /"the number 12")
    monthly_interest_rate = annual_interest / 12
    # 12. monthly interest charge = 10. * 11.
    monthly_interest_charge = average_daily_balance * (monthly_interest_rate / 100)
    print(round(monthly_interest_charge, 2))


if __name__ == "__main__":
    main()
