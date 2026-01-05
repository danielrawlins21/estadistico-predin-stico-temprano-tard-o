# Hipótesis y planteamiento del test de normalidad

## 1. Objetivo del contraste de normalidad

Antes de aplicar técnicas de inferencia estadística para comparar la anchura craneal entre periodos históricos, resulta necesario evaluar si el supuesto de normalidad es razonable en cada una de las submuestras analizadas.

El contraste de normalidad no tiene como finalidad demostrar que los datos siguen exactamente una distribución normal, sino determinar si la hipótesis de normalidad es compatible con los datos observados y, por tanto, si el uso de contrastes paramétricos posteriores puede considerarse adecuado.

---

## 2. Test utilizado: Kolmogorov–Smirnov

Para evaluar la normalidad de las distribuciones se emplea el test de Kolmogorov–Smirnov (KS). Este contraste compara la función de distribución empírica de los datos con una función de distribución teórica específica.

Dado que los parámetros de la distribución normal (media y desviación típica) no son conocidos a priori, los datos de cada submuestra se estandarizan previamente y se comparan con una distribución normal estándar \(\mathcal{N}(0,1)\).

El contraste se realiza de forma independiente para cada periodo histórico.

---

## 3. Formulación general de las hipótesis

Para cada una de las submuestras se plantean las siguientes hipótesis:

- **Hipótesis nula (H₀):** la variable *anchura craneal* sigue una distribución normal.
- **Hipótesis alternativa (H₁):** la variable *anchura craneal* no sigue una distribución normal.

El contraste se plantea de forma bilateral, ya que se pretende detectar cualquier desviación respecto a la normalidad, independientemente de su forma (asimetría, curtosis u otras irregularidades).

El nivel de significación adoptado es \(\alpha = 0.05\).

---

## 4. Hipótesis para el periodo predinástico temprano

En el caso de la submuestra correspondiente al periodo **predinástico temprano**, las hipótesis del contraste de Kolmogorov–Smirnov se formulan de la siguiente manera:

- **H₀ (temprano):** la anchura craneal de los cráneos del periodo predinástico temprano sigue una distribución normal.
- **H₁ (temprano):** la anchura craneal de los cráneos del periodo predinástico temprano no sigue una distribución normal.

Este contraste permitirá evaluar si la distribución observada en el periodo temprano es compatible con el supuesto de normalidad, condición relevante para la aplicación posterior de contrastes paramétricos.

---

## 5. Hipótesis para el periodo predinástico tardío

Para la submuestra correspondiente al periodo **predinástico tardío**, las hipótesis del contraste se establecen como:

- **H₀ (tardío):** la anchura craneal de los cráneos del periodo predinástico tardío sigue una distribución normal.
- **H₁ (tardío):** la anchura craneal de los cráneos del periodo predinástico tardío no sigue una distribución normal.

Este análisis permitirá determinar si el supuesto de normalidad resulta razonable también en el periodo tardío y si existen diferencias en el comportamiento distributivo entre ambos periodos.

---

## 6. Criterio de decisión

El criterio de decisión del contraste es el siguiente:

- Si el *p-valor* es mayor que \(\alpha = 0.05\), no se rechaza la hipótesis nula de normalidad.
- Si el *p-valor* es menor o igual que \(\alpha = 0.05\), se rechaza la hipótesis nula de normalidad.

Es importante destacar que no rechazar la hipótesis nula no implica afirmar que los datos sean normales, sino que no se dispone de evidencia suficiente para afirmar lo contrario.

---

## 7. Relación con el análisis inferencial posterior

Los resultados de estos contrastes de normalidad se utilizarán para contextualizar y discutir la validez de los análisis inferenciales posteriores, en particular el contraste de igualdad de medias mediante el test t.

Incluso en el caso de que el supuesto de normalidad no se cumpla estrictamente, el contraste t se aplicará igualmente, tal como se indica en el enunciado del ejercicio, discutiendo de forma crítica la validez de los resultados obtenidos.

