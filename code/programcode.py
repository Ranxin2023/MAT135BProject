import matplotlib.pyplot as plt
import random

def simulate_tosses():
    tosses = []  
    toss_count = 1  

    while True:
        # Generate the initial toss.
        initial_toss = random.choice(['T', 'H'])
        
        # Ask for user input on a new line for clarity.
        print(f"Toss {toss_count} - Initial toss is {initial_toss}.")
        result = input("Enter toss result (T or H, anything else to exit): ")
        
        if result in ['T', 'H']:
            # Save the toss number, initial toss, and result.
            tosses.append((toss_count, initial_toss, result))
            toss_count += 1
        else:
            print("Exiting.")
            break

    return tosses

def calculate_probabilities(tosses):
    # Initialize counters
    total_T_starts = 0
    T_results_from_T_starts = 0
    total_H_starts = 0
    H_results_from_H_starts = 0
    
    # Analyze the tosses to count occurrences
    for _, initial, result in tosses:
        if initial == 'T':
            total_T_starts += 1
            if result == 'T':
                T_results_from_T_starts += 1
        elif initial == 'H':
            total_H_starts += 1
            if result == 'H':
                H_results_from_H_starts += 1
    
    # Calculate probabilities
    probability_T_to_T = T_results_from_T_starts / total_T_starts if total_T_starts else 0
    probability_H_to_H = H_results_from_H_starts / total_H_starts if total_H_starts else 0
    
    return probability_T_to_T, probability_H_to_H

# Execute the toss simulation
toss_results = simulate_tosses()

# Calculate and display the probabilities
probability_T_to_T, probability_H_to_H = calculate_probabilities(toss_results)
print(f"Probability of 'T' start leading to 'T' result: {probability_T_to_T:.2f}")
print(f"Probability of 'H' start leading to 'H' result: {probability_H_to_H:.2f}")
