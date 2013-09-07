import pydot
graph = pydot.Dot(graph_type='digraph')
graph.set_graph_defaults(shape="box")
tree = []
seen = []
step = 1
def walk(step):
    p = Paragraph.objects.get(pk=step)
    options = p.option_set.all()
    for o in options:
        pair = [step, o.target]
        if pair not in seen:
            graph.add_edge(pydot.Edge(pair[0], pair[1]))
            seen.append(pair)
            walk(o.target)

walk(step)

graph.write_png('owned.png')