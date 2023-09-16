

def fibonacci(term_number):
    previous_term, current_term = 0, 1
    for _ in range(term_number):
        previous_term, current_term = current_term, previous_term + current_term
    return previous_term


