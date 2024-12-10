import random

# Generate 10 random 100-bit numbers
random_numbers = [random.getrandbits(100) for _ in range(10)]

# Convert each number to a binary string with 100 bits
binary_numbers = [bin(num)[2:].zfill(100) for num in random_numbers]

# Generate Spectre code for each random number
spectre_code = []
for i, binary in enumerate(binary_numbers):
    spectre_code.append(f"// Random number {i+1}")
    for j, bit in enumerate(binary):
        dc_value = '1' if bit == '1' else '0'
        spectre_code.append(f"vkey{j} (key{j} 0) vsource dc={dc_value}")
    spectre_code.append("")  # Add a blank line between each set

# Join the Spectre code lines
spectre_code_str = "\n".join(spectre_code)

# Print or save the Spectre code
print(spectre_code_str)

# Optionally, save to a file
with open("random_keys.scs", "w") as file:
    file.write(spectre_code_str)