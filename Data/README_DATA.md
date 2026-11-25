# Fuentes de Datos — Proyecto Centinela

Por políticas de almacenamiento y licenciamiento abierto, las 1.188 fotografías crudas no se alojan directamente en este repositorio.

1. **Imágenes Foliares (INRAE):**
   * **Dataset:** *S.tuberosum_Multi_Cla_Field_Leaves* (v4.0) — Bousset-Vaslin (2025).
   * **Enlace oficial:** https://doi.org/10.57745/D6DVD5
   * **Ubicación esperada:** Extraer las subcarpetas (`Alt`, `Mil`, `Oth`, `S`) dentro de `data/raw/`.

2. **Serie Agroclimática Diaria (NASA POWER):**
   * **Coordenadas:** Latitud `48.1001683`, Longitud `-1.8003047` (Le Rheu, Francia).
   * **Periodo:** `2023-01-01` a `2025-12-31` (1.096 observaciones diarias).
   * **Descarga:** El cuaderno `Fase2_CentinelaPapa.ipynb` consulta directamente la API pública de NASA POWER en tiempo de ejecución.