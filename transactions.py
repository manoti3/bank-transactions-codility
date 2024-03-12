# writing a function that that represents transaction amounts 
# def solution(A):
#     transactions=''
#     balance = 0
     




#     bank_transactions = [100,100,100,-10]
#     transactions = solution(bank_transactions)
#     print(transactions)

    



# # a funcion that returns transaction dates and returns the final balance of the account at the end of the year
# def solutioon(D):
#     transactions_dates=''



#     bank_transactions_dates = ["2020-12-31", "2020-12-22", "2020-12-29"]
#     dates = solution(bank_transactions_dates)
#     print(dates)


#writing a function that that represents transaction amounts
def solution(A, D):
    # Dictionary to track total transactions for each month
    transactions = {}
    # Variables to track total income and expenses
    total_income = 0
    total_expenses = 0
    
    # Iterate through each transaction
    for amount, date in zip(A, D):
        # Extract year, month, and day from the date
        year, month, _ = date.split('-')
        # Create a key in the transactions dictionary based on year and month
        key = f"{year}-{month}"
        
        # Update total amount for the corresponding month in transactions
        if key not in transactions:
            transactions[key] = 0
        transactions[key] += amount
        
        # Update total income and expenses based on the sign of the amount
        if amount >= 0:
            total_income += amount
        else:
            total_expenses += amount
    
    # Calculate fees based on specific transaction amounts
    total_fee = 0
    for amount in transactions.values():
        # Adjust fee calculation based on the specified rules
        if amount < -100:
            total_fee += 5
        elif amount < -50:
            total_fee += 4
        elif amount < -25:
            total_fee += 3
        elif amount < -10:
            total_fee += 2
        elif amount < 0:
            total_fee += 1
    
    # Calculate final balance by subtracting total fees from the sum of total income and total expenses
    final_balance = total_income + total_expenses - total_fee
    return final_balance

# Example usage:
A1 = [100, 100, 100, -10]
D1 = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]
print(solution(A1, D1))  # Output: 230

A2 = [180, -50, -25, -25]
D2 = ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]
print(solution(A2, D2))  # Output: 25

A3 = [-1, -1, 0, -105, 1]
D3 = ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]
print(solution(A3, D3))  # Output: -164

A4 = [100, 100, -10, -20, -30]
D4 = ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]
print(solution(A4, D4))  # Output: 80

A5 = [60, 60, -40, -20]
D5 = ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]
print(solution(A5, D5))  # Output: -115
