def event_to_json(event_line):
    # Split event line by comma
    tokens = event_line.split(',')

    # Extract event name
    event_name = tokens[0]

    # Create JSON-like output string
    output = []
    output.append('{"eventName":"' + event_name + '"')

    for i, token in enumerate(tokens[1:], 1):
        # Everything is treated as a string now
        output.append(', "param{}":"{}"'.format(i, token.replace('"', '\\"')))

    # Close JSON string
    output.append("}")

    return "".join(output)

def process_events_from_file(filename, start_line):
    # Determine output file name based on input file
    output_filename = filename.rsplit('.', 1)[0] + '_converted.txt'

    with open(filename, 'r') as f, open(output_filename, 'w') as out_f:
        for current_line_number, line in enumerate(f, 1):  # Start line numbers at 1
            if current_line_number < start_line:
                continue  # Skip lines before the starting line

            line = line.strip()  # Remove any leading/trailing whitespace
            if line:  # Check line is not empty
                out_f.write(event_to_json(line) + "\n")

    print(f"Converted events saved to: {output_filename}")

if __name__ == "__main__":
    filename = input("Enter the filename with events: ")
    start_line = int(input("Enter the line number to start at: "))

    process_events_from_file(filename, start_line)
