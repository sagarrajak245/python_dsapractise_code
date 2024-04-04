def job_sequencing_with_deadlines(jobs):
    # Sort jobs based on their profits in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Find the maximum deadline
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    
    # Initialize schedule with zeros
    schedule = [0] * (max_deadline + 1)
    total_profit = 0
    
    # Iterate through each job
    for job in jobs:
        profit = job[2]
        deadline = job[1]
          
        # Find a slot in the schedule
        while deadline > 0 and schedule[deadline] != 0: 
            deadline -= 1
        
        # If a slot is found, assign the job to that slot
        if deadline > 0:
            schedule[deadline] = job[0]
            total_profit += profit
    
    return total_profit

# Example usage:
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
max_profit = job_sequencing_with_deadlines(jobs)
print("Maximum profit:", max_profit)
