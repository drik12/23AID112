# Stacks and Queues Questions

---

## Question 1: Browser History Management (Stack)

A web browser stores visited pages so users can navigate backward through previously opened pages.

### Operations Required

- Visit a new page  
- Go back to the previous page  
- Display the current page  

### Tasks

1. Identify the most suitable data structure (**Stack or Queue**) for managing browser history and justify your answer.

2. Explain how **push** and **pop** operations represent visiting a new page and going back to the previous page.

3. Write pseudocode for the **Back operation using a stack**.

4. Analyze the **time complexity of push and pop operations** used in browser history management.

5. **Implementation Task:**  
   Write a Python program to implement **browser history using a stack (linked list implementation)** with the following operations:

   - `visit(page)` – push a webpage onto the stack  
   - `back()` – pop the current webpage  
   - `current_page()` – display the page at the top of the stack  
   - `display()` – display all visited pages  

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

5. **Implementation Task:**  
   Write a Python program using a **stack** that checks whether parentheses in an expression are **balanced**.

   The program should support:

   - `push()` for opening brackets  
   - `pop()` when a closing bracket appears  
   - Display whether the expression is **Balanced** or **Not Balanced**

---

## Question 3: Printer Job Scheduling (Queue)

An office printer receives print requests from multiple users.

### System Characteristics

- Print jobs arrive continuously  
- Jobs must be processed in **First-Come First-Served (FCFS)** order  

### Tasks

1. Identify the most suitable data structure for this system and justify your answer.

2. Explain how **enqueue** and **dequeue** operations work in this scenario.

3. Write pseudocode for **adding a new print job to the queue**.

4. Compare the **time complexity of enqueue and dequeue operations**.

5. **Implementation Task:**  
   Write a Python program to implement a **printer job queue using linked list implementation** with the following operations:

   - `enqueue(job)` – add a print job to the queue  
   - `dequeue()` – process the next print job  
   - `peek()` – display the job at the front of the queue  
   - `display()` – display all pending jobs  

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

5. **Implementation Task:**  
   Write a Python program to implement a **customer service ticket system using a queue (linked list)** with the following operations:

   - `enqueue(ticket)` – add a new ticket  
   - `dequeue()` – serve the next ticket  
   - `peek()` – display the next ticket to be served  
   - `display()` – show all pending tickets  

---