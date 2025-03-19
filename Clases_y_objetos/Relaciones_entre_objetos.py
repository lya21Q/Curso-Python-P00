class Empleado:
    no_id = 1

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        self.id_Empleado = Empleado.no_id
        Empleado.no_id += 1

    def aumentar_sueldo(self, porcentaje: float) -> None:
        pass

    def __str__(self) -> str:
        return f"Empleado(id={self.no_id}, nombre={self.nombre}, sueldo= {self.sueldo})"

class Empresa:
    no_id =1
    def __init__(self,nombre:str,*empleados:Empleado):
        self.nombre=nombre
        self.empleados=list(empleados)
        Empresa.no_id += 1
    def agregar_empleados(self,*nuevos_empleados:Empleado):
        for empleados in nuevos_empleados:
            self.empleados.append(empleados)

    def __str__(self) -> str:
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"

    def remover_empleados(self, *empleados_a_remover: Empleado) -> None:
        """
        Se utiliza para remover un empleado de la empresa.
        :param empleados_a_remover: Empleado a remover de la empresa.
        """
        for empleado in empleados_a_remover:
            if empleado in self.empleados:
                self.empleados.remove(empleado)
            else:
                print(f"El empleado {empleado} no forma parte de {self.nombre}.")

if __name__ == '__main__':
    empleado1 = Empleado("Jose Ramirez", 250)
    empleado2 = Empleado("Maria Ramirez", 250)
    print(empleado1)
    print(empleado2)

    Unsij=Empresa("UNSIJ",empleado1,empleado2)
    Unsij.agregar_empleados(empleado1,empleado2)
    print(Unsij)


