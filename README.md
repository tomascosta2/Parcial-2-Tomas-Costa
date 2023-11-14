# Parcial-2-Tomas-Costa

# Nombre: Tomás Costa
# Legajo:
# Email: tomascostapp@gmail.com 
# DNI: 44.625.800

# De que trata el proyecto:
Es un proyecto extraido de pruebas de ingreso a mercado libre que consta en
detectar caracteres consecutivos en el adn para determinar si un humano es mutante o no

# Como lo resolvi (Alto nivel):
Lo que hice en un principio fue recorrer el adn en las direcciones que se puede encontrar
la "anomalia" vertical, horizontal y diagonalmente, usando bucles y una variable auxiliar 
en la que guardaba el ultimo valor leido y lo comparaba con el actual lo que en caso de 
coincidir sumaba uno a un contador el cual de llegar a cuatro retornaba que el adn era de 
un mutante.
Como lo optimice:
Para optimizar el codigo use algunas funciones de Python como:
- join: Con esta funcion junte en una cadena las secuencias correspondientes a las distintas para despues detectar si en alguna de las subcadenas se repetia 4 veces una letra lo que me ahorro tener que usar la variable auxiliar
- any: Indica si en alguno de los casos dados (pasados como bucles for) se cumple cierta condicion
Además 



# Como correrlo