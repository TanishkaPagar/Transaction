import streamlit as st
import random

# Title
st.title("Simple Blockchain Simulation")

# Numeric data types
block_number = 123456  # integer
transaction_fee = 0.0005  # float

# Text data type
wallet_address = "0xABC123XYZ"  # string

# List: store multiple transactions
transactions = [10, 50, 200, 5]

# Dictionary: represents a transaction
transaction1 = {
    "sender": "Harry",
    "receiver": "Louis",
    "amount": 500000
}

# Display static blockchain data
st.header("Blockchain Data")
st.write("Block Number:", block_number)
st.write("Transaction Fee:", transaction_fee)
st.write("Wallet Address:", wallet_address)
st.write("Transactions:", transactions)
st.write("Transaction Details:", transaction1)

# Display each transaction amount
st.subheader("Transactions List")
transactions = [10, 20, 50, 100]
for amount in transactions:
    st.write("Transaction Amount:", amount)

# Simulate mining blocks
st.subheader("Mining Simulation")
if st.button("Start Mining"):
    for block in range(1, 6):
        st.write(f"Mining Block: {block}")

# Blockchain tasks with counter
st.subheader("Blockchain Tasks")
if st.button("Run Blockchain Task Loop"):
    count = 0
    while count < 3:
        st.write("Blockchain task")
        count += 1

# Payment processing simulation
st.subheader("Payment Processing")
if st.button("Process Payments"):
    balance = 100
    while balance > 0:
        st.write(f"Processing payment... Remaining balance: {balance}")
        balance -= 20

# Random transaction guessing game
st.subheader("Guess the Transaction Amount Game")
transactions = [100, 200, 300, 400, 500]
chosen_transaction = random.choice(transactions)

user_guess = st.number_input("Guess the transaction amount:", min_value=0, step=1)

if st.button("Submit Guess"):
    if user_guess == chosen_transaction:
        st.success("Congratulations! You guessed the right amount.")
    else:
        st.error(f"Wrong! The correct transaction was {chosen_transaction}.")
