import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Mindfulness en América Latina", page_icon="🧘", layout="wide")
st.title("🧘 Mindfulness en América Latina: Eficacia en Ansiedad y Cognición")
st.caption("DOI: 10.7910/DVN/AHUZZ0 | Harvard Dataverse | CC0 1.0 | 2015–2024")

page = st.sidebar.selectbox("Sección", [
    "Inicio","Estudios Clínicos","Prevalencia Ansiedad","Efectos Cognitivos",
    "Acceso Salud Mental","MBSR","MBCT","Países","Brecha Tratamiento",
    "Tamaño de Efecto","Publicaciones","Comparativas","Tendencias","Poblaciones","Barreras"
])

if page == "Inicio":
    c1,c2,c3 = st.columns(3)
    c1.metric("Efecto MBI en ansiedad","d = -1.26")
    c2.metric("Prevalencia ansiedad LATAM","7.3%")
    c3.metric("Brecha de tratamiento","73.9%")
    c4,c5,c6 = st.columns(3)
    c4.metric("Participantes prog. ALMA 2023","226")
    c5.metric("Meta-análisis enfermería Brasil","818")
    c6.metric("Prevalencia global (referencia)","4.7%")
    st.info("Base de datos sobre la eficacia de intervenciones basadas en mindfulness (MBI, MBSR, MBCT) en América Latina. Incluye estudios clínicos, prevalencia de ansiedad, acceso a salud mental y efectos cognitivos. Fuentes: PubMed/PMC, SciELO, BVS, JAMA, Cochrane, UNDP, OPS/OMS.")
    paises = ["Brasil","Uruguay","Argentina","Chile","México","Colombia","Perú","Ecuador","Venezuela"]
    prevalencia = [9.3,8.4,7.9,7.6,7.4,7.1,6.9,6.5,5.8]
    colors = ["#ff6b6b","#ff9f43","#ffd32a","#0be881","#48dbfb","#58a6ff","#a55eea","#1dd1a1","#ff4757"]
    fig = go.Figure(go.Bar(x=paises, y=prevalencia, marker_color=colors, name="Prevalencia %"))
    fig.add_hline(y=4.7, line_dash="dot", line_color="#ff6b6b", annotation_text="Media global 4.7%")
    fig.update_layout(template="plotly_dark",height=420,title="Prevalencia de Trastornos de Ansiedad en América Latina (OPS/OMS 2021)",yaxis_title="Prevalencia (%)")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Estudios Clínicos":
    st.subheader("🔬 Estudios Clínicos MBI en América Latina")
    df = pd.DataFrame({
        "Estudio":["Programa ALMA (México)","Venezuela MBI","Brasil Enfermería (meta-análisis)","Chile MBSR","Argentina MBCT","Colombia MBI","Perú MBI"],
        "n":[226,153,818,45,62,38,29],
        "Reducción Ansiedad (%)":[-42,-38,-35,-31,-44,-29,-27],
        "d Cohen":[-1.26,-1.05,-0.87,-0.72,-1.31,-0.65,-0.58],
        "País":["México","Venezuela","Brasil","Chile","Argentina","Colombia","Perú"]
    })
    st.dataframe(df,use_container_width=True)
    fig = go.Figure(go.Bar(x=df["Estudio"],y=df["Reducción Ansiedad (%)"],marker_color="#0be881"))
    fig.update_layout(template="plotly_dark",height=400,title="Reducción de ansiedad por estudio (%)",yaxis_title="Reducción (%)")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Prevalencia Ansiedad":
    st.subheader("😟 Prevalencia de Ansiedad en América Latina (OPS/OMS 2021)")
    paises = ["Brasil","Uruguay","Argentina","Chile","México","Colombia","Perú","Ecuador","Venezuela"]
    prevalencia = [9.3,8.4,7.9,7.6,7.4,7.1,6.9,6.5,5.8]
    fig = go.Figure(go.Bar(x=paises, y=prevalencia, marker_color=["#ff6b6b","#ff9f43","#ffd32a","#0be881","#48dbfb","#58a6ff","#a55eea","#1dd1a1","#ff4757"]))
    fig.add_hline(y=4.7, line_dash="dot", line_color="#ff6b6b", annotation_text="Media global 4.7%")
    fig.update_layout(template="plotly_dark",height=420,title="Prevalencia de Trastornos de Ansiedad (%)",yaxis_title="%")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Efectos Cognitivos":
    st.subheader("🧠 Efectos Cognitivos de las Intervenciones MBI")
    dominios = ["Ansiedad","Depresión","Rumiación","Atención","Mem. Trabajo","Flexib. Cogn.","Regulac. Emoc."]
    d_cohen = [-1.26,-0.87,-0.56,0.37,0.35,0.31,0.44]
    colors = ["#0be881" if v < 0 else "#58a6ff" for v in d_cohen]
    fig = go.Figure(go.Bar(x=dominios, y=d_cohen, marker_color=colors))
    fig.add_hline(y=0, line_color="white", line_width=1)
    fig.update_layout(template="plotly_dark",height=420,title="Tamaños de Efecto (d de Cohen) de MBI (negativo = reducción)",yaxis_title="d de Cohen")
    st.plotly_chart(fig,use_container_width=True)
    st.info("Efectos negativos = reducción de síntomas (ansiedad, depresión, rumiación). Efectos positivos = mejora de capacidades cognitivas.")

elif page == "Acceso Salud Mental":
    st.subheader("🏥 Acceso a Salud Mental en América Latina")
    paises = ["Brasil","Argentina","Chile","México","Colombia","Perú","Ecuador","Venezuela","Bolivia"]
    psiq_100k = [3.2,12.1,5.8,1.6,1.5,1.1,0.9,0.8,0.4]
    cobertura = [35,72,45,18,15,12,10,8,5]
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Psiquiatras/100k",x=paises,y=psiq_100k,marker_color="#58a6ff"))
    fig.add_trace(go.Bar(name="Cobertura salud mental (%)",x=paises,y=cobertura,marker_color="#3fb950"))
    fig.update_layout(template="plotly_dark",barmode="group",height=420,title="Recursos de Salud Mental en LATAM")
    st.plotly_chart(fig,use_container_width=True)

elif page == "MBSR":
    st.subheader("🌿 Mindfulness-Based Stress Reduction (MBSR)")
    st.info("El MBSR es un programa de 8 semanas desarrollado por Jon Kabat-Zinn (1979). En LATAM muestra reducciones medias del 35-42% en síntomas de ansiedad.")
    anios = list(range(2015,2025))
    estudios = [2,3,4,5,6,8,10,12,15,18]
    fig = go.Figure(go.Scatter(x=anios,y=estudios,mode="lines+markers",line=dict(color="#0be881",width=3),marker=dict(size=8)))
    fig.update_layout(template="plotly_dark",height=380,title="Publicaciones MBSR en América Latina (2015-2024)",yaxis_title="Número de estudios")
    st.plotly_chart(fig,use_container_width=True)

elif page == "MBCT":
    st.subheader("💆 Mindfulness-Based Cognitive Therapy (MBCT)")
    st.info("El MBCT combina el mindfulness con la terapia cognitiva. Especialmente eficaz para la prevención de recaídas en depresión mayor (d = -1.31 en LATAM).")
    indicadores = ["Reducción ansiedad (%)","Reducción depresión (%)","Prevención recaída (%)","Adherencia (%)"]
    mbct = [44,52,67,78]
    mbsr = [38,42,45,72]
    fig = go.Figure()
    fig.add_trace(go.Bar(name="MBCT",x=indicadores,y=mbct,marker_color="#58a6ff"))
    fig.add_trace(go.Bar(name="MBSR",x=indicadores,y=mbsr,marker_color="#0be881"))
    fig.update_layout(template="plotly_dark",barmode="group",height=420,title="Comparación MBCT vs MBSR en resultados clave (%)")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Países":
    st.subheader("🌎 Distribución de Estudios MBI por País")
    fig = go.Figure(go.Pie(
        labels=["Brasil","México","Argentina","Colombia","Chile","Venezuela","Otros"],
        values=[35,22,18,12,8,3,2], hole=0.4,
        marker=dict(colors=["#ff6b6b","#0be881","#58a6ff","#ffd32a","#48dbfb","#a55eea","#ff9f43"])
    ))
    fig.update_layout(template="plotly_dark",height=440,title="Distribución de Estudios MBI en América Latina (%)")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Brecha Tratamiento":
    st.subheader("⚡ Brecha de Tratamiento en Salud Mental")
    st.metric("Brecha de tratamiento promedio LATAM","73.9%")
    paises = ["Perú","México","Colombia","Venezuela","Ecuador","Brasil","Chile","Argentina","Uruguay"]
    brecha = [88,82,79,81,84,65,55,45,38]
    fig = go.Figure(go.Bar(x=paises,y=brecha,marker_color=["#ff7b72" if b > 70 else "#ffa657" if b > 50 else "#3fb950" for b in brecha]))
    fig.update_layout(template="plotly_dark",height=420,title="Brecha de Tratamiento en Salud Mental por País (%)",yaxis_title="% sin acceso a tratamiento")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Tamaño de Efecto":
    st.subheader("📐 Tamaños de Efecto d de Cohen")
    df = pd.DataFrame({
        "Intervención":["MBI (ansiedad)","MBI (depresión)","MBSR (estrés)","MBCT (recaída dep.)","MBI (rumiación)","MBI (atención)","MBI (mem. trabajo)"],
        "d Cohen":[-1.26,-0.87,-0.95,-1.31,-0.56,0.37,0.35],
        "Interpretación":["Muy grande","Grande","Grande","Muy grande","Mediano","Pequeño","Pequeño"]
    })
    st.dataframe(df,use_container_width=True)
    fig = go.Figure(go.Bar(x=df["Intervención"],y=df["d Cohen"],marker_color=["#0be881" if d < 0 else "#58a6ff" for d in df["d Cohen"]]))
    fig.update_layout(template="plotly_dark",height=420,title="Tamaños de Efecto de Intervenciones Mindfulness")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Publicaciones":
    st.subheader("📚 Publicaciones MBI en América Latina 2015-2024")
    anios = list(range(2015,2025))
    pubs = [8,11,14,18,22,28,35,42,51,63]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=anios,y=pubs,marker_color="#58a6ff",name="Publicaciones por año"))
    fig.add_trace(go.Scatter(x=anios,y=pubs,mode="lines+markers",line=dict(color="#ffa657",width=2),name="Tendencia"))
    fig.update_layout(template="plotly_dark",height=420,title="Publicaciones sobre MBI en América Latina",yaxis_title="Número de publicaciones")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Comparativas":
    st.subheader("⚖️ Comparativa de Intervenciones")
    intervenciones = ["MBI","MBSR","MBCT","TCC","Farmacoterapia","Lista espera"]
    efecto_ansiedad = [-1.26,-0.95,-1.31,-1.12,-0.89,0.05]
    efecto_depresion = [-0.87,-0.82,-1.18,-1.05,-0.95,0.02]
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Ansiedad",x=intervenciones,y=efecto_ansiedad,marker_color="#58a6ff"))
    fig.add_trace(go.Bar(name="Depresión",x=intervenciones,y=efecto_depresion,marker_color="#ff7b72"))
    fig.update_layout(template="plotly_dark",barmode="group",height=420,title="Comparativa de efectividad de intervenciones (d de Cohen)")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Tendencias":
    st.subheader("📈 Tendencias 2015-2024")
    anios = list(range(2015,2025))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=anios,y=[2,3,4,5,6,8,10,12,15,18],name="Ensayos clínicos",line=dict(color="#58a6ff",width=3)))
    fig.add_trace(go.Scatter(x=anios,y=[8,11,14,18,22,28,35,42,51,63],name="Publicaciones totales",line=dict(color="#3fb950",width=3),yaxis="y2"))
    fig.update_layout(template="plotly_dark",height=420,title="Crecimiento de la investigación MBI en LATAM",yaxis=dict(title="Ensayos clínicos"),yaxis2=dict(title="Publicaciones totales",overlaying="y",side="right"))
    st.plotly_chart(fig,use_container_width=True)

elif page == "Poblaciones":
    st.subheader("👥 Poblaciones Objetivo en Estudios MBI")
    pops = ["Adultos generales","Personal sanitario","Universitarios","Pacientes oncológicos","Adultos mayores","Adolescentes","Madres postparto"]
    counts = [42,18,15,10,8,5,2]
    fig = go.Figure(go.Bar(x=pops,y=counts,marker_color=["#58a6ff","#3fb950","#ffa657","#ff7b72","#d2a8ff","#ffd700","#1dd1a1"]))
    fig.update_layout(template="plotly_dark",height=420,title="Distribución de estudios por población objetivo",yaxis_title="Número de estudios")
    st.plotly_chart(fig,use_container_width=True)

elif page == "Barreras":
    st.subheader("🚧 Barreras para el Acceso a Intervenciones MBI")
    barreras = ["Costo económico","Falta de instructores","Estigma salud mental","Desconocimiento","Tiempo limitado","Acceso rural","Idioma/culturales"]
    porcentaje = [68,55,48,62,45,72,38]
    fig = go.Figure(go.Bar(x=barreras,y=porcentaje,marker_color="#ffa657"))
    fig.update_layout(template="plotly_dark",height=420,title="Principales barreras para el acceso a MBI en LATAM (%)",yaxis_title="% de estudios que reportan la barrera")
    st.plotly_chart(fig,use_container_width=True)

st.divider()
st.markdown("**Citación:** de la Serna, J.M. (2026). *Intervenciones Basadas en Mindfulness: Eficacia en la Reducción de Ansiedad y Mejora del Rendimiento Cognitivo en América Latina*. Harvard Dataverse. https://doi.org/10.7910/DVN/AHUZZ0")
