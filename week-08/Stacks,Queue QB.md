# Stacks and Queues Questions

---

## Question 1: Browser History Management (Stack)

A web browser stores visited pages so users can navigate backward through previously opened pages.

### Operations Required

- Visit a new page
- Go back to the previous page
- Display the current page

### Tasks

1. Identify the most suitable data structure (**Stack or Queue**) and justify your answer.

2. Explain how the **push** and **pop** operations represent visiting a new page and going back.

3. Write pseudocode for the **Back operation using a stack**.

4. Compare the **time complexity of push and pop operations**.

5. If the browser stores **n visited pages**, determine the **space complexity of the stack**.

---

## Question 2: Arithmetic Expression Evaluation (Stack)

A calculator program evaluates mathematical expressions entered by a user.

### Example Expression

```
(8 + 2) * 5
```

### The program must handle

- Parentheses
- Operator precedence

### Tasks

1. Explain why a **stack is useful for expression evaluation**.

2. Describe how a **stack helps in checking balanced parentheses**.

3. Write pseudocode for **checking balanced parentheses using a stack**.

4. Determine the **time complexity** of the algorithm for an expression of length **n**.

5. Compare the **memory usage of stack-based evaluation with recursive evaluation**.

---

## Question 3: Printer Job Scheduling (Queue)

An office printer receives print requests from multiple users.

### System Characteristics

- Print jobs arrive continuously
- Jobs must be processed in **First-Come First-Served (FCFS)** order

### Tasks

1. Identify the most suitable data structure for this system and justify your answer.

2. Explain how **enqueue and dequeue operations** work in this scenario.

3. Write pseudocode for **adding a new print job to the queue**.

4. Compare the **time complexity of enqueue and dequeue operations**.

5. Determine the **space complexity** if **n print jobs** are stored in the queue.

---

## Question 4: Customer Service Ticket System (Queue)

A customer support center handles service tickets submitted by users.

### System Behavior

- Tickets arrive continuously
- The earliest ticket must be handled first

### Tasks

1. Identify the appropriate data structure for this system and explain why.

2. Describe how **adding a ticket** and **serving a ticket** correspond to queue operations.

3. Write pseudocode for **serving the next ticket**.

4. Compare **array-based queue vs linked list queue** in terms of memory allocation.

5. Analyze the **time complexity** of adding and removing tickets.

---