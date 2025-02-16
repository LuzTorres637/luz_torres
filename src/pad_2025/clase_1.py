# class - relacion directa con el objeto (entidad o objeto)
# def - acciones o funciones del obejto

class Personas():
    def __init__(self):
    # atributos del obejto
        self.nombre = "Andres"
        self.edad = 0
        self.estatura = 100.0 
        self.peso = 35.6
    
        
persona =Personas()  
persona.edad = 42
persona.estatura =193 
print(persona.nombre) 
print("nombre: ",persona.nombre," edad: ",persona.edad, " cms: ", persona.estatura)
print("nombre: ",persona.nombre," edad: ",persona.edad, " cms: ", persona.estatura)