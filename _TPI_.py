def calcular_hormigon(longitud, anchura, altura, unidad_de_medida):
    if unidad_de_medida == "pies":
        longitud = longitud * 0.3048  # Convert feet to meters
        anchura = anchura * 0.3048
        altura = altura * 0.3048

    elif unidad_de_medida == "cm":
        longitud = longitud / 100  # Convert centimeters to meters
        anchura = anchura / 100
        altura = altura / 100

    volumen = longitud * anchura * altura
    return longitud, anchura, altura, volumen

def calcular_materiales(resistencia, volumen):
    if resistencia == 1:
        cantidad_cemento = (volumen * 420) * 1.05
        bolsas_cemento = (volumen * 8.4) * 1.05
        cantidad_arena = volumen * 0.67
        cantidad_grava = volumen * 0.67
        cantidad_agua = volumen * 220

    elif resistencia == 2:
        cantidad_cemento = (volumen * 350) * 1.05
        bolsas_cemento = (volumen * 7) * 1.05
        cantidad_arena = volumen * 0.56
        cantidad_grava = volumen * 0.84
        cantidad_agua = volumen * 180

    elif resistencia == 3:
        cantidad_cemento = (volumen * 300) * 1.05
        bolsas_cemento = (volumen * 6) * 1.05
        cantidad_arena = volumen * 0.48
        cantidad_grava = volumen * 0.96
        cantidad_agua = volumen * 170

    elif resistencia == 4:
        cantidad_cemento = (volumen * 260) * 1.05
        bolsas_cemento = (volumen * 5.2) * 1.05
        cantidad_arena = volumen * 0.63
        cantidad_grava = volumen * 0.96
        cantidad_agua = volumen * 170

    elif resistencia == 5:
        cantidad_cemento = (volumen * 210) * 1.05
        bolsas_cemento = (volumen * 4.2) * 1.05
        cantidad_arena = volumen * 0.5
        cantidad_grava = volumen * 1
        cantidad_agua = volumen * 160

    return bolsas_cemento, cantidad_arena, cantidad_grava, cantidad_agua, cantidad_cemento

# Función para guardar el pedido en un archivo de control
def guardar_pedido(cliente):
    with open("archivo_de_control.txt", "a") as control:
        control.write(f"Cliente: {cliente}, Dimensiones de la superficie: {longitud} x {anchura} x {altura} m3\n")
    control.close()

# Función para generar un archivo para imprimir
def generar_archivo_impresion(cliente):
    archivo_para_imprimir = f"Pedido para: =========={cliente}==========\n"
    archivo_para_imprimir += f"-------------Dimensiones de la superficie------------- \nLongitud: {longitud} m \nAnchura: {anchura} m \nAltura: {altura} m\n"
    archivo_para_imprimir += f"-------------Volumen de la superficie------------- \nvolumen: {volumen} m3\n"
    archivo_para_imprimir += f"--------------------------Materiales--------------------------\n"
    archivo_para_imprimir += f"\nLa Cantida de Cemento a Utilizar: {cantidad_cemento} m3\n"
    archivo_para_imprimir += f"\nBolsas de cemento requeridas: {bolsas_cemento} de 50kg\n"
    archivo_para_imprimir += f"\nCantidad de arena requerida: {cantidad_arena} m3\n"
    archivo_para_imprimir += f"\nCantidad de grava requerida:{cantidad_grava} m3\n"
    archivo_para_imprimir += f"\nCantidad de Agua requerida: {cantidad_agua} L\n"
    return archivo_para_imprimir



# Function principal del programa
print("=================== Calculadora de Hormigón ===================")
cliente = input("\n/ / /---Nombre del cliente---\ \ \ \n-> ")

#primera validacion

while True:
 unidad_de_medida = input("\n--------Unidad de medida en la que se ingresarán los datos--------\n \nUnidades: (m, pies, cm) \n* m -> (metros) \n* pies -> (pies) \n* cm -> (centímetros) \n\n->  ").lower()
 if unidad_de_medida in ["m", "pies", "cm"]:
      break
 else:
     print("Por favor, ingresa solo 'm' para metros, 'pies' para pies o 'cm' para centímetros.")

#segunda validacion
print("\n--------Ingreso de Datos--------")
while True:
 try:
     longitud = float(input("\nLongitud de la superficie: ->  "))
     anchura = float(input("\nAnchura de la superficie: ->  "))
     altura = float(input("\nAltura de la superficie: ->  "))
 except ValueError:
     print("--------Error--------: -> Debes ingresar solo números")
 else:
     if longitud and altura and anchura == str:
        print("--------Error--------: -> Debes ingresar solo números .")
        longitud = float(input("\nLongitud de la superficie: ->  "))
        anchura = float(input("\nAnchura de la superficie: ->  "))
        altura = float(input("\nAltura de la superficie: ->  "))

     else:
         break
volumen = longitud * anchura * altura

print("\n--------Ingreso de la resistencia del Concreto--------")
resistencia = int(input("\nResistencia del concreto: (1, 2, 3, 4, 5) \n* 1 -> 246 kg*m2, \n* 2 -> 210 kg*m2, \n* 3 -> 175 kg*m2, \n* 4 -> 140 kg*m2, \n* 5 -> 105 kg*m2\n\n-> "))

#tercera validacion
while 1 < resistencia > 5:
      print("--------Error--------: -> ingrese solos numeros del 1 al 5 ")
      resistencia = int(input("Resisrencia: -> "))

longitud, anchura, altura, volumen = calcular_hormigon(longitud, anchura, altura, unidad_de_medida)
bolsas_cemento, cantidad_arena, cantidad_grava, cantidad_agua, cantidad_cemento = calcular_materiales(resistencia, volumen)

# Guardar el pedido en un archivo de control
guardar_pedido(cliente)

# Generar el archivo para imprimir
generar_archivo_impresion(cliente)
archivo_impresion = generar_archivo_impresion(cliente)

# Guardar el archivo para imprimir
imprimir = open("archivo_para_imprimir.txt", "w")
imprimir.write(archivo_impresion)
print("\n-------------------------------------------------------------------")
print("/ / / /Pedido registrado y archivo para imprimir generado\ \ \ \.")
print("-------------------------------------------------------------------\n")
imprimir.close()


print("\n================Datos================")
print(f"Nombre del cliente: {cliente}\n\nUnidad de medida Utilizada: {unidad_de_medida}\n\nResistencia Utilizada: {resistencia}")
print("=====================================\n")

print("\n=============Dimensiones de la superficie expresada en metos=============")
print(f"Longitud: {longitud} m\nAnchura: {anchura} m\nAltura: {altura} m \nVolumen: {volumen} m3")
print("=========================================================================\n")

print("\n===========================================Materiales===========================================")
print(f"La Cantida de Cemento a Utilizar: {cantidad_cemento} m3 \n\nLa cantidad de bolsas de cemento que se van a utilizar son: {bolsas_cemento} de 50kg\n\nLa cantidad de grava que se va a utilizar es: {cantidad_grava} m3\n\nLa cantidad de arena que se va a utilizar es: {cantidad_arena} m3 \n\nLa cantidad de agua que se va a utilizar es: {cantidad_agua} L")
print("================================================================================================\n")