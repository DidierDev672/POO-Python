# Nota y mejoras posibles

1. ***Orbitas no circulares:*** hoy usamos orbitas circulares (facil). Para mas realismo, introduce excentricidad y calculo con anomalia verdadera.

2. ***Fases iniciales:*** Aqui todos empiezan en angulos >0 (x = a, y = 0). Puedes agregar fase inicial >(mean_anomaly_at_epoch) como atributo.

3. ***Integracion dinamica:*** Para simulacion gravitacionales reales usuarios un integrador numerico >(verlet, RK4) y la suma de fuerzas entre cuerpo >(N-body). Para eso convienen librerias cientificas >(Numpy) o integradores existentes.

4. ***Visualizacion:*** Puedes graficar posiciones con ***matplotlib*** para ver orbitas.

5. ***Unidades:*** El codigo usa metros y segundos; para imprimir convertimos a AU a dias cuando conviene.