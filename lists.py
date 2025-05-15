# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 1:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3:5]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

def is_empty(list_to_check):
    if list_to_check == []:
        rta = True
    else:
        rta = False
    return rta

def check_lists(list_to_compare1, list_to_compare2):
    if (len(list_to_compare1) >= 3) and (len(list_to_compare2) >= 3):
        if list_to_compare1[2] == list_to_compare2[2]:
            rta = True
        else:
            rta = False
    elif (len(list_to_compare1) < 3) or (len(list_to_compare2) < 3):
        rta = False
    return rta

def list_of_lists(list_of_lists_to_modify):
    lista_nueva = [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2][-2:]]
    return lista_nueva
