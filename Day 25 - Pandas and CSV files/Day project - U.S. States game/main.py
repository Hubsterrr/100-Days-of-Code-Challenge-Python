from write import Write
import turtle
import pandas

# Variables
answered_states = []

# Generate screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Assign Write class with typing on screen functionality
write = Write()

# Assign states data and create list of state names
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(answered_states) < len(data.state):

    answer_state = screen.textinput(title=f"{len(answered_states)}/50 Guess the state", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        not_answered_states = all_states

        for state in all_states:
            if state not in answered_states:
                not_answered_states.append(state)

        states_at_the_end = pandas.DataFrame(not_answered_states)
        states_at_the_end.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        answered_states.append(answer_state)
        # Write answered state on the map
        state_row = data[data.state == answer_state]
        write.write_state(int(state_row.x), int(state_row.y), answer_state)




