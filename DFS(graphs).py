def dfs(graph, start):
    vis = set(); st = [start]; order = []
    while st:
        u = st.pop()
        if u in vis: continue
        vis.add(u); order.append(u)
        for v in reversed(graph.get(u, [])):
            if v not in vis: st.append(v)
    return order

if __name__ == "__main__":
    g = {1:[2,3],2:[4],3:[4],4:[]}
    print(dfs(g,1))
