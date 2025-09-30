--------------------------------------------------------------------
--------------------------------------------------------------------
UNIVERSIDAD GERARDO BARRIOS
--------------------------------------------------------------------
--------------------------------------------------------------------

**MATERIA -
PROGRAMACION COMPUTACIONAL III**

--------------------------------------------------------------------


INTEGRANTES - 
ROBERTO ANTONIO LOPEZ RAMIREZ 
GERARDO ELISEO GUEVARA REYES 
--------------------------------------------------------------------

**DOCENTE -
WILLIAN ALEXIS MONTES GIRON**

--------------------------------------------------------------------

**ACTIVIDAD - 
Laboratorio 2 Segundo Cómputo – Semana 10**

--------------------------------------------------------------------

**Interpretación de resultados.**

**A. Describe brevemente de qué trata el dataset utilizado**

El dataset movies_metadata.csv contiene información sobre muchas películas. Incluye datos como el título, 
calificación promedio (vote_average), cantidad de votos, fecha de estreno, géneros, presupuesto, ingresos y otros detalles. 
Sirve para analizar qué películas son más populares, cuáles tienen mejores calificaciones y cómo se comportan diferentes tipos de
películas según distintas características.

**B. ¿Qué información permite ver el resumen estadístico?**

El resumen estadístico con describe() muestra datos importantes:
- Columnas numéricas: número de valores, promedio, desviación estándar, mínimo, máximo y percentiles (25%, 50% y 75%).
- Columnas de texto o categorías: cuántos valores no están vacíos, cuántos son diferentes, cuál aparece más y cuántas veces.
Esto ayuda a entender rápidamente cómo se distribuyen los datos y si hay valores faltantes o extremos.

**C. ¿Qué cambios o tendencias se detectan en la información del dataset?**

Se pueden ver películas con calificaciones muy altas o muy bajas.
También se pueden notar patrones según el género, la fecha de estreno o los ingresos que generaron.
La media y la mediana de las calificaciones (vote_average) muestran si la mayoría de películas tienen notas promedio o si hay muchas excepciones.

**D. ¿Qué categorías sobresalen en la comparación y por qué crees que será?**

Al ordenar las películas por vote_average, se destacan las mejor y peor valoradas.
Las películas con mejores calificaciones suelen ser conocidas o de géneros populares como acción o drama.
Las peor valoradas son generalmente películas menos conocidas o con críticas negativas.
Esto muestra cómo la popularidad y la calidad percibida influyen en las calificaciones.

**E. ¿Qué diferencias se observan entre los primeros y últimos registros?**

Los primeros registros (head()) suelen corresponder a las primeras filas del CSV, que pueden estar ordenadas por fecha de lanzamiento o un ID inicial.
Los últimos registros (tail()) representan las filas finales, probablemente películas más recientes o registros agregados al final del archivo.
Esto permite comparar cambios en calificaciones, géneros y tendencias a lo largo del tiempo.

**F. ¿Qué aportan las medidas estadísticas al análisis del dataset?**

**Media:**   indica el promedio general de calificaciones (vote_average).
**Mediana:** muestra el valor central, útil si hay valores extremos que distorsionan la media.
**Desviación**  estándar: indica cuánta variación existe en las calificaciones. Estas medidas ayudan a resumir el comportamiento general de los datos y a detectar anomalías o patrones significativos.

