# Examen Final
# Jack Delvalle y Ana Duarte

## Descripción

Este proyecto implementa y dockeriza dos algoritmos de planificación de procesos:
- **Round Robin**
- **SJF Preemptive (Shortest Job First Preemptive)**

Ambos algoritmos fueron implementados en Python y dockerizados para su ejecución en contenedores, garantizando un entorno consistente para su ejecución.

## Tecnologías Utilizadas

- **Docker**: Para la creación de contenedores y la ejecución de los algoritmos en un entorno aislado.
- **Python 3.9**: Lenguaje utilizado para implementar los algoritmos.
- **Pandas**: Para el manejo de datos (si es necesario para la lectura del archivo CSV).

## Archivos del Proyecto

- **`procesos.csv`**: Contiene los datos de los procesos, como el ID del proceso, el tiempo de llegada, el tiempo de ejecución, etc.
- **`round_robin.py`**: Implementación del algoritmo Round Robin.
- **`sjf_preemptive.py`**: Implementación del algoritmo SJF Preemptive.
- **`dockerfile.round_robin`**: Dockerfile para crear la imagen de Docker para el algoritmo Round Robin.
- **`dockerfile.sjf_preemptive`**: Dockerfile para crear la imagen de Docker para el algoritmo SJF Preemptive.

### Entrada
Archivo `procesos.csv`:

## Pasos para la Creación de las Imágenes Docker

### 1. Crear la Imagen para Round Robin

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY round_robin.py procesos.csv ./
CMD ["python", "round_robin.py"]

##  **Construir las imagenes Docker**
### Round Robin
```bash
docker build -f dockerfile.round_robin -t round_robin_image .
```
### Shortest Time Preemptive
```bash
docker build -f dockerfile.sjf_preemptive -t sjf_preemptive_image .
```

---

## **Ejecutar los Contenedores**

### Contenedor Round Robin
```bash
docker run -d --name round_robin_container round_robin_image
```
### Contenedor Shortest Time
```bash
docker run -d --name sjf_preemptive_container sjf_preemptive_image
```

---

## **Verificar los Contenedores**
### Listar contenedores activos
```bash
docker ps
```
### Ver logs de un contenedor
```bash
docker logs round_robin_container
docker logs sjf_preemptive_container
```

---
## **Detener y Eliminar Contenedores**

Cuando finalices las pruebas:
```bash
docker stop round_robin_container round_robin_container
docker rm sjf_preemptive_container sjf_preemptive_container
```
