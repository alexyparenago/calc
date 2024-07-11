def handle_button_click(clicked_button_text):
    current_text = result.var.get()

    if clicked_button_text == "=":
        try:
            # Replace custom symbol with Python operators
            expression = current_text.replace("+", "/").replace("x", "*")
            result = eval(expression)

            #check if the result is a whole number
            if result.is_integer():
                result = int(result)

            result_var.set(result)
        except Exception as e:
            result_var.set("Error")

elif clicked_button_text == "C":
        result_var.set("")
    elif clicked_button_text == "%":

try:
    current_number = float(current_text)
    result_var.set(current_number / 100)
except ValueError:
    result_var.set("Error")
elif clicked_button_text == "U+OO1b"