### Case Study 28: Transaction Detection

### 1\. Problem Statement

Write a Python program to identify duplicate transaction IDs and display transactions whose amounts are greater than ₹1000. Use two lists: one to store transaction IDs and another to store their corresponding amounts.

### 2\. Algorithm

* Start.

* Create a list of transaction IDs and a list of transaction amounts.

* Display the heading “Duplicate Transactions”.

* Traverse the transaction list using a loop.

* Check whether each transaction ID has already appeared in the previous elements.

* If it has appeared, print the duplicate transaction ID.

* Display the heading “Transactions above 1000”.

* Traverse the amounts list using a loop.

* If an amount is greater than 1000, print its transaction ID and amount.

* Stop.

### 3\. Flowchart (Mermaid Code)

```mermaid

flowchart TD
    A([Start]) --> B[Create transactions and amounts lists]
    B --> C[Print Duplicate Transactions]
    C --> D[Set i = 0]
    D --> E{i < length of transactions?}
    E -- Yes --> F{transactions[i] in transactions[:i]?}
    F -- Yes --> G[Print duplicate transaction ID]
    F -- No --> H[i = i + 1]
    G --> H
    H --> E
    E -- No --> I[Print Transactions above 1000]
    I --> J[Set i = 0]
    J --> K{i < length of amounts?}
    K -- Yes --> L{amounts[i] > 1000?}
    L -- Yes --> M[Print transaction ID and amount]
    L -- No --> N[i = i + 1]
    M --> N
    N --> K
    K -- No --> O([Stop])
```

### 4\. Python Source Code

```python

# Case Study 28: Transaction Detection

transactions = [101, 102, 103, 102, 104, 101]

amounts = [500, 1200, 800, 1500, 300, 2000]

print("Duplicate Transactions:")

for i in range(len(transactions)):
    if transactions[i] in transactions[:i]:
        print(transactions[i])

print("Transactions above 1000:")

for i in range(len(amounts)):
    if amounts[i] > 1000:
        print(transactions[i], "-", amounts[i])
```

### 5\. Sample Input

The program uses predefined lists, so no user input is required.

```text
transactions = [101, 102, 103, 102, 104, 101]
amounts = [500, 1200, 800, 1500, 300, 2000]
```

### 6\. Sample Output

```text
Duplicate Transactions:
102
101
Transactions above 1000:
102 - 1200
102 - 1500
101 - 2000
```

### 7\. Explanation

* `transactions` stores the transaction IDs.

* `amounts` stores the corresponding transaction amounts.

* `range(len(transactions))` accesses each transaction by its index.

* `transactions[:i]` checks all transaction IDs before the current position.

* `if transactions[i] in transactions[:i]` identifies duplicate IDs.

* `if amounts[i] > 1000` selects amounts greater than ₹1000.

* Both lists use matching indexes, so the program displays the correct transaction ID with its amount.
*
