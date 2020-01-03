if __name__ == "__main__" :

    final_states = set()
    current_states = set()
    #--------------------------------------------------------------------------
    # Read file and initialize variables
    f = open('automatoNondeterministicEtransitions.txt', 'r')

    number_of_states = int(f.readline())
    print("Number of states : ", number_of_states)

    starting_state = int(f.readline())
    current_states.add(starting_state)
    print("Starting state : ", starting_state)

    number_of_finalStates = int(f.readline())
    print("Number of final states : ", number_of_finalStates)

    final_states.update(f.readline().split())
    final_states = set(map(int, final_states)) #convert into a list of integers
    print("Final states : ", final_states)

    number_of_transitions = int(f.readline())
    print("Number of transitions : ", number_of_transitions)

    transitions_dict = {} #Explained above
    transitions_dict_e = {} #Explained above

    #transitions_dict : A dictionary with two keys (expected current state and expected input) and value (next state)
    #key[0] = expected current state
    #key[1] = expected input
    #value  = next state (if key-conditions are satysfied)
    #Example : If you are in position key[0] and input is key[1] go to value
    #transitions_dict_e : The same type of dictionary but for the 'e' transitions (the transitions that does not require input)

    #Initialization of the dictionaries
    for line in f:
        line = line.split()

        key = tuple([int(line[0]),line[1]])
        value = tuple([int(line[2])])

        #If the 'character to be written' is '#' (e.g. 3 # 2) append the transitions_dict_e dictionary else append the transitions_dict dictionary
        if line[1] != '#': #The character '#' represents the no-input
            if key in transitions_dict.keys():
                transitions_dict[key] = transitions_dict[key] + value
            else:
                transitions_dict.update({
                    key : value
                })
        else:
            if key in transitions_dict_e.keys():
                transitions_dict_e[key] = transitions_dict_e[key] + value
            else:
                transitions_dict_e.update({
                    key : value
                })

    print("Transitions : ", transitions_dict)
    print("Transitions of e: ", transitions_dict_e)
    #--------------------------------------------------------------------------
    # Read a word from the user
    word = input("Type a word to be checked : ")

    temp_current_states = set() #keeps the temporary state while executing

    # Execute the automato for the given word
    for letter in word:
        for cs_idx, cs in enumerate(current_states.copy()):
            for key_e, value_e in transitions_dict_e.items():
                if cs == key_e[0] and key_e[1] == '#':
                    current_states.remove(key_e[0])
                    cs = value_e[0]
            for key, value in transitions_dict.items():
                if key[1] == letter and key[0] == cs:
                    temp_current_states.update(value)
                
        current_states.clear()
        current_states.update(temp_current_states)
        temp_current_states.clear()
    #--------------------------------------------------------------------------
    # Check if a current positions is contained in the final_states list after the automato executed and print the results
    if any(x in current_states for x in final_states):
        print("The given word is acceptable !")
    else:
        print("The given word is inacceptable :(")

    print("Current states : ", current_states)
    print("Final states : ", final_states)



