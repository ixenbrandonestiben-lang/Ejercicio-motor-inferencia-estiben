import json

# ================================================================
# SISTEMA EXPERTO: Diagnóstico de PC (Versión Mejorada)
# ================================================================

# Nivel 1: Base de Conocimiento con reglas adicionales
base_de_conocimiento = [
    {"id": "R01", "descripcion": "Fuente de poder dañada", "condiciones": ["no_enciende", "sin_luces", "sin_sonido"], "conclusion": "Revisar o reemplazar la fuente de poder", "confianza": 0.92},
    {"id": "R02", "descripcion": "Falla de RAM", "condiciones": ["enciende", "pitidos_arranque", "sin_video"], "conclusion": "Probar con módulos de RAM de a uno", "confianza": 0.88},
    {"id": "R03", "descripcion": "Falla de tarjeta de video", "condiciones": ["enciende", "pantalla_negra", "sin_pitidos"], "conclusion": "Revisar tarjeta de video", "confianza": 0.80},
    {"id": "R04", "descripcion": "Problemas de almacenamiento", "condiciones": ["enciende", "inicia_lento", "disco_al_100"], "conclusion": "Verificar salud del disco duro", "confianza": 0.85},
    {"id": "R05", "descripcion": "Infección por malware", "condiciones": ["enciende", "inicia_lento", "ventilador_siempre_activo"], "conclusion": "Escanear con antivirus", "confianza": 0.72},
    {"id": "R06", "descripcion": "Driver o RAM dañada", "condiciones": ["enciende", "pantalla_azul_frecuente"], "conclusion": "Actualizar drivers y testear RAM", "confianza": 0.87},
    {"id": "R07", "descripcion": "Sobrecalentamiento", "condiciones": ["enciende", "se_apaga_solo", "calor_excesivo"], "conclusion": "Limpiar ventiladores y pasta térmica", "confianza": 0.90},
    {"id": "R11", "descripcion": "Falla de red inalámbrica", "condiciones": ["enciende", "sin_internet", "wifi_no_detectado"], "conclusion": "Reinstalar driver de tarjeta Wi-Fi", "confianza": 0.75},
    {"id": "R12", "descripcion": "Problema de teclado", "condiciones": ["enciende", "teclas_no_responden", "teclado_bloqueado"], "conclusion": "Limpiar teclado o probar con USB externo", "confianza": 0.82},
    {"id": "R13", "descripcion": "Falla de sistema operativo", "condiciones": ["enciende", "no_inicia_windows", "error_boot"], "conclusion": "Reparar sector de arranque o reinstalar SO", "confianza": 0.95},
]

# Diccionario de preguntas para el usuario
PREGUNTAS = {
    "no_enciende": "¿El equipo NO enciende (sin luces, sin sonido)?",
    "sin_luces": "¿No hay ninguna luz LED encendida?",
    "sin_sonido": "¿No se escucha ningún sonido al encender?",
    "enciende": "¿El equipo SÍ enciende?",
    "pitidos_arranque": "¿Se escuchan pitidos al encender?",
    "sin_video": "¿La pantalla no muestra absolutamente nada?",
    "pantalla_negra": "¿La pantalla queda en negro?",
    "sin_pitidos": "¿No se escuchan pitidos?",
    "inicia_lento": "¿El equipo tarda más de 3 minutos en iniciar?",
    "disco_al_100": "¿El administrador de tareas muestra disco al 100%?",
    "ventilador_siempre_activo": "¿El ventilador está siempre a máxima velocidad?",
    "pantalla_azul_frecuente": "¿Aparece pantalla azul (BSOD) con frecuencia?",
    "se_apaga_solo": "¿El equipo se apaga solo?",
    "calor_excesivo": "¿El chasis está muy caliente?",
    "sin_internet": "¿No tienes conexión a internet?",
    "wifi_no_detectado": "¿El Wi-Fi no aparece como opción?",
    "teclas_no_responden": "¿Las teclas no escriben?",
    "teclado_bloqueado": "¿El teclado parece bloqueado?",
    "no_inicia_windows": "¿El sistema no carga Windows?",
    "error_boot": "¿Aparece un mensaje de 'No boot device found'?"
}

# Nivel 3: Encadenamiento hacia atrás
def encadenamiento_atras(meta_id):
    for regla in base_de_conocimiento:
        if regla['id'] == meta_id:
            return regla['condiciones']
    return None

# Nivel 4: Exportar red
def exportar_red():
    red = {"nodos": [], "aristas": []}
    for r in base_de_conocimiento:
        red["nodos"].append({"id": r['id'], "tipo": "conclusión", "desc": r['descripcion']})
        for cond in r['condiciones']:
            if {"id": cond, "tipo": "síntoma"} not in red["nodos"]:
                red["nodos"].append({"id": cond, "tipo": "síntoma"})
            red["aristas"].append({"origen": cond, "destino": r['id']})
    return json.dumps(red, indent=4, ensure_ascii=False)

# Nivel 2: Diagnóstico múltiple ordenado
def procesar_diagnostico(hechos):
    aplicables = [r for r in base_de_conocimiento if set(r['condiciones']).issubset(hechos)]
    ranking = sorted(aplicables, key=lambda x: x['confianza'], reverse=True)
    
    print("\n--- RESULTADOS DEL DIAGNÓSTICO ---")
    if not ranking:
        print("No se encontraron coincidencias exactas.")
    for i, r in enumerate(ranking, 1):
        print(f"{i}. [{r['id']}] {r['descripcion']} (Confianza: {r['confianza']*100:.0f}%)")
        print(f"   Recomendación: {r['conclusion']}")

# Interfaz principal
def iniciar_sistema():
    
    print("--- SISTEMA EXPERTO DE DIAGNÓSTICO ---")
    hechos = set()
    for sintoma, pregunta in PREGUNTAS.items():
        resp = input(f"{pregunta} (s/n): ").strip().lower()
        if resp == 's':
            hechos.add(sintoma)
    
    procesar_diagnostico(hechos)

if __name__ == "__main__":
    iniciar_sistema()