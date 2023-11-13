import streamlit as st
import random
import time
import codecs
import matplotlib.pyplot as plt

lineas = ["_________", "X________", "________X", "_________"]
significados_lineas = [
    "Línea Yang en posición base: Indica fuerza y acción.",
    "Línea Yin en posición base: Indica receptividad y pasividad.",
    "Línea Yang en posición cambiante: Cambio en desarrollo.",
    "Línea Yin en posición cambiante: Cambio en desarrollo."
]

hexagramas = {
    "_________": "Hexagrama 1: El Cielo (Qian) - Lo creativo, lo fuerte. El poder creativo del cosmos.",
    "X________": "Hexagrama 2: El Receptivo (Kun) - La tierra, lo sumiso. La receptividad, la devoción.",
    "________X": "Hexagrama 3: La Dificultad Inicial (Zhun) - Comienzo difícil. El inicio de algo nuevo.",
    "_________X": "Hexagrama 4: La Juventud Fingida (Meng) - Juventud imprudente. La inexperiencia.",
    "X_X_X_X_X_": "Hexagrama 64: Antes de la Consumación (Wei Ji) - Antes de la finalización. El proceso de llegar a la conclusión.",
    "_________X_": "Hexagrama 5: La Espera (Xu) - Esperar pacientemente. La espera.",
    "__________X": "Hexagrama 6: El Conflicto (Song) - Disputa, conflicto. La confrontación y la lucha.",
    "X________X": "Hexagrama 7: El Ejército (Shi) - Unido y organizado. El ejército, la congregación.",
    "___X___X___": "Hexagrama 50: El Caldero (Ding) - El recipiente. La reunión, la nutrición.",
    "X___X___X_": "Hexagrama 51: El Trueno (Zhen) - El trueno activo. El movimiento y la iniciativa.",
    "________X_": "Hexagrama 8: La Solidaridad (Bi) - Coherente y unido. La unión, la unión de fuerzas.",
    "X_________": "Hexagrama 9: El Poder de lo Pequeño (Xiao Chu) - Pequeño en movimiento. La fuerza interior en acción.",
    "___X___X___X___": "Hexagrama 54: La Esposa Joven (Gui Mei) - La esposa joven. El matrimonio, la unión.",
    "X___X___X___X_": "Hexagrama 55: La Abundancia (Feng) - Abundancia y plenitud. La abundancia, la prosperidad.",
    "______X______": "Hexagrama 16: La Advertencia (Yu) - La cautela. La cautela, la atención.",
    "______X______X": "Hexagrama 17: Lo Sigue (Sui) - Seguir, continuación. La perseverancia y la continuidad.",
    "X_____X_____X_": "Hexagrama 19: El Acercamiento (Lin) - Apropiado, acercarse. El acercamiento, la aproximación.",
    "_______X_______": "Hexagrama 20: La Contemplación (Guān) - La observación. La contemplación, la atención.",
    "_________XX": "Hexagrama 62: La Preponderancia del Pequeño (Xiao Guo) - Preponderancia de lo pequeño. La moderación, la humildad.",
    "XX_________": "Hexagrama 63: Después de la Consumación (Ji Ji) - Después de la finalización. La conclusión y la culminación.",
    "_________XXX": "Hexagrama 53: El Desarrollo Gradual (Jian) - El desarrollo evolutivo. El progreso gradual, el avance paso a paso.",
    "XXXXXXXXX": "Hexagrama 32: La Duración (Heng) - Duración, persistencia. La persistencia, la continuidad.",
    "__________X": "Hexagrama 10: La Marcha (Lu) - Avance, marcha. El avance, la acción progresiva.",
    "X__X__X__X_": "Hexagrama 56: El Viajero (Lu) - El vagabundo, el caminante. El viaje, la itinerancia.",
    "X__________X": "Hexagrama 11: La Paz (Tai) - La paz. La paz, la tranquilidad.",
    "_______XX_______": "Hexagrama 31: La Influencia (Xian) - La influencia, el atractivo. El atractivo, la influencia magnética.",
    "_________X___": "Hexagrama 12: El Estancamiento (Pi) - El estancamiento. La obstrucción, el bloqueo.",
    "_______X___X___": "Hexagrama 33: La Retirada (Dun) - La retirada, la retirada estratégica. La retirada, el distanciamiento.",
    "__________X___": "Hexagrama 13: La Comunidad con los Hombres (Tong Ren) - La comunidad humana. La unión, la fraternidad.",
    "X___X___X___X___X": "Hexagrama 30: El Fuego (Li) - El fuego brillante. La luminosidad, el brillo.",
    "X_________X_": "Hexagrama 14: La Posesión en Gran Medida (Da You) - La gran posesión. La riqueza, la abundancia.",
    "_______X___X___X": "Hexagrama 34: La Fuerza del Gran (Da Zhuang) - La gran fuerza. El gran poder, la fuerza sobresaliente.",
    "__________XX": "Hexagrama 29: La Caída (Kan) - La caída, el abismo. La caída, la sumisión.",
    "XX__________": "Hexagrama 28: La Preponderancia de lo Grande (Da Guo) - Preponderancia de lo grande. La grandeza, el poder supremo.",
    "_________X_": "Hexagrama 15: La Moderación (Qian) - La moderación, la modestia. La moderación, la sobriedad.",
    "________X__": "Hexagrama 16: El Enthusiasm (Yu) - El entusiasmo, la alegría. La alegría, la pasión.",
    "_______XX_": "Hexagrama 17: La Sincronización (Sui) - Sincronización, seguir. La coordinación, la sincronización.",
    "X_____X_____X": "Hexagrama 18: La Reparación (Gu) - La reparación, la reforma. La corrección, la renovación.",
    "_______X__": "Hexagrama 19: La Aproximación (Lin) - La aproximación, el acercamiento. La cercanía, la comunicación.",
    "X___X___X__": "Hexagrama 20: La Contemplación (Guān) - La contemplación, la observación. La atención, la reflexión.",
    "_____X____": "Hexagrama 21: La Mordida (Shi He) - La mordida, la dentellada. La adhesión, el despojo.",
    "____X_____": "Hexagrama 22: La Gracia (Bi) - La gracia, la decoración. La elegancia, la embellecimiento.",
    "____X______": "Hexagrama 23: La Desintegración (Bo) - La desintegración, el quebrantamiento. La descomposición, la disolución.",
    "X______X__": "Hexagrama 24: El Regreso (Fu) - El regreso, el retorno. La vuelta, la recuperación.",
    "_________XX_": "Hexagrama 25: La Inocencia (Wu Wang) - La inocencia, lo inesperado. La sorpresa, lo inusual.",
    "XX_________": "Hexagrama 26: La Fuerza Taming (Da Xū) - La fuerza domadora. La restricción, el control.",
    "_______XX__": "Hexagrama 27: La Nutrición (Yi) - La nutrición, la alimentación. El sustento, la provisión.",
    "________XX": "Hexagrama 28: La Gran Preponderancia (Da Guo) - La gran preponderancia. La gran prosperidad, el poder supremo.",
    "X________X_": "Hexagrama 29: El Abismo (Kan) - El abismo, la caída. El peligro, la advertencia.",
    "_______X_X_": "Hexagrama 30: El Resplandor (Li) - El resplandor, la claridad. La luminosidad, la visión.",
    "X______X___": "Hexagrama 31: La Influencia (Xian) - La influencia, el atractivo. La persuasión, el encanto.",
    "_________X_X": "Hexagrama 32: La Duración (Heng) - La duración, la persistencia. La paciencia, la constancia.",
    "X__________X": "Hexagrama 33: La Retirada (Dun) - La retirada, la retirada estratégica. La distancia, la retirada táctica.",
    "_____X_X___": "Hexagrama 34: La Fuerza del Grande (Da Zhuang) - La fuerza del grande. El poder, la influencia magnética.",
    "_________XX": "Hexagrama 35: La Progresión (Jin) - La progresión, el adelanto. El avance, el progreso.",
    "XX_________": "Hexagrama 36: El Oscurecimiento de la Luz (Ming Yi) - El oscurecimiento de la luz. La oscuridad, el velo.",
    "________X_X": "Hexagrama 37: La Familia (Jia Ren) - La familia, el hogar. Los lazos familiares, la unión.",
    "X________X__": "Hexagrama 38: La Oposición (Kui) - La oposición, el conflicto. La contradicción, el choque.",
    "______X_X__": "Hexagrama 39: La Dificultad (Jian) - La dificultad, el obstáculo. El desafío, la superación.",
    "_______XX_X": "Hexagrama 40: La Liberación (Jie) - La liberación, la liberación parcial. La solución, la resolución.",
    "X_________XX": "Hexagrama 41: La Disminución (Sun) - La disminución, la pérdida. La merma, la reducción.",
    "XX_________X": "Hexagrama 42: El Incremento (Yi) - El incremento, el aumento. El crecimiento, la expansión.",
    "X________XX": "Hexagrama 43: La Resolución (Guai) - La resolución, la determinación. La decisión, la firmeza.",
    "________XX_": "Hexagrama 44: El Encuentro (Gou) - El encuentro, la reunión. La coincidencia, la unión.",
    "XX________X_": "Hexagrama 45: La Reunión (Cui) - La reunión, la agrupación. La unión, la reconciliación.",
    "X______X_X_": "Hexagrama 46: El Ascenso (Sheng) - El ascenso, el empuje hacia arriba. La promoción, el progreso.",
    "_______X__": "Hexagrama 47: La Opresión (Kun) - La opresión, la agotamiento. La represión, el agobio.",
    "X______X___": "Hexagrama 48: El Pozo (Jing) - El pozo, la fuente. El manantial, la fuente de vida.",
    "_____X_X___": "Hexagrama 49: La Transformación (Ge) - La transformación, la revolución. El cambio, la renovación.",
    "_______XX__": "Hexagrama 50: El Caldero (Ding) - El caldero, el recipiente. La reunión, la nutrición.",
    "XX________X": "Hexagrama 51: El Trueno (Zhen) - El trueno, el despertar. El movimiento, la iniciativa.",
    "______X_X_": "Hexagrama 52: La Quietud (Gen) - La quietud, el estancamiento. La inmovilidad, la pausa.",
    "________X__": "Hexagrama 53: El Desarrollo Gradual (Jian) - El desarrollo gradual. El avance progresivo, el crecimiento.",
    "X__________": "Hexagrama 54: La Esposa Joven (Gui Mei) - La esposa joven. La unión, el matrimonio.",
    "_______XX__": "Hexagrama 55: La Abundancia (Feng) - La abundancia, la plenitud. La prosperidad, la riqueza.",
    "__________XX": "Hexagrama 56: El Viajero (Lu) - El viajero, el caminante. El viaje, la itinerancia.",
    "XX_____X___": "Hexagrama 57: La Penetración (Xun) - La penetración, la confluencia. La asimilación, la influencia.",
    "___X_X_X___": "Hexagrama 58: La Alegría (Dui) - La alegría, el júbilo. La celebración, la diversión.",
    "___X_X_X___X": "Hexagrama 59: La Dispersión (Huan) - La dispersión, la disipación. La separación, el desorden.",
    "X___X_X_X___": "Hexagrama 60: La Limitación (Jie) - La limitación, la restricción. La moderación, el autocontrol.",
    "__________X_": "Hexagrama 61: La Verdad Interior (Zhong Fu) - La verdad interior. La sinceridad, la autenticidad.",
    "____X____X_": "Hexagrama 62: La Preponderancia del Pequeño (Xiao Guo) - La preponderancia del pequeño. La modestia, la humildad.",
    "____X____X__": "Hexagrama 63: Después de la Consumación (Ji Ji) - Después de la consumación. La culminación, el éxito.",
    "___X____X___": "Hexagrama 64: Antes de la Consumación (Wei Ji) - Antes de la consumación. La preparación, la finalización."
}

def lanzar_moneda():
    return random.choice(lineas)

def generar_hexagrama():
    hexagrama = [lanzar_moneda() for _ in range(6)]
    return hexagrama

def interpretar_hexagrama(hexagrama):
    significado_hexagrama = hexagramas.get(''.join(hexagrama), 'Hexagrama desconocido')
    significados_lineas_hexagrama = [significados_lineas[lineas.index(linea)] for linea in hexagrama]
    return significado_hexagrama, significados_lineas_hexagrama

def obtener_significado(linea):
    return f"**Significado:** {hexagramas.get(linea, 'Hexagrama desconocido')}"

def guardar_respuesta(respuesta, ruta):
    with codecs.open(ruta, "a", "utf-8") as archivo:
        archivo.write(respuesta + "\n")

def guardar_imagen(hexagrama, pregunta, ruta):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Dibujar el hexagrama a la izquierda de la imagen
    for i, linea in enumerate(hexagrama):
        color = 'darkgreen' if linea == 'X' else 'black'
        ax.text(0.2, 0.9 - i / 7, f"{linea}", fontsize=16, ha='center', va='center', color=color, weight='bold')

    ax.axis('off')

    significado_hexagrama, significados_lineas_hexagrama = interpretar_hexagrama(hexagrama)

    respuesta = (
        f"**Interpretación del hexagrama:**\n\n"
        f"{significado_hexagrama}\n\n"
    )

    for i, linea in enumerate(hexagrama):
        respuesta += (
            f"**Línea {i + 1}:** {significados_lineas_hexagrama[i]}\n"
            f"{obtener_significado(linea)}\n\n"
        )

    ax.text(0.7, 0.5, respuesta, transform=ax.transAxes, fontsize=12, va='center', ha='left', color='darkblue', weight='bold')

    # Colocar la pregunta en la parte inferior de la imagen, 3 saltos de línea más abajo
    ax.text(0.5, 0.02, f"Pregunta del usuario: {pregunta}", transform=ax.transAxes, fontsize=12, va='center', ha='center', color='darkblue', weight='bold')

    st.pyplot(fig)

def pregunta_usuario():
    pregunta = st.text_input("Haz una pregunta sobre tu pasado, presente o futuro (o escribe 'salir' para salir): ")
    return pregunta

archivo_conversacion = "conversacion.txt"

with codecs.open(archivo_conversacion, "a", "utf-8") as archivo:
    archivo.write("=== Inicio de la Conversación ===\n")

st.title("Consulta del Oráculo I Ching")

while True:
    pregunta = pregunta_usuario()

    if pregunta.lower() == 'salir':
        break

    hexagrama = generar_hexagrama()

    guardar_imagen(hexagrama, pregunta, f"hexagrama_{time.time()}.png")

print("Conversación guardada en 'conversacion.txt'")

