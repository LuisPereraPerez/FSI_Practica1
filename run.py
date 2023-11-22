# Search methods

import search


ab = search.GPSProblem('A', 'B', search.romania)

print("\n----------------------------------\n")
print("A --> B\n")

print("Búsqueda por Niveles:")
print(search.breadth_first_graph_search(ab).path())

print("\nBúsqueda por Profundidad:")
print(search.depth_first_graph_search(ab).path())

print("\nBúsqueda por Ramificación y Acotación:")
print(search.branch_and_bound(ab).path())

print("\nBúsqueda por Ramificación y Acotación con Subestimación:")
print(search.branch_and_bound_h(ab).path())

print("\n----------------------------------\n")

"""

oe = search.GPSProblem('O', 'E', search.romania)

print("\n----------------------------------\n")
print("O --> E\n")
print("Búsqueda por Niveles:")
print(search.breadth_first_graph_search(oe).path())
print("\nBúsqueda por Profundidad:")
print(search.depth_first_graph_search(oe).path())
print("\nBúsqueda por Ramificación y Acotación:")
print(search.branch_and_bound(oe).path())
print("\nBúsqueda por Ramificación y Acotación con Subestimación:")
print(search.branch_and_bound_h(oe).path())
print("\n----------------------------------\n")


gz = search.GPSProblem('G', 'Z', search.romania)

print("\n----------------------------------\n")
print("G --> Z\n")
print("Búsqueda por Niveles:")
print(search.breadth_first_graph_search(gz).path())
print("\nBúsqueda por Profundidad:")
print(search.depth_first_graph_search(gz).path())
print("\nBúsqueda por Ramificación y Acotación:")
print(search.branch_and_bound(gz).path())
print("\nBúsqueda por Ramificación y Acotación con Subestimación:")
print(search.branch_and_bound_h(gz).path())
print("\n----------------------------------\n")




nd = search.GPSProblem('N', 'D', search.romania)

print("\n----------------------------------\n")
print("N --> D\n")
print("Búsqueda por Niveles:")
print(search.breadth_first_graph_search(nd).path())
print("\nBúsqueda por Profundidad:")
print(search.depth_first_graph_search(nd).path())
print("\nBúsqueda por Ramificación y Acotación:")
print(search.branch_and_bound(nd).path())
print("\nBúsqueda por Ramificación y Acotación con Subestimación:")
print(search.branch_and_bound_h(nd).path())
print("\n----------------------------------\n")




mf = search.GPSProblem('M', 'F', search.romania)

print("\n----------------------------------\n")
print("M --> F\n")
print("Búsqueda por Niveles:")
print(search.breadth_first_graph_search(mf).path())
print("\nBúsqueda por Profundidad:")
print(search.depth_first_graph_search(mf).path())
print("\nBúsqueda por Ramificación y Acotación:")
print(search.branch_and_bound(mf).path())
print("\nBúsqueda por Ramificación y Acotación con Subestimación:")
print(search.branch_and_bound_h(mf).path())
print("\n----------------------------------\n")

"""