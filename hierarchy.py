def grandparent(value):
    print("Entering grandparent")
    value += parent(value)
    print("Leaving grandparent")
    return value

def parent(value):
    print("Entering parent")
    breakpoint()
    value += child(value)
    print("Leaving parent")
    return value

def child(value):
    print("Entering child")
    value += value
    print("Leaving child")
    return value

value = grandparent(5)

print(f"El valor es {value}")