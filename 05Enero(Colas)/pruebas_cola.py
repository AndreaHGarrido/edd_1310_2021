from cola import Queue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de Queue")
c1={ "id":1 , "nombre":"Mario" , "balance": 20.5 }
c2={ "id":2 , "nombre":"Diana" , "balance": 3456.5 }
c3={ "id":3 , "nombre":"Bartolo" , "balance": 1000000.0 }

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
sig = atencion.dequeue()
print(f"Bienvenido sr. { siguiente['nombre'] }, en que podemos servirle el día de hoy")
print(atencion.to_string())
