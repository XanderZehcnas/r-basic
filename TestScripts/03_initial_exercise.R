segundos = 250000000
diassegs = 24*3600
seganyo = 365*diassegs
cuatroanyo = seganyo*4 + diassegs

val4 = segundos%/%cuatroanyo
pendsegs = segundos%%cuatroanyo
val3 = pendsegs%/%seganyo

print(sprintf("Segs en anyo = %i",seganyo))
print(sprintf("Año = %i",2018+val4*4+val3))


lastsegs = pendsegs-seganyo*3-diassegs;
print(lastsegs)
dias = lastsegs%/%diassegs;
horas = (lastsegs%%diassegs)%/%(60*60)
minutos = ((lastsegs%%diassegs)%%(60*60))%/%60
segundos = ((lastsegs%%diassegs)%%(60*60))%%60

print(sprintf("Fecha = Año %i, día %i a las %i:%i:%i",2018+val4*4+val3,dias,horas,minutos,segundos))
## 2 diciembre 12:26 2025


## Ejercicio 2
ecuacion = function(a,b,c) {
  (c-b)/a
}
ecuacion(5,3,0);
ecuacion(7,4,8);
ecuacion(1,1,1);

## Ejercicio 3
eje3 = 3*exp(1)-pi
print(round(eje3,3))

comp1 = 2+3i
comp2 = 5+8i
rescomp = comp1^2/comp2
print(round(rescomp,3))

## Segundo intento Ejercicio 3
totalsegs = 250000000
diassegs = 24*3600

segs = totalsegs%%60
hour = totalsegs%%diassegs%/%3600
mins = totalsegs%%(60*60)%/%60

totaldias = totalsegs%/%diassegs
cuatrienios = totaldias%/%(365*4+1)
restoanyos = totaldias%%(365*4+1)%/%365
restodias = totaldias%%(365*4+1)%%365 - 1 ##Afecta 1 año bisiesto en resto

print(sprintf("Fecha = Año %i, día %i a las %i:%i:%i",2018+cuatrienios*4+restoanyos,restodias,hour,mins,segs))
#Día 336 es 2 Diciembre (365-336 = 29 >> 2+29 = 31)
