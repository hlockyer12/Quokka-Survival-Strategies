# from vertex import Vertex
# from graph import QuokkaMaze

# a = Vertex(False, 1)
# b = Vertex(False, 2)
# c = Vertex(False, 3)
# d = Vertex(False, 4)
# e = Vertex(True, 5)
# f = Vertex(False, 6)
# g = Vertex(False, 7)
# h = Vertex(False, 8)
# i = Vertex(False, 9)
# j = Vertex(False, 10)
# k = Vertex(False, 11)
# l = Vertex(False, 12)
# m = Vertex(False, 13)
# n = Vertex(False, 14)
# o = Vertex(False, 15)

# q = QuokkaMaze()

# q.add_vertex(a)
# q.add_vertex(b)
# q.add_vertex(c)
# q.add_vertex(d)
# q.add_vertex(e)
# q.add_vertex(f)
# q.add_vertex(g)
# q.add_vertex(h)
# q.add_vertex(i)
# q.add_vertex(j)
# q.add_vertex(k)
# q.add_vertex(l)
# q.add_vertex(m)
# q.add_vertex(n)
# q.add_vertex(o)

# # # TEST GRAPH BASIC
# # q.fix_edge(a, b)
# # q.fix_edge(b, c)
# # q.fix_edge(c, d)
# # q.fix_edge(d, e)
# # q.fix_edge(d, f)

# # # TEST GRAPH 1
# # q.fix_edge(a, b)
# # q.fix_edge(a, c)
# # q.fix_edge(b, e)
# # q.fix_edge(c, d)
# # q.fix_edge(c, e)
# # q.fix_edge(c, f)
# # q.fix_edge(d, f)
# # q.fix_edge(d, g)
# # q.fix_edge(e, h)
# # q.fix_edge(f, h)
# # q.fix_edge(g, i)
# # q.fix_edge(h, i)

# # # TEST GRAPH 2
# # q.fix_edge(a, d)
# # q.fix_edge(a, f)
# # q.fix_edge(b, c)
# # q.fix_edge(b, e)
# # q.fix_edge(c, h)
# # q.fix_edge(d, e)
# # q.fix_edge(d, f)
# # q.fix_edge(e, g)
# # q.fix_edge(g, i)
# # q.fix_edge(h, k)
# # q.fix_edge(i, j)
# # q.fix_edge(j, k)

# # # TEST GRAPH TREE
# # q.fix_edge(a, e)
# # q.fix_edge(b, c)
# # q.fix_edge(c, d)
# # q.fix_edge(c, g)
# # q.fix_edge(e, i)
# # q.fix_edge(f, j)
# # q.fix_edge(g, h)
# # q.fix_edge(h, i)
# # q.fix_edge(h, l)
# # q.fix_edge(i, j)
# # q.fix_edge(j, k)
# # q.fix_edge(j, m)

# # # TEST GRAPH BST
# # q.fix_edge(a, b)
# # q.fix_edge(a, c)
# # q.fix_edge(b, d)
# # q.fix_edge(b, e)
# # q.fix_edge(c, f)
# # q.fix_edge(c, g)
# # q.fix_edge(d, h)
# # q.fix_edge(d, i)
# # q.fix_edge(e, j)
# # q.fix_edge(e, k)
# # q.fix_edge(f, l)
# # q.fix_edge(f, m)
# # q.fix_edge(g, n)
# # q.fix_edge(g, o)

# # # TEST EXISTS EXAMPLE
# # q.fix_edge(a, b)
# # q.fix_edge(b, c)
# # q.fix_edge(c, d)
# # q.fix_edge(d, e)

# # TEST PATH ODD
# q.fix_edge(a, b)
# q.fix_edge(b, c)
# q.fix_edge(c, d)
# q.fix_edge(d, e)
# q.fix_edge(a, f)


# # q.find_path(b, m, 900)
# # names = []
# # if q.path != None:
# #     for x in q.path:
# #         names.append(x.name)
# # print(names)

# # print(q.exists_path_with_extra_food(a, e, 2, 1))

# path = q.find_path(a, f, 2)
# names = []
# if path != None:
#     for x in path:
#         names.append(x.name)
# print(names)
# print(q.exists_path_with_extra_food(a, f, 2, 1))
