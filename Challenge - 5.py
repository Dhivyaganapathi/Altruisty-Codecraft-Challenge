def find_strongest_trainee():
    strength_values = []
    
    for round_num in range(3):
        for trainee_num in range(4):
            try:
                strength = int(input(f"Enter strength of Trainee {trainee_num + 1} for Round {round_num + 1}: "))
                
                if strength < 1 or strength > 200:
                    print("INVALID INPUT")
                    return 
                strength_values.append(strength)
            except ValueError:
                print("INVALID INPUT")
                return  

    averages = []
    for i in range(0, len(strength_values), 4):
        avg_strength = sum(strength_values[i:i + 4]) / 3
        averages.append(round(avg_strength))  

    max_avg = max(averages)

    if max_avg < 100:
        print("All trainees are unfit.")
    else:
        for i in range(4):
            if averages[i] == max_avg:
                print(f"Trainee Number : {i + 1}")

# Call the function to execute the logic
find_strongest_trainee()
