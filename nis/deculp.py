def generate_avg_trn_value(transactions):
    """
    Calculate the average transaction value from a list of transactions.

    Args:
        transactions (list): A list of transaction values (floats or integers).

    Returns:
        float: The average transaction value.
    """
    # Check if the transactions list is empty
    if not transactions:
        return 0.0

    # Calculate the sum of all transactions
    total_value = sum(transactions)

    # Calculate the number of transactions
    num_transactions = len(transactions)

    # Calculate the average transaction value
    avg_value = total_value / num_transactions

    return avg_value

# Example usage:
transactions = [100.0, 200.0, 150.0, 300.0]
average_transaction_value = generate_avg_trn_value(transactions)
print(f"The average transaction value is: {average_transaction_value}")
