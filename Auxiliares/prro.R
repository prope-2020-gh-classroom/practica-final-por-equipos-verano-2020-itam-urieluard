#Establecer directorio de trabajo
#Librerias utilizadas en su mayoria
#codigo sin acentos para evitar errores de codificacion

setwd("D:/cenace/Cuarentena/RENOVABLE ESTADISTICA/SERIE POR GCR")
library(fitdistrplus)
library(ggplot2)
library(GGally)
library(ggfortify)
library(forecast)


#Leer archivo CVS que tiene la info
DATA_SIN = read.csv("TS-SEN GCR SIN1.csv")
#Cambio de nombre la primera columna
colnames(DATA_SIN)[1] = "Fecha"
#Declaro columna a analizar
Sistema = DATA_SIN$SIN

#Aqui creo la serie de tiempo (TS)
#Sistema: columna de la cual se creara la TS
#frequency = (60 min)*(24 hrs/dia) = 1440
#60 min ya que en una hora tenemos 60 lecturas. Cambia cuando las lecturas son cada 2 min etc
TS_SIN = ts(Sistema, frequency=1440, start=0)

#algunos parametros basicos
TS_minimo=min(TS_SIN)
TS_maximo=max(TS_SIN)
TS_media=mean(TS_SIN)
TS_desvEst = sd(TS_SIN)



#histograma de la curva original
hist(TS_SIN,breaks=80,freq = F,xlab = "MW", ylab = "Densidad", main=paste("Histograma FV ","\n","GCR Occidental jun19-may20"),col = "green")

#descomposicion de la TS
Descomposicion = decompose(TS_SIN)
#graficacion de las componentes
plot(Descomposicion, type="l", xlab="Descomposicion Aditiva", ylab="MW",col="blue")

#Se extrae ruido de la TS
Ruido_SIN=Descomposicion$random
#Histograma solo del ruido
hist(Ruido_SIN,freq = F,xlim=c(-1000,1000),xlab = "MW", ylab = "Densidad", main=paste("Histograma de componente aleatoria FV ","\n","GCR Occidental jun-may-19-20"), col="green")


