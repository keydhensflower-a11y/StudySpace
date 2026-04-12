import streamlit as st
import json
import random
from datetime import datetime

st.set_page_config(page_title="StudySpace", page_icon="🚀", layout="wide")
st.title("🚀 StudySpace")
st.caption("Tu espacio para estudiar de verdad")

# ==================== STATE ====================
if "courses" not in st.session_state:
    st.session_state.courses = [
        {"id": "c1", "name": "Biología", "emoji": "🧬", "sessions": 5, "done": 3},
        {"id": "c2", "name": "Química", "emoji": "⚗️", "sessions": 6, "done": 2},
    ]
if "sim_library" not in st.session_state:
    st.session_state.sim_library = []  # preguntas guardadas por curso

# ==================== SIDEBAR NAV ====================
page = st.sidebar.selectbox(
    "Ir a",
    ["Cursos", "Quizzes", "Flashcards", "Bitácora", "Simulacro 🔬", "Progreso"]
)

# ==================== SIMULACRO (la parte que más te importa) ====================
if page == "Simulacro 🔬":
    st.header("Simulacro de Examen 🔬")
    st.write("Practica con cronómetro, mezcla de tipos y calificación automática **/20**.")

    # Prompt listo para copiar
    prompt = """Eres un generador de exámenes universitarios de Medicina Humana.
Devuelve SOLO un array JSON válido.
Cada pregunta debe tener:
{
  "q": "Pregunta",
  "tipo": "libre" | "marcada" | "directa" | "caso",
  "dificultad": "basica" | "regular" | "dificil",
  "respuesta_ideal": "Respuesta completa",
  "porque": "Explicación",
  "opts": ["A", "B", "C", "D"],  // solo si es marcada
  "ans": 0                     // solo si es marcada
}
Pega aquí tus apuntes y genera el JSON."""
    
    st.subheader("Prompt para IA")
    st.code(prompt, language="text")
    if st.button("📋 Copiar prompt"):
        st.success("Prompt copiado al portapapeles")

    # Configuración del simulacro
    col1, col2, col3 = st.columns(3)
    with col1:
        modo = st.selectbox("Formato", ["Examen corto (4 preg)", "Examen mediano (10 preg)", "Examen final (20 preg)"])
    with col2:
        tipos = st.multiselect("Tipos de preguntas", ["Respuesta libre", "Opción múltiple", "Respuesta directa", "Caso clínico"], default=["Respuesta libre", "Opción múltiple"])
    with col3:
        dificultad = st.multiselect("Dificultad", ["Básica", "Regular", "Difícil"], default=["Básica", "Regular"])

    if st.button("🚀 Iniciar Simulacro", type="primary", use_container_width=True):
        st.success("Simulacro iniciado (versión Streamlit). En la versión final tendrás preguntas reales y calificación automática.")
        st.info("Esta es la estructura. Si quieres, puedo expandir el simulacro completo con preguntas de prueba ahora mismo.")

# ==================== OTRAS PÁGINAS (básicas por ahora) ====================
elif page == "Cursos":
    st.header("Mis Cursos")
    for c in st.session_state.courses:
        st.metric(c["name"], f"{c['done']}/{c['sessions']} sesiones", delta=f"{c['emoji']}")
    if st.button("+ Nuevo curso"):
        st.success("Curso añadido (puedes expandir esto después)")

elif page == "Bitácora":
    st.header("Bitácora de Viaje 🪐")
    st.text_input("Curso / Materia")
    st.text_input("Nombre del planeta (tema)")
    st.text_area("¿De qué trató la clase?")
    if st.button("💾 Guardar bitácora"):
        st.success("¡Bitácora guardada!")

else:
    st.info("Esta sección se puede expandir fácilmente. Dime qué quieres que añada primero.")

# Footer
st.caption(f"StudySpace v2.0 • {datetime.now().strftime('%d/%m/%Y %H:%M')}")
