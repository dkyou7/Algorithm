while True:
    n = input()
    st = []
    if n == ".": break

    for el in n:
        if el == "[" or el == "(":
            st.append(el)

        if el == "]":
            if len(st) >0 and st[-1] == "[":
                st.pop(-1)
            else:
                st.append(el)
                break

        if el == ")":
            if len(st) > 0 and st[-1] == "(":
                st.pop(-1)
            else:
                st.append(el)
                break
    if len(st) > 0:
        print("no")
    else:
        print("yes")
