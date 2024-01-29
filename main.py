def remove_duplicates():
    input_file = "list.txt"
    output_file = "list_wo_dupes.txt"

    unique_lines = set()

    with open(input_file, 'r') as file:
        for line in file:
            if line not in unique_lines:
                unique_lines.add(line)
            else:
                print("Duplicate: " + line)

    with open(output_file, 'w') as file:
        for line in unique_lines:
            # Depending on the formatting of the file, you may need to adjust the following line
            #file.write(line + '\n')
            file.write(line)

if __name__ == '__main__':
    remove_duplicates()
