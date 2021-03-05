install.packages("tidyverse",dep = TRUE)
library(tidyverse)

install.packages("magic",dep=TRUE)
library(magic)

x=pi
sin(x)
cos(60)
cos(60*pi/180)
sin(60*pi/180)
tan(pi)
tan(pi/3)
asin(0.8660254)
asin(0.8660254)*180/pi
round(x = 2.43,digits = 1)
floor(-3.45)
trunc(-3.45)
double = function(x) {x*2}
x = double(3)
x
y <- x
cos(pi/4) -> z

cuadrado = function(x) {x^2}
cuadrado(2)
ala3 <- function(x) {x^3}
ala3(3)
pot = function (x,y) {x^y}
pot(2,3)
hello = function (x) {
  print("Hello")
  print
}
hello("Maria")
suma5 = function(num) {
  num = num + 1;
  num = num + 1;
  num = num + 1;
  num = num + 1;
  num + 1
}

argumento = 3
suma5(argumento)
argumento