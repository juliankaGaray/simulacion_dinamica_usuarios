OBJETIVO DEL EJERCICIO:

Simular la dinámica de usuarios que interactúan con un sistema web, permitiendo:
Objetivo de la Maqueta Virtual
Simular la dinámica de usuarios que interactúan con un sistema web, permitiendo:

Estudiar la evolución de usuarios activos, procesados y abandonados.

Medir el impacto de la carga del servidor, tiempos de respuesta y congestión.

Evaluar qué tan bien resiste el sistema en situaciones críticas, como picos de demanda.

Ajustar parámetros del sistema para optimizar el rendimiento.
Estudiar la evolución de usuarios activos, procesados y abandonados.

Medir el impacto de la carga del servidor, tiempos de respuesta y congestión.

Evaluar qué tan bien resiste el sistema en situaciones críticas, como picos de demanda.

Ajustar parámetros del sistema para optimizar el rendimiento.

FUNDAMENTO MATEMÁTICO:
Se basa en un modelo derivado del clásico SIR (Susceptible - Infected - Recovered), adaptado al flujo de usuarios en un entorno web. La evolución del sistema se modela mediante ecuaciones diferenciales, considerando:

U(t): Usuarios activos conectados.

P(t): Usuarios siendo procesados.

A(t): Usuarios que abandonan el sistema.

Variables a tener en cuenta:

λ (lambda): Tasa de llegada de nuevos usuarios.

μ (mu): Tasa de procesamiento (capacidad del servidor).

α (alfa): Tasa de abandono (por error o lentitud).

θ: Tasa de finalización del procesamiento.
Parámetros a Definir
Usuarios iniciales conectados.

Capacidad del servidor, medida en procesos por segundo.

Tasa de llegada de nuevos usuarios.

Probabilidad de abandono si el sistema está lento o saturado.

Tiempo de respuesta promedio del sistema.

Cantidad de peticiones simultáneas que el sistema puede manejar.    

Herramientas utilizadas:
Python + Streamlit: Ideal para crear una interfaz web amigable e interactiva.

MATLAB / Simulink: Útil para quienes prefieren bloques visuales y simulación continua.

AnyLogic: Potente para integrar lógica condicional y simulaciones multi-método.

NetLogo: Para modelos basados en agentes (usuarios individuales).




¿Qué vamos a hacer?
Simularemos la evolución de:

U(t) → Usuarios conectados.

P(t) → Usuarios procesados.

A(t) → Usuarios que abandonan.

¿Como lo vamos a hacer?

versiones adaptadas de las siguientes ecuaciones diferenciales :
ECUACION 1:
dt
dU
​
 =λ−μU−αU
ECUACION 2:
dt
dP
​
 =μU−θP


 ECUACION 3:
dt
dA
​
 =αU



 Parámetros personalizables por el usuario:
λ: tasa de llegada de usuarios.

μ: tasa de procesamiento.

α: tasa de abandono.

θ: tasa de finalización de procesamiento.

U₀, P₀, A₀: condiciones iniciales.


Resultados Esperados
Gráficas dinámicas en tiempo real de usuarios activos, procesados y abandonados.

Detección de cuellos de botella, puntos de saturación o fallos del sistema.

Capacidad de modificar parámetros en tiempo real para ver sus efectos inmediatos.

Comprensión clara del impacto de cada variable en el rendimiento general del sistema.