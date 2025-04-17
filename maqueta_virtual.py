import streamlit as st  
import numpy as np  
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import plotly.graph_objects as go

#configuracion del entorno

st.set_page_config( page_title="MAQUETA VIRTUAL", layout="centered" )
st.title("📈Dinámica Usuarios en sistema Web")
st.markdown("Simulador del comprotamiento de usuarios en un sistema web basado en ecuaciones diferenciales")

#sidebar -Párametros
st.sidebar.title("⚙️ Parámetros del Modelo")
st.sidebar.markdown("-----")
with st.sidebar.expander("📎Parámetros de entrada"):
    lambd= st.slider("Tasa de llegada de usuarios(ʎ)",0.0,100.0,10.0, help="Número de usuarios que llegan por segundo")
    mu= st.slider("Tasa de proceso de usuarios (ų)",0.1,20.0,1.0)
    alpha= st.slider("Tasa de Abandono de usuarios(ɑ)",0.0,10.0,0.5)
    theta= st.slider("Tasa de finalización de usuarios(ɸ)",0.1,10.0,1.0)
    max_users= st.number_input("🔏Máximo de usuarios simultaneamente", min_value=1, max_value=1000,value=200)
    
with st.sidebar.expander("Condiciones Iniciales"):
    U0= st.number_input("🟢Usuarios Activos inicales",0,1000,100)
    P0= st.number_input("🔵Usuarios Procesados inicales",0,1000,0)
    A0= st.number_input("🔴Usuarios Abandonados inicales",0,1000,0)
with st.sidebar.expander("⏱️Tiempo de la Simulación"):
    tiempo= st.slider("Tiempo Total de la Simulación",10,500,100)
    
    
#Modelo Matemático

def sistema(y,t ,lambd,mu,alpha,theta,max_users):
    
    U,P,A =y
    llegada_efectiva= lambd if U < max_users else 0
    dUdt = llegada_efectiva - mu * U - alpha * U
    dPdt = mu * U - theta *P
    dAdt = alpha * U
    return [dUdt, dPdt, dAdt]

#simulación
y0= [U0,P0,A0]
t= np.linspace(0,tiempo,500)
resultado= odeint(sistema,y0,t,args=(lambd,mu,alpha,theta,max_users))

 #tiempo de respuesta estimado
tiempo_estimado_respuesta= resultado[:,0] /mu

#Gráfica dinámica con plotly

fig_plotly= go.Figure()
fig_plotly.add_trace(go.Scatter(x=t, y=resultado[:,0],mode='lines',name='Usuarios Activos', line=dict(color='royalblue')))
fig_plotly.add_trace(go.Scatter(x=t, y= resultado[:,1],mode='lines',name='Usuarios Procesados',line=dict(color='green')))
fig_plotly.add_trace(go.Scatter(x=t, y= resultado[:,2],mode='lines',name='Usuarios Finalizados',line=dict(color='red')))
fig_plotly.add_trace(go.Scatter(x=t, y=[max_users]*len(t),mode='lines',name='Máximo de usuarios Simultaneos',line=dict(color='orange',dash='dash')))
fig_plotly.update_layout(
    title="Evolución de Usuarios",
     xaxis_title="Tiempo(s)",
     yaxis_title="Cantidad de Usuarios",
     template="plotly_white"
)
st.plotly_chart(fig_plotly)

#Gráfica estatica 

fig_static, ax= plt.subplots(figsize=(10,5))
ax.plot(t,resultado[:,0],color='blue')
ax.plot(t,resultado[:,1],color='green')
ax.plot(t,resultado[:,2],color='red')
ax.axhline(max_users,color='orange', linestyle= '--', label='Máximo de usuarios Simultaneos')
ax.legend()
ax.grid(True)
st.pyplot(fig_static)

#Metricas Finales

st.subheader("📊Métricas finales")
st.metric("🟢 Usuarios Activos Finales", f"{resultado[-1,0]:.2f}")
st.metric("🔵 Usuarios Procesados Finales", f"{resultado[-1,1]:.2f}")
st.metric("🔴 Usuarios Avandonados Finales",f"{resultado[-1,2]:.2f}")

#fooder

st.markdown("----")
st.markdown("Ingeniería de Sistemas - Grupo 4 Ecuaciones Diferenciales NRC 40-65412 - Uniminuto a Distancia")