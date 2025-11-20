def eval_postfix(expr):
    st = []
    for tok in expr.split():
        if tok.lstrip('-').isdigit():
            st.append(int(tok))
        else:
            b = st.pop(); a = st.pop()
            if tok == '+': st.append(a+b)
            elif tok == '-': st.append(a-b)
            elif tok == '*': st.append(a*b)
            elif tok == '/': st.append(int(a/b))
            elif tok == '^': st.append(a**b)
    return st[0] if st else None

if __name__ == "__main__":
    print(eval_postfix("2 3 1 * + 9 -"))
