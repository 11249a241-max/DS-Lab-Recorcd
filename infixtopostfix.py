def precedence(op):
    return {'+':1,'-':1,'*':2,'/':2,'^':3}.get(op,0)

def infix_to_postfix(expr):
    out = []
    st = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isspace():
            i += 1; continue
        if c.isalnum():
            j = i
            while j < len(expr) and expr[j].isalnum():
                j += 1
            out.append(expr[i:j]); i = j; continue
        if c == '(':
            st.append(c)
        elif c == ')':
            while st and st[-1] != '(':
                out.append(st.pop())
            st.pop()
        else:
            while st and precedence(st[-1]) >= precedence(c):
                out.append(st.pop())
            st.append(c)
        i += 1
    while st:
        out.append(st.pop())
    return ' '.join(out)

if __name__ == "__main__":
    print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))
