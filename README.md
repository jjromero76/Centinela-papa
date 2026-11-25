# 🥔 Centinela de la Papa — Detección Temprana de Tizón Tardío (*Phytophthora infestans*)

Sistema de aprendizaje profundo y fusión multimodal desarrollado para asistir a productores y técnicos agrícolas en la detección temprana del tizón tardío en hojas de papa (*Solanum tuberosum*), combinando visión por computador, series agroclimáticas y criterios de IA ética.

## 📊 Evolución del Desempeño Experimental (Conjunto de Prueba, $n = 247$)

| Fase / Modelo | Modalidad | Exactitud Global | Sensibilidad (Recall) | Puntaje F1 | Hallazgo Principal |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Línea Base** | Clase Mayoritaria | 35,22 % | 0,00 % | 0,0000 | Ignora el 100 % de las plantas enfermas. |
| **Fase 1: MLP Regularizado** | Tabular (Color RGB/HSV/ExG) | 66,40 % | **93,13 %** | 0,7822 | Alta sensibilidad, pero 72 falsas alarmas por falta de textura espacial. |
| **Fase 2 — Rama A: ResNet50 (FT)** | Visión por Computador (CNN) | **85,02 %** | 82,50 % | **0,8680** | Reduce drásticamente los falsos positivos al analizar forma y textura foliar. |
| **Fase 2 — Rama B: GRU** | Serie Climática (NASA POWER) | 65,59 % | **100,00 %** | 0,7901 | Detecta el 100 % de las ventanas temporales de riesgo epidemiológico. |
| **Fase 2 — Rama C: Fusión Tardía** | Multimodal (`Imagen + Clima`) | **85,02 %** | 82,50 % | **0,8680** | Mantiene el desempeño óptimo visual; el clima opera como alerta temprana. |

---

## 🗂️ Estructura del Proyecto

* **`data/`**: Metadatos auditados (1.188 registros válidos de INRAE) y serie diaria agroclimática (1.096 días de NASA POWER, 2023–2025).
* **`fase_1_linea_base_mlp/`**: Cuaderno ejecutable en PyTorch, pesos guardados (`.pth`), curvas de regularización, matriz de confusión e informe técnico-ético.
* **`fase_2_multimodal_cnn_rnn/`**: Comparativa `ResNet50` vs. `EfficientNet-B0` + mapas de calor `Grad-CAM`, contraste de redes recurrentes (`RNN` vs. `LSTM` vs. `GRU`), estudio de ablación multimodal, bitácora de auditoría de IA y presentación de sustentación.
* **`fase_3_despliegue_y_escalamiento/`**: Prototipo de inferencia rápida en CPU y guía metodológica para recolección de datos locales en Colombia.

---

## ⚙️ Reproducción Rápida

1. Clonar el repositorio e instalar dependencias:
   ```bash
   git clone [https://github.com/jjromero76/centinela-papa.git](https://github.com/jjromero76/centinela-papa.git)
   cd centinela-papa
   pip install -r requirements.txt