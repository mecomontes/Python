def distancia(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2 - x1, y2 - y1
    
    return (dx ** 2 + dy ** 2) ** .5

def perimetro(vertices):
    n = len(vertices)
    suma = 0.0
    
    for i in range(n):
        a = vertices[i]
        b = vertices[(i + 1)%n]
        suma += distancia(a, b)
   
    return suma

p = [(4, 1), (7, 2), (7, 4), (5, 9)]

print(perimetro(p))