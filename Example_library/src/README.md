# 🔧 Código Fuente

Este directorio contiene el código fuente y utilidades que se utilizan en los notebooks y ejemplos.

## Estructura

```
src/
├── utils/              # Funciones de utilidad general
├── processors/         # Procesadores de datos
├── visualization/      # Utilidades de visualización
└── api/               # Implementaciones de API
```

## Módulos Principales

### Utils
- Funciones helper para manejo de archivos
- Utilidades de conversión
- Funciones de validación

### Processors
- Procesadores de PDF
- Procesadores de Excel
- Transformadores de datos

### Visualization
- Funciones de plotly personalizadas
- Helpers para Streamlit
- Utilidades de gráficos

### API
- Implementaciones de FastAPI
- Middlewares y utilidades
- Modelos y schemas

## Uso

Para utilizar estas utilidades en los notebooks:

```python
from src.utils import file_helpers
from src.processors import pdf_processor
from src.visualization import plot_utils
``` 