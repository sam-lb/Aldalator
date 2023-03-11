
TAX_MULT = 1.07

individual = {
    ""
}

def get_input(preprompt, prompt):
    result = []
    print(preprompt)
    while True:
        string = input(prompt)
        if string == "": break
        try:
            result.append(float(string))
        except ValueError:
            break
    return result
     


if __name__ == "__main__":
    meat = get_input("--- meat ---", "enter meat price > ")
    nut = get_input("--- nut ---", "enter nut price > ")
    other = get_input("--- other ---", "enter item price > ")

    meat_total = sum(meat)
    nut_total = sum(nut)
    other_total = sum(other)
    subtotal = meat_total + nut_total + other_total
    total = TAX_MULT * subtotal

    print(
        f"""
        Meat total: {meat_total}
        Nut total: {nut_total}
        Other total: {other_total}
        --------------------------
        Subtotal: {subtotal}
        Total: {total}
        """
    )
