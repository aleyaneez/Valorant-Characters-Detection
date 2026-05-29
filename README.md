# Detección de Personajes Duelistas de Valorant

**Proyecto de detección de personajes en videojuegos mediante visión por computadora**

**Autores:** Rocío Rivas (@Roussd) & Alejandro Yáñez (@aleyaneez)

---

## Objetivo

Aplicar técnicas de visión por computadora para detectar y clasificar personajes del videojuego Valorant, limitándose a los 8 personajes del rol **duelista**: Reyna, Jett, Phoenix, Raze, Yoru, Neon, Iso y Waylay.

---

## Dataset

- **1250 imágenes** extraídas de partidas grabadas directamente del juego.
- **1654 anotaciones** realizadas en [Roboflow](https://roboflow.com/), con un mínimo de 200 anotaciones por personaje para garantizar un dataset balanceado.
- Las imágenes fueron realizadas en un solo mapa (Ascent) y capturan variaciones en fondos, iluminación y ángulos dentro del juego.
- Se realizaron dos iteraciones de entrenamiento:
  1. Imágenes con un solo personaje en pantalla.
  2. Imágenes con múltiples personajes (duelistas y otros roles).

---

## Entrenamiento

- **Modelo:** YOLO11s (Ultralytics)
- **Plataforma:** Google Colab Pro con GPU T4
- **Versiones de software:**
  - Python 3.12
  - Ultralytics 8.3.223
  - PyTorch 2.9 con CUDA 12.6
  - OpenCV 4.12.0
- Notebook: [`ProyectoCV-RocíoRivas-AlejandroYáñez.ipynb`](./ProyectoCV-RocíoRivas-AlejandroYáñez.ipynb)

---

## Resultados

| Métrica | Valor |
|---------|-------|
| mAP50 general | **0.94** |
| Clase con mejor rendimiento | Iso (0.96) |
| Clase con menor rendimiento | Reyna (0.91) |

---

## Inferencia

Se utilizó el script [`test.py`](./test.py) para ejecutar el modelo sobre videos en tiempo real.

- **Hardware:** NVIDIA RTX 3060 8GB
- **Confianza mínima:** 0.8
- El modelo detecta correctamente a los personajes duelistas. Con personajes de otros roles, en ocasiones los ignora y en otras los detecta, dependiendo del contexto visual.

### Controles del visor

| Tecla | Acción |
|-------|--------|
| `Q` | Salir |
| `→` | Adelantar 5 segundos |
| `←` | Retroceder 5 segundos |

---

## Archivos del repositorio

```
├── ProyectoCV-RocíoRivas-AlejandroYáñez.ipynb   # Notebook de entrenamiento
├── test.py                                       # Script de inferencia en video
├── best.pt                                       # Pesos del modelo entrenado
├── requirements.txt                              # Dependencias del proyecto
└── README.md                                     # Este archivo
```

---

## Créditos

Proyecto desarrollado por **Rocío Rivas** (@Roussd) y **Alejandro Yáñez** (@aleyaneez) con fines prácticos, abarcando el ciclo completo de un proyecto de visión por computadora: creación de dataset, etiquetado, entrenamiento e inferencia.
