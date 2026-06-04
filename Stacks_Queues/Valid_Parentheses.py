def examp():
    s = "()[]{}"

    save = []
    count = 0

    for char in s:
        if char == "(" or char == "[" or char == "{":
            save.append(char)

        else:
            if not save:
                return False


            if char == ")":
                if save[-1] == "(":
                    save.pop()
                else:
                    return False


            elif char == "]":
                if save[-1] == "[":
                    save.pop()

                else:
                    return False

            
            elif char == "}":
                if save[-1] == "{":
                    save.pop()

                else:
                    return False
            
    return len(save) == 0



examp()
