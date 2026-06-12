# Solucion: Motor de inferencia en Python.
    Construccion de un sistema funcional para diagnostico de problemas tecnicos en computadoras.

## objetivo:

    Mejorar el codigo agregandole nuevas funciones, usando problemas comunes presentes en la mayor parte de computadoras y asi entregar la solucione de una mejor manera, facilitando el diagnóstico de las máquinas y sus distintos compontes.

## Explicacion de componentes:

```texto

    * base_de_conocimiento[]
        contiene problemas comunes en la computadora, estos estan registrados con un 'id', 'descripcion' (describe la falla que se presenta), 'condiciones' (posibles causas del problema), 'conslusion' (brnda una recomendacion para solucionar el problema.), 'confianza' (brinda un porcentaje de seguridad a la solucion completa del problema)
    
    * preguntas_de_diagnostico.
        aqui tenemos registrados para detectar el podible problema.

    * encadenamiento_atras
        esta funcion busca en la base de datos la regla especifica por si ID y devuelve la lista de precondiciones necesarias.
    
    *exportar_red:
        construye un diccionario que reprecenta los nodos (sintomas y reglas) y sus conexiones, convirtiendolo en formato JSON para su posible uso en herramientas de visualizacion de grafos.

    * procesar_diagnositco:
        Filtra, ordena y presenta.
        muestra las soluciones mas probables primero, ayudando a priorizar las reparaciones.
    
    * iniciar_sistema
      Automatiza la recoleccion de informacion. Sin esta funcion, tendriamos que ingresar los datos manualmente en el codigo.
      Esta funcion hace que todo sea mucho mas facil de utilizar.
```
- ¿Cuál es la diferencia principal entre un sistema experto y un programa de software tradicional?

  Un sistema experto esta diseñado para solucionar un problema en base a los conocimientos que nosotros le brindemos enfocandolo en un area. Por lo tantop imita el razonamiento humano.

  un software esta diseñado para realizar una tarea especifica sin contener informacion. conteniendo asi algoritmos rigidos.
  
  -----------------------

- ¿Por qué se dice que los sistemas expertos tienen conocimiento separado de su motor de razonamiento? ¿Cuál es la ventaja de esto?

 Este tiene su motor de inferencia y base conocimiento el cual sabe aplicar reglas mas no que reglas aplicar.

  -------------------
- ¿Qué es la base de hechos y en qué se diferencia de la base de conocimiento?
  la base conocimientos es permanente mietras  la base de hechos contiene los datos del problema actual.

  -------------------

- ¿Qué significa que un sistema experto pueda "explicar su razonamiento"? ¿Por qué esto es importante en medicina o derecho?
  
  esto quiere decir que el experto puede mostrar las reglas que aplico, ejemplo(R01--> R05 --> conclusion) que lo lleva e un resultado.
  Esto mismo es importante en medicina o derecho ya que el expertoo humano deve evaluar los hechos (acusaciones o sintomas ) para poder aplicar las centencias o asignar la medicina correcta a la persona. 
  
  --------

- ¿Por qué fracasaron comercialmente los sistemas expertos en los años 90? Menciona al menos 3 razones.
  
  porque era dificil de mantener, rigidez de las reglas y y su falta de flexibiolidad ya que se especificaban unicamente e n un area.
  ----------
- Dada la siguiente regla: SI (fiebre AND tos) OR perdida_olfato ENTONCES sospecha_covid y los hechos: {fiebre=True, tos=False, perdida_olfato=True} — ¿Se activa la regla? ¿Por qué?

  si se cumple ya se cumple el sintoma OR perdida_olfato y esto basta para que la condicion OR sea verdadera.

  -------------------------
- Completa la tabla de verdad para la expresión (A AND NOT B) OR (NOT A AND B) para todos los valores posibles de A y B.


    ```tabla
  (A AND NOT B) OR (NOT A AND B)

  Esta es la operación XOR (OR exclusivo).

  A ----------B----A AND NOT B -----NOT A AND B------Resultado

  V-----------V-------------F---------------------F----------------F

  V-----------F-------------V---------------------F----------------V

  F-----------V-------------F---------------------V----------------V

  F-----------F-------------F---------------------F----------------F
    ```
    -------------------
- ¿Cuál es la diferencia entre encadenamiento hacia adelante y hacia atrás? Da un ejemplo de una situación real donde usarías cada uno.

  Adelante: parte de los datos para llegar a una conclusion.
  atras: parte de una hipotesis o cunclusion para ver si los datos se cumplen.

  -----------
- Diseña 3 reglas IF-THEN para un sistema experto que asesore a estudiantes sobre qué lenguaje de programación aprender primero, basándose en su objetivo (desarrollo web, análisis de datos, desarrollo de videojuegos).
  
  ```
  SI objetivo == "desarrollo_web" ENTONCES aprender == "JavaScript"

  SI objetivo == "analisis_de_datos" ENTONCES aprender == "Python"

  SI objetivo == "desarrollo_videojuegos" ENTONCES aprender == "C#"

  ```
  -----------------
- Dibuja la red de inferencia correspondiente a las 3 reglas que diseñaste en la pregunta anterior.


  ----------------------
- ¿Qué problema de diseño podría surgir si dos reglas tienen exactamente las mismas condiciones pero conclusiones diferentes? ¿Cómo lo resolverías?

  Si llegara apasar esto el experto caeria a un conflicto de resolucion.

  - problema: confusion logica.
  - solucion: 
    - elegir la de mayor confianza.
    - o hacer la regla con mas condiciones.
    - evaluar las coinsidencias.
    - aplicar las primeras dos.
    - agregar mas condiciones a las base de conocimientos, para poder especificar con mator exactitud el problema.
  

  -------------

# herramientas utilizadar.

  ```

  ---python

  ---visual studio Code.

  ---github
```

# autor 

* BRANDON ESTIBEN IXEN TELEGUARIO.
* ixenbrandonestiben@gmail.com
  