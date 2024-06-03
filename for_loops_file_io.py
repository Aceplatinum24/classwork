# Text Document
f = open("users.txt", "r")  
lines = f.read().splitlines()  
f.close()  
print(f"Data: {len(lines)} lines loaded.")


# User Input
filename = input("Filename for output file: ")
print(f"Writing report to {filename}." ) #using the name of the output file.


# Writing report to the "filename"
with open(filename, "w") as output_file:


    # Data Table
    age_count = 0
    for line in lines:  
        name_str, age_str = line.split(",")
        age = int(age_str)
        
        if age >= 23:
            age_count += 1
            output_file.write(f"{name_str} is {age_str} years old, and is old enough to ride a dinosaur 🦖. \n")

        if age < 23:
            output_file.write(f"{name_str} is {age_str} years old, and is NOT old enough to ride a dinosaur 🦖.\n")
            

    output_file.write(f"{age_count} people are old enough to ride a dinosaur.")

# Complete
print("🏆 🏁 Report Completed 🏁 🏆")

      
