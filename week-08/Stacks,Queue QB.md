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

```
BACK(stack)

if stack is empty
    print "No previous page"
    return

pop the current page
print "Moved to previous page"
```

4. Compare the **time complexity of push and pop operations**.

| Operation | Time Complexity |
|-----------|----------------|
| Push | O(1) |
| Pop | O(1) |

5. If the browser stores **n visited pages**, determine the **space complexity of the stack**.

Space complexity = **O(n)**

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

A stack follows the **Last In First Out (LIFO)** principle which is useful for evaluating expressions where the most recent operator or parenthesis must be processed first.

2. Describe how a **stack helps in checking balanced parentheses**.

When an opening parenthesis `(` is encountered, it is pushed onto the stack.  
When a closing parenthesis `)` appears, the stack is popped.  
If the stack becomes empty correctly at the end, the parentheses are balanced.

3. Write pseudocode for **checking balanced parentheses using a stack**.

```
CHECK_BALANCED(expression)

create empty stack

for each character in expression
    if character is '('
        push to stack

    if character is ')'
        if stack is empty
            return "Not Balanced"
        pop from stack

if stack is empty
    return "Balanced"
else
    return "Not Balanced"
```

4. Determine the **time complexity** of the algorithm for an expression of length **n**.

Time Complexity = **O(n)**

Each character is processed once.

5. Compare the **memory usage of stack-based evaluation with recursive evaluation**.

| Method | Memory Usage |
|------|------|
| Stack Based | Uses explicit stack structure |
| Recursive | Uses system call stack |
| Efficiency | Stack method gives better control over memory |

---

## Question 3: Printer Job Scheduling (Queue)

An office printer receives print requests from multiple users.

### System Characteristics

- Print jobs arrive continuously
- Jobs must be processed in **First-Come First-Served (FCFS)** order

### Tasks

1. Identify the most suitable data structure for this system and justify your answer.

The most suitable data structure is a **Queue** because it follows the **First In First Out (FIFO)** principle.

2. Explain how **enqueue and dequeue operations** work in this scenario.

- **Enqueue** → Adds a new print job to the end of the queue  
- **Dequeue** → Removes the print job at the front of the queue for printing

3. Write pseudocode for **adding a new print job to the queue**.

```
ADD_PRINT_JOB(queue, job)

if queue is full
    print "Printer Queue Full"
    return

insert job at rear of queue
```

4. Compare the **time complexity of enqueue and dequeue operations**.

| Operation | Time Complexity |
|-----------|----------------|
| Enqueue | O(1) |
| Dequeue | O(1) |

5. Determine the **space complexity** if **n print jobs** are stored in the queue.

Space Complexity = **O(n)**

---

## Question 4: Customer Service Ticket System (Queue)

A customer support center handles service tickets submitted by users.

### System Behavior

- Tickets arrive continuously
- The earliest ticket must be handled first

### Tasks

1. Identify the appropriate data structure for this system and explain why.

The appropriate data structure is a **Queue**, since the system processes tickets in the order they arrive.

2. Describe how **adding a ticket** and **serving a ticket** correspond to queue operations.

- Adding a ticket → **Enqueue**
- Serving a ticket → **Dequeue**

3. Write pseudocode for **serving the next ticket**.

```
SERVE_TICKET(queue)

if queue is empty
    print "No tickets available"
    return

ticket = remove from front of queue
print "Serving ticket:", ticket
```

4. Compare **array-based queue vs linked list queue** in terms of memory allocation.

| Feature | Array Queue | Linked List Queue |
|-------|------|------|
| Memory Allocation | Fixed size | Dynamic |
| Overflow | Possible | Rare |
| Memory Usage | Efficient | Slightly higher |

5. Analyze the **time complexity** of adding and removing tickets.

| Operation | Time Complexity |
|----------|----------------|
| Enqueue | O(1) |
| Dequeue | O(1) |

---