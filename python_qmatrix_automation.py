import random

# Generate 100 random 5-bit numbers (0 to 31)
random_numbers = [random.randint(0, 31) for _ in range(100)]

# Assign the generated random numbers to the Q matrix bitwise
Q_matrix = {}
for i, number in enumerate(random_numbers):
    binary_representation = f"{number:05b}"  # Convert to 5-bit binary
    for bit_index, bit in enumerate(binary_representation):
        Q_matrix[f"Q{bit_index}{i}"] = int(bit)

# Generate the Spectre code for each parameter
spectre_code = []
for param, value in Q_matrix.items():
    if value == 0:
        spectre_code.append(f"v{param} ({param} 0) vsource dc=0")
    else:
        spectre_code.append(f"v{param} ({param} 0) vsource dc=1")

# Print the resulting Spice code
spectre_code_str= "\n".join(spectre_code)

with open("qmatrix.scs", "w") as file:
    file.write(spectre_code_str)

print("Spectre code has been saved to qmatrix.scs")