# solucion: Motor de inferencia en Python.
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
        
```
- ¿Cuál es la diferencia principal entre un sistema experto y un programa de software tradicional?
  -----------------------

- ¿Por qué se dice que los sistemas expertos tienen conocimiento separado de su motor de razonamiento? ¿Cuál es la ventaja de esto?
  -------------------
- ¿Qué es la base de hechos y en qué se diferencia de la base de conocimiento?
  -------------------
- ¿Qué significa que un sistema experto pueda "explicar su razonamiento"? ¿Por qué esto es importante en medicina o derecho?
  --------
- ¿Por qué fracasaron comercialmente los sistemas expertos en los años 90? Menciona al menos 3 razones.
  ----------
- Dada la siguiente regla: SI (fiebre AND tos) OR perdida_olfato ENTONCES sospecha_covid y los hechos: {fiebre=True, tos=False, perdida_olfato=True} — ¿Se activa la regla? ¿Por qué?
  -------------------------
- Completa la tabla de verdad para la expresión (A AND NOT B) OR (NOT A AND B) para todos los valores posibles de A y B.
  -------------------
- ¿Cuál es la diferencia entre encadenamiento hacia adelante y hacia atrás? Da un ejemplo de una situación real donde usarías cada uno.
  -----------
- Diseña 3 reglas IF-THEN para un sistema experto que asesore a estudiantes sobre qué lenguaje de programación aprender primero, basándose en su objetivo (desarrollo web, análisis de datos, desarrollo de videojuegos).
  -----------------
- Dibuja la red de inferencia correspondiente a las 3 reglas que diseñaste en la pregunta anterior.
  ----------------------
- ¿Qué problema de diseño podría surgir si dos reglas tienen exactamente las mismas condiciones pero conclusiones diferentes? ¿Cómo lo resolverías?
