from flask import Flask, render_template, request

#  Creamos la instancia de la aplicacion Flask
app = Flask(__name__)

# Definimos la clave secreta para el manejo seguro de sesiones, para ejercicio2
app.secret_key = 'UnaClaveSecretaMuySegura'


# Aqui definimos la ruta raiz
@app.route('/')
def index():
    return render_template('index.html')


# Definimos una funcion para el calculo del descuento
def calcular_descuento(edad, total_base):
# Inicializamos el porcentaje de descuento con monto en 0
    descuento_porcentaje = 0
#Aplicamos logica de descuento segun instructivo de examen segun edad!
    if edad >= 18 and edad <= 30:
        descuento_porcentaje = 0.15
    elif edad > 30:
        descuento_porcentaje = 0.25
    descuento_monto = total_base * descuento_porcentaje
    total_final = total_base - descuento_monto
#Retornamos el monto
    return descuento_monto, total_final

#Definimos la ruta para el Ejercicio1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    #Si la solicitud es POST, procesamos los datos del formulario
    if request.method == 'POST':
        nombre = request.form['nombre']
        # Convertimos datos a enteros/flotantes para realizar calculos
        try:
            edad = int(request.form['edad'])
            cantidad = int(request.form['cantidad'])
        except ValueError:
            # Manejo de errores si los datos no son numericos
            return render_template('ejercicio1.html',
                                   error="Por favor, ingresa valores numéricos válidos para Edad y Cantidad.")
        #El valor de cada tarro es de $9000 segun instructivo
        VALOR_TARRO = 9000
        total_sin_descuento = cantidad * VALOR_TARRO
        #  Usamos la funcion para aplicar la logica de descuento
        descuento_monto, total_a_pagar = calcular_descuento(edad, total_sin_descuento)
        # Renderizamos la plantilla nuevamente para mostrar resultados
        return render_template('ejercicio1.html',
                               resultado_nombre=nombre,
                               total_sin_descuento=f"{total_sin_descuento:.0f}",
                               descuento_monto=f"{descuento_monto:.1f}",
                               total_a_pagar=f"{total_a_pagar:.1f}",

                               #Enviamos de vuelta los valores ingresados para que no se borren
                               nombre=nombre,
                               edad=edad,
                               cantidad=cantidad)

    return render_template('ejercicio1.html')



# DEFINICION DE LA RUTA PARA EL EJERCICIO2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    nombre = ''
    contrasena_simulada = ''
    #Si la solicitud es POST, procesamos la autenticacion
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        if contrasena:
            contrasena_simulada = '•••••'

    # Validamos los usuarios usando logica
        if nombre == 'juan' and contrasena == 'admin':
            mensaje = f"Bienvenido Administrador {nombre}"
        elif nombre == 'pepe' and contrasena == 'user':
            mensaje = f"Bienvenido Usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html',
                           mensaje=mensaje,
                           nombre=nombre,
                           contrasena_simulada=contrasena_simulada)


# BLOQUE DE EJECUCION FINAL donde inicia la aplicacion
if __name__ == '__main__':
    app.run(debug=True)