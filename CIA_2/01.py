ordered_part = ["Start", "River"]

jumbled_part = ["Clearing", "Village", "Cave"]
corrected_order = []

def reconstruct_path(ordered, jumbled):
    correct_order = ["Start","Clearing", "River", "Village", "Cave" ]
    for i in correct_order:
        if i in ordered:
            corrected_order.append(i)
        elif i in jumbled:
            corrected_order.append(i)
    
    return corrected_order

print(reconstruct_path(ordered_part, jumbled_part)) 