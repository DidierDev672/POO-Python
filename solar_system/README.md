# Nota y mejoras posibles

1. ***Orbitas no circulares:*** hoy usamos orbitas circulares (facil). Para mas realismo, introduce excentricidad y calculo con anomalia verdadera.

2. ***Fases iniciales:*** Aqui todos empiezan en angulos >0 (x = a, y = 0). Puedes agregar fase inicial >(mean_anomaly_at_epoch) como atributo.

3. ***Integracion dinamica:*** Para simulacion gravitacionales reales usuarios un integrador numerico >(verlet, RK4) y la suma de fuerzas entre cuerpo >(N-body). Para eso convienen librerias cientificas >(Numpy) o integradores existentes.

4. ***Visualizacion:*** Puedes graficar posiciones con ***matplotlib*** para ver orbitas.

5. ***Unidades:*** El codigo usa metros y segundos; para imprimir convertimos a AU a dias cuando conviene.

# 🌍 Qué verás al ejecutar el programa
1. Una ***ventana grafica*** con las orbitas de la Tierra, Marte y la Luna (Simplificada.)
2. El ***Sol*** en el centro (amarillo)
3. Cada planeta con su orbita y su posucion actual.

# 🔬 Qué puedes modificar

| Elemento | Que hace | | Ejemplo |
| -------------- | ------------ | ----------- |
| ***days_to_simulate=365*** | Duracion de la simulacion | Cambia a ***365*2*** para 2 years|
| ***semi_major_axis*** | Distancia al Sol | Prueba con 0.39 * AU para Mercurio|
| ***plt.scatter(..., s=50)*** | Tamano de los puntos | Ajusta el tamano de planetas |
| ***t_values = [i * DAY for i in range(0, days_to_simulate, 5)]*** | Paso temporal | Reduce a ***1*** para mas detalle|
