def compare_binary_files(file1_path, file2_path):
    with open(file1_path, "rb") as file1, open(file2_path, "rb") as file2:
        differences = 0  # Initialize the counter for differences
        while True:
            byte1 = file1.read(1)
            byte2 = file2.read(1)
            
            if not byte1 and not byte2:
                break  # End of both files
            
            if byte1 != byte2:
                differences += 1  # Increment the difference counter

    return differences

if __name__ == "__main__":
    file1_path = "file1.bin"  # Replace with the actual file paths
    file2_path = "file2.bin"  # Replace with the actual file paths

    num_differences = compare_binary_files(file1_path, file2_path)

    if num_differences == 0:
        print("Files are identical.")
    else:
        print(f"Files differ in {num_differences} byte(s).")
