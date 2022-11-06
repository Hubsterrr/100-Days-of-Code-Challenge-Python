#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = []

with open("Input/Letters/starting_letter.txt") as file:
    starting_line = file.readline()
    document = file.read()

with open("Input/Names/invited_names.txt") as file:
    for _ in range(8):
        name = file.readline()
        strip = name.strip("\n")
        invited_names.append(strip)

for name in invited_names:
    new_line = starting_line.replace("[name],", name + ",")
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file1:
        file1.write(new_line + document)

