# Inference Engine

Este repositorio contiene una aplicación gráfica de usuario (GUI) que permite interactuar con un motor de inferencia que usa los métodos de encadenamiento hacia adelante y hacia atrás. El motor de inferencia utiliza un conjunto de reglas y una base de hechos para determinar si se puede alcanzar un objetivo específico.

## Archivos en este repositorio

- `motor.py`: Este es el archivo principal que contiene la implementación del motor de inferencia y las reglas.
- `interfaz.py`: Este archivo contiene la aplicación de interfaz de usuario (GUI) que interactúa con el motor de inferencia. Está implementado utilizando PyQt6.

## Cómo usar

1. Clonar este repositorio.
2. Instalar las dependencias necesarias. Se necesita Python y PyQt6.
3. Ejecutar `interfaz.py`.

Una vez que se inicia la aplicación, el usuario tiene la opción de ingresar reglas manualmente o importarlas desde un archivo de texto. Además, el usuario puede ingresar una base de hechos inicial y un objetivo.

Una vez que todos estos datos estén en su lugar, el usuario puede elegir si desea usar el encadenamiento hacia adelante o hacia atrás para evaluar si el objetivo puede ser alcanzado. El motor de inferencia ejecutará el algoritmo seleccionado y mostrará el resultado, además de los pasos tomados para llegar a ese resultado.

Las reglas se ingresan en el formato: "antecedente1, antecedente2->consecuente", donde los antecedentes y el consecuente son afirmaciones simples. Los antecedentes pueden ser múltiples y están separados por comas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
