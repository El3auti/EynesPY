class Circulo:
    def __init__(self, radio):
        
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self.radio = radio
        

    def obtenerRadio(self):
        return self.radio
        
    def obtener_area(self):
        return 3.1416 * self._radio ** 2
        
    def obtenePerimetro(self):
        return 2 * 3.1416 * self.radio
        
    def __str__(self):
        return f"Circulo de radio {self.radio}🔴"
    
    def multiplica(self,n):
        if n <= 0:
            raise ValueError('El multiplicador debe ser mayor que cero')
        return Circulo(self.radio * n) 
        

nuevoCirculo = Circulo(10)
print(nuevoCirculo.radio * 0) 