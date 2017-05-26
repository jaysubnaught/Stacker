# Given a set of n real, positive values representing box sizes (heights) and an opening of height H,
# find all of the combinations of box sizes that will fill or most nearly fill the opening.

import json                                # Useful routines for file i/o


def record(c):  # Record the latest result as comma separated values in the output file, adding one line to the file.
    for i in range(1, n):
        out_file.write(str(c[i]))
        out_file.write(", ")
    out_file.write("\n")
    return


def stack(h, level):  # Recursively called routine to fill the space H with boxes of progressively smaller sizes.
    last_level = (level == n - 1)           # TRUE if this is the smallest of the defined box sizes.
    if last_level:
        Counts[level] = int(h / Sizes[level])
        record(Counts)                      # Wait to record results until every box size has been tested.
    else:
        max_count = int(h / Sizes[level])   # Calculate the max number of my boxes that can fit in the available space.
        for i in range(max_count, -1, -1):  # After each call to next level, remove a box and try again
            Counts[level] = i               # Set the current box count for current level
            next_h = h - i * Sizes[level]   # Subtract that many box heights to get remaining height.
            next_level = level + 1          # If so, stack in the next smaller size box
            stack(next_h, next_level)       # Call the stack routine for the next smaller size box.
    return

# Main body of the program
Sizes = [0, 23.2, 20, 16, 12] # Without coding an input program, define the box sizes in order.
                                            # The leading 0 entry in the list is not used.
H = 500                                     # Define the opening height into which the boxes will be fitted.

out_file = open('Stacker_out_file.csv', 'w')  # Open a file to capture results

n = len(Sizes)                              # Determine how long is the list of sizes
Counts = [0] * n                            # Also define and initialize a matching list of count values for each box size.
                                            # Create a file header
out_file.write("Sizes \n")
record(Sizes)
out_file.write("\nHeight \n")
json.dump(H, out_file)
out_file.write("\n\nCounts\n")

print('Running Stacker')                    # Call the first stack routine, which will call all of the others.
stack(H, 1)

out_file.close()
