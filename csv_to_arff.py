import csv

def csv_to_arff(csv_filepath, attribute_filepath, output_arff_filepath, relation_name="dataset"):
    # Read attribute definitions from the attribute file
    with open(attribute_filepath, 'r') as attr_file:
        attribute_definitions = attr_file.read()

    # Open the CSV file and ARFF output file
    with open(csv_filepath, 'r') as csv_file, open(output_arff_filepath, 'w') as arff_file:
        csv_reader = csv.reader(csv_file)

        # Write the relation name and attribute definitions to the ARFF file
        arff_file.write(f"@relation {relation_name}\n\n")
        arff_file.write(attribute_definitions + "\n")

        # Extract the header (column names) from the CSV file
        header = next(csv_reader)

        # Write the data section header in the ARFF file
        arff_file.write("\n@data\n")

        # Write each row of the CSV file to the ARFF file
        for row in csv_reader:
            # Convert each row to a comma-separated string and write to ARFF
            arff_file.write(','.join(row) + "\n")

    print(f"Conversion completed: {output_arff_filepath} created.")

# Example usage
csv_to_arff("data.csv", "attribute_definitions.txt", "output_data.arff")
