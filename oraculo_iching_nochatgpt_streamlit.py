import streamlit as st
import random
import time
import codecs
import matplotlib.pyplot as plt

lineas = ["_________",
    "X________",
    "________X",
    "_________",
    "X_X_X_X_X_",
    "_________X_",
    "__________X",
    "X________X",
    "___X___X___",
    "X___X___X_",
    "________X_",
    "X_________",
    "___X___X___X___",
    "X___X___X___X_",
    "______X______",
    "______X______X",
    "X_____X_____X_",
    "_______X_______",
    "_________XX",
    "XX_________",
    "_________XXX",
    "XXXXXXXXX",
    "__________X",
    "X__X__X__X_",
    "X__________X",
    "_______XX_______",
    "_________X___",
    "_______X___X___",
    "__________X___",
    "X___X___X___X___X",
    "X_________X_",
    "_______X___X___X",
    "__________XX",
    "XX__________",
    "_________X_",
    "________X__",
    "_______XX_",
    "X_____X_____X",
    "_______X__",
    "X______X___",
    "_____X_X___",
    "_______XX__",
    "XX________X",
    "______X_X_",
    "________X__",
    "X__________",
    "_______XX__",
    "__________XX",
    "XX_____X___",
    "___X_X_X___",
    "___X_X_X___X",
    "X___X_X_X___",
    "__________X_",
    "____X____X_",
    "____X____X__",
    "___X____X___",
    "__________X_",
    "____X_X_X____",
    "_______XX____",
    "XX_________X",
    "X________XX",
    "_________X_",
    "________X__",
    "_______XX_",
    "XX_________",
    "_________X_X",
    "X__________X",
    "_____X_X___",
    "_________XX",
    "XX________X",
    "______X_X_",
    "________X__",
    "X__________",
    "_____X_X___",
    "_________XX",
    "XX_____X___",
    "X_____X_X_X",
    "___X_X_X_X___X",
    "__________X_",
    "____X____X_",
    "____X____X__",
    "___X____X___",
    "__________X_",
    "____X____X_",
    "____X____X__",
    "___X____X___",
    "__________X_",
    "____X____X__",
    "____X____X___",
    "___X____X___"]
significados_lineas = [
    "Hexagram 1: The Creative (Qian) - The creative, the strong. The creative power of the cosmos.",
    "Hexagram 2: The Receptive (Kun) - The earth, the receptive. Receptivity, devotion.",
    "Hexagram 3: Difficulty at the Beginning (Zhun) - Beginning of difficulty. The start of something new.",
    "Hexagram 4: Youthful Folly (Meng) - Youthful folly. Inexperience.",
    "Hexagram 64: Before Completion (Wei Ji) - Before completion. The process of reaching conclusion.",
    "Hexagram 5: Waiting (Xu) - Waiting patiently. Waiting.",
    "Hexagram 6: Conflict (Song) - Conflict, dispute. Confrontation and struggle.",
    "Hexagram 7: The Army (Shi) - United and organized. The army, congregation.",
    "Hexagram 50: The Cauldron (Ding) - The receptacle. Gathering, nourishment.",
    "Hexagram 51: The Arousing (Zhen) - Active thunder. Movement and initiative.",
    "Hexagram 8: Holding Together (Bi) - Holding together, union. Unity, pooling of resources.",
    "Hexagram 9: The Taming Power of the Small (Xiao Chu) - Small in motion. Inner strength in action.",
    "Hexagram 54: The Marrying Maiden (Gui Mei) - The marrying maiden. Marriage, union.",
    "Hexagram 55: Abundance (Feng) - Abundance and fullness. Abundance, prosperity.",
    "Hexagram 16: Enthusiasm (Yu) - Enthusiasm. Joy, passion.",
    "Hexagram 17: Following (Sui) - Following, adaptation. Perseverance and continuity.",
    "Hexagram 19: Approach (Lin) - Approach, nearing. Approach, approximation.",
    "Hexagram 20: Contemplation (Guan) - Observation. Contemplation, attention.",
    "Hexagram 62: Preponderance of the Small (Xiao Guo) - Preponderance of the small. Moderation, humility.",
    "Hexagram 63: After Completion (Ji Ji) - After completion. Conclusion and culmination.",
    "Hexagram 53: Development Gradual (Jian) - Evolutionary development. Gradual progress, step-by-step advance.",
    "Hexagram 32: Duration (Heng) - Duration, persistence. Persistence, continuity.",
    "Hexagram 10: Treading (Lu) - Treading, conducting. Advance, progressive action.",
    "Hexagram 56: The Wanderer (Lu) - The wanderer, the traveler. Journey, roaming.",
    "Hexagram 11: Peace (Tai) - Peace. Peace, tranquility.",
    "Hexagram 31: Influence (Xian) - Influence, attraction. Attraction, magnetic influence.",
    "Hexagram 12: Standstill (Pi) - Standstill. Obstruction, blockage.",
    "Hexagram 33: Retreat (Dun) - Retreat, strategic withdrawal. Retreat, distancing.",
    "Hexagram 13: Fellowship with Men (Tong Ren) - Human fellowship. Union, fraternity.",
    "Hexagram 30: Fire (Li) - Brightening fire. Luminosity, brilliance.",
    "Hexagram 14: Possession in Great Measure (Da You) - Great possession. Wealth, abundance.",
    "Hexagram 34: The Power of the Great (Da Zhuang) - The great force. Great power, outstanding strength.",
    "Hexagram 29: The Abysmal (Kan) - The abysmal, the abyss. The fall, submission.",
    "Hexagram 28: Preponderance of the Great (Da Guo) - Preponderance of the great. Greatness, supreme power.",
    "Hexagram 15: Modesty (Qian) - Modesty, humility. Moderation, sobriety.",
    "Hexagram 16: Enthusiasm (Yu) - Enthusiasm, joy. Joy, passion.",
    "Hexagram 17: Following (Sui) - Synchronization, following. Coordination, synchronization.",
    "Hexagram 18: Repairing (Gu) - Repairing, renovation. Correction, renewal.",
    "Hexagram 19: Approach (Lin) - Approach, approximation. Nearness, communication.",
    "Hexagram 20: Contemplation (Guan) - Contemplation, observation. Attention, reflection.",
    "Hexagram 21: Biting Through (Shi He) - Biting through, the gnawing bite. Adherence, stripping away.",
    "Hexagram 22: Grace (Bi) - Grace, adornment. Elegance, embellishment.",
    "Hexagram 23: Splitting Apart (Bo) - Splitting apart, the disintegration. Decomposition, dissolution.",
    "Hexagram 24: Return (Fu) - Return, the turning point. Return, recovery.",
    "Hexagram 25: Innocence (Wu Wang) - Innocence, the unexpected. Surprise, the unusual.",
    "Hexagram 26: Taming Power of the Great (Da Xu) - Taming power. Restraint, control.",
    "Hexagram 27: Nourishment (Yi) - Nourishment, the caring. Sustenance, provision.",
    "Hexagram 28: Great Preponderance (Da Guo) - Great preponderance. Great prosperity, supreme power.",
    "Hexagram 29: The Abysmal (Kan) - The abyss, the fall. Danger, warning.",
    "Hexagram 30: The Clinging (Li) - The clinging, the brightness. Luminosity, insight.",
    "Hexagram 31: Influence (Xian) - Influence, attraction. Persuasion, charm.",
    "Hexagram 32: Duration (Heng) - Duration, persistence. Patience, constancy.",
    "Hexagram 33: Retreat (Dun) - Retreat, strategic withdrawal. Distance, tactical withdrawal.",
    "Hexagram 34: The Power of the Great (Da Zhuang) - The power of the great. Power, magnetic influence.",
    "Hexagram 35: Progress (Jin) - Progress, advance. Advance, progress.",
    "Hexagram 36: Darkening of the Light (Ming Yi) - Darkening of the light. Darkness, veiling.",
    "Hexagram 37: The Family (Jia Ren) - The family, the home. Family ties, unity.",
    "Hexagram 38: Opposition (Kui) - Opposition, conflict. Contradiction, clash.",
    "Hexagram 39: Obstruction (Jian) - Obstruction, obstacle. Challenge, overcoming.",
    "Hexagram 40: Deliverance (Jie) - Deliverance, partial deliverance. Solution, resolution.",
    "Hexagram 41: Decrease (Sun) - Decrease, loss. Diminution, reduction.",
    "Hexagram 42: Increase (Yi) - Increase, expansion. Growth, expansion.",
    "Hexagram 43: Breakthrough (Guai) - Breakthrough, determination. Decision, firmness.",
    "Hexagram 44: Coming to Meet (Gou) - Coming to meet, the meeting. Coincidence, union.",
    "Hexagram 45: Gathering Together (Cui) - Gathering together, grouping. Union, reconciliation.",
    "Hexagram 46: Pushing Upward (Sheng) - Pushing upward, the upward thrust. Promotion, progress.",
    "Hexagram 47: Oppression (Kun) - Oppression, exhaustion. Repression, burden.",
    "Hexagram 48: The Well (Jing) - The well, the source. The spring, the source of life.",
    "Hexagram 49: Revolution (Ge) - Revolution, transformation. Change, renewal.",
    "Hexagram 50: The Cauldron (Ding) - The cauldron, the receptacle. Gathering, nourishment.",
    "Hexagram 51: The Arousing (Zhen) - The arousing, the awakening. Movement, initiative.",
    "Hexagram 52: Keeping Still (Gen) - Keeping still, the standstill. Immobility, pause.",
    "Hexagram 53: Development Gradual (Jian) - Gradual development. Progressive advance, growth.",
    "Hexagram 54: The Marrying Maiden (Gui Mei) - The marrying maiden. Union, marriage.",
    "Hexagram 55: Abundance (Feng) - Abundance, fullness. Prosperity, wealth.",
    "Hexagram 56: The Wanderer (Lu) - The wanderer, the traveler. Journey, wandering.",
    "Hexagram 57: The Gentle (Xun) - The gentle, the penetration. Assimilation, influence.",
    "Hexagram 58: The Joyous (Dui) - The joyous, the jubilant. Celebration, amusement.",
    "Hexagram 59: Dispersion (Huan) - Dispersion, dissipation. Separation, disorder.",
    "Hexagram 60: Limitation (Jie) - Limitation, restraint. Moderation, self-control.",
    "Hexagram 61: Inner Truth (Zhong Fu) - Inner truth. Sincerity, authenticity.",
    "Hexagram 62: Preponderance of the Small (Xiao Guo) - Preponderance of the small. Modesty, humility.",
    "Hexagram 63: After Completion (Ji Ji) - After completion. Culmination, success.",
    "Hexagram 64: Before Completion (Wei Ji) - Before completion. Preparation, completion."
]

hexagramas = {
    "_________": "Embrace change with creativity. Be strong and adaptable, harness the creative power of the universe.",
    "X________": "Stay grounded and be receptive. Cultivate patience and devotion in all endeavors.",
    "________X": "Face new beginnings with resilience. Challenges at the start are opportunities for growth.",
    "_________X": "Approach youth with wisdom. Learn from experiences and navigate the journey with caution.",
    "X_X_X_X_X_": "Embrace the process before completion. Recognize the value in every step leading to a conclusion.",
    "_________X_": "Practice patience in waiting. Trust in the process and maintain calm anticipation.",
    "__________X": "Navigate conflicts with grace. Confrontation can lead to growth and resolution.",
    "X________X": "Unite and organize your efforts. Strength lies in unity and coordinated action.",
    "___X___X___": "Gather and nurture your resources. Create a supportive environment for growth and nourishment.",
    "X___X___X_": "Be proactive and seize opportunities. Take initiative and embrace movement and change.",
    "________X_": "Strive for solidarity and coherence. Unity is a powerful force that overcomes challenges.",
    "X_________": "Find strength in modesty and humility. Small, consistent efforts can lead to significant impact.",
    "___X___X___X___": "Approach relationships with youthful energy. Nurture connections and cultivate unity.",
    "X___X___X___X_": "Embrace abundance with gratitude. Recognize and appreciate the richness in your life.",
    "______X______": "Exercise caution and foresight. Pay attention to details and be prepared for potential challenges.",
    "______X______X": "Persevere and maintain continuity. Stay committed to your goals and objectives.",
    "X_____X_____X_": "Approach situations with appropriateness. Seek harmony and make the right connections.",
    "_______X_______": "Observe and contemplate. Gain insights through careful observation and reflection.",
    "_________XX": "Embrace humility and modesty. Find strength in moderation and remain humble.",
    "XX_________": "Reflect on your achievements after completion. Celebrate success and learn from the experience.",
    "_________XXX": "Embrace gradual development. Progress step by step, and be patient with the journey.",
    "XXXXXXXXX": "Endure with persistence. Persevere through challenges and maintain continuity.",
    "__________X": "March forward with determination. Take progressive actions and move towards your goals.",
    "X__X__X__X_": "Embrace the journey as a traveler. Be open to new experiences and discoveries.",
    "X__________X": "Cultivate peace within. Find tranquility and balance amidst life's challenges.",
    "_______XX_______": "Influence others positively. Radiate charisma and be a source of inspiration.",
    "_________X___": "Overcome stagnation with innovation. Break through obstacles and find creative solutions.",
    "_______X___X___": "Strategically withdraw when necessary. Know when to step back and reassess.",
    "__________X___": "Foster community and brotherhood. Build connections and collaborate with others.",
    "X___X___X___X___X": "Shine brightly like fire. Let your inner light illuminate your path and inspire others.",
    "X_________X_": "Embrace abundance and prosperity. Cultivate wealth and share your blessings.",
    "_______X___X___X": "Harness great strength. Tap into your power and influence others positively.",
    "__________XX": "Rise after a fall. Learn from setbacks and emerge stronger.",
    "XX__________": "Embrace greatness and power. Strive for excellence and influence others positively.",
    "_________X_": "Practice moderation and humility. Find balance and remain grounded in all endeavors.",
    "________X__": "Approach life with enthusiasm and joy. Find joy in every experience and share it.",
    "_______XX_": "Coordinate and synchronize. Find harmony in the rhythm of life.",
    "X_____X_____X": "Embrace change and renewal. Seek correction and improvement.",
    "_______X__": "Approach with proximity and connection. Build relationships and communicate openly.",
    "X___X___X__": "Contemplate and reflect. Cultivate mindfulness and awareness in your actions.",
    "_____X____": "Deal with challenges assertively. Face difficulties with resilience and determination.",
    "____X_____": "Embrace grace and elegance. Enhance your surroundings with beauty.",
    "____X______": "Accept dissolution with grace. Embrace change and transformation.",
    "X______X__": "Embrace return and recovery. Find renewal and healing in setbacks.",
    "_________XX_": "Embrace innocence and the unexpected. Find joy in life's surprises.",
    "XX_________": "Control with restraint. Practice discipline and self-control.",
    "_______XX__": "Provide sustenance and support. Nurture and care for those around you.",
    "________XX": "Embrace great prosperity. Strive for success and wield power wisely.",
    "X________X_": "Face danger with caution. Be vigilant and heed warnings.",
    "_______X_X_": "Illuminate with clarity. Seek understanding and clarity in all situations.",
    "X______X___": "Persuade with influence. Influence others positively through persuasion.",
    "_________X_X": "Practice patience and persistence. Endure challenges with fortitude.",
    "X__________X": "Strategically withdraw when necessary. Choose your battles and preserve energy.",
    "_____X_X___": "Wield power and influence. Attract and lead with magnetic charisma.",
    "_________XX": "Progress steadily. Advance with purpose and celebrate incremental achievements.",
    "XX_________": "Navigate through darkness. Find clarity and insight amidst challenges.",
    "________X_X": "Cherish family bonds. Cultivate strong connections and unity within the family.",
    "X________X__": "Navigate conflicts with diplomacy. Seek resolution and understanding in disagreements.",
    "______X_X__": "Overcome difficulties with resilience. Face challenges head-on and persevere.",
    "_______XX_X": "Embrace liberation and resolution. Find solutions and free yourself from constraints.",
    "X_________XX": "Accept diminishing returns with grace. Learn and grow through losses.",
    "XX_________X": "Embrace growth and expansion. Strive for progress and abundance.",
    "X________XX": "Make decisions with determination. Resolve to achieve your goals.",
    "________XX_": "Embrace chance encounters. Find meaning in serendipity and connections.",
    "XX________X_": "Reconcile and reunite. Mend relationships and promote harmony.",
    "X______X_X_": "Rise and progress. Seize opportunities for growth and advancement.",
    "_______X__": "Face oppression with resilience. Overcome challenges with strength.",
    "X______X___": "Tap into inner resources. Find sustenance and strength within yourself.",
    "_____X_X___": "Embrace transformation and renewal. Adapt to change and evolve.",
    "_______XX__": "Gather and nurture your resources. Create a supportive environment for growth and nourishment.",
    "XX________X": "Embrace awakening and initiative. Seize opportunities with boldness and determination.",
    "______X_X_": "Embrace stillness and reflection. Find peace in moments of quiet and contemplation.",
    "________X__": "Embrace gradual development. Progress step by step, and be patient with the journey.",
    "X__________": "Approach relationships with youthful energy. Nurture connections and cultivate unity.",
    "_______XX__": "Embrace abundance with gratitude. Recognize and appreciate the richness in your life.",
    "__________XX": "Embrace the journey as a traveler. Be open to new experiences and discoveries.",
    "XX_____X___": "Penetrate obstacles with adaptability. Flow with life's challenges and assimilate lessons.",
    "___X_X_X___": "Cultivate joy and celebration. Find delight and positivity in every experience.",
    "___X_X_X___X": "Navigate through dispersion with focus. Stay centered amidst chaos and confusion.",
    "X___X_X_X___": "Embrace limitation with self-control. Practice moderation and discipline.",
    "__________X_": "Seek inner truth and authenticity. Be sincere and true to yourself.",
    "____X____X_": "Embrace humility and modesty. Find strength in moderation and remain humble.",
    "____X____X__": "Reflect on your achievements after completion. Celebrate success and learn from the experience.",
    "___X____X___": "Prepare for completion with patience. Approach endings with mindfulness and readiness."
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
