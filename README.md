# Proyecto Docker con Python y BigQuery

Este proyecto demuestra la integración de Python con Docker y incluye esquemas para BigQuery.

## Objetivo del Proyecto

El proyecto tiene como finalidad demostrar:
1. Configuración básica de un entorno Docker para Python
2. Manejo de archivos entre contenedor y host
3. Implementación de buenas prácticas en manejo de errores
4. Uso de volúmenes en Docker Compose
5. Definición de esquemas para BigQuery usando diferentes formatos

## Estructura del Proyecto

```
.
├── first_project.py      # Script principal de Python
├── Dockerfile           # Configuración de la imagen Docker
├── docker-compose.yml   # Configuración de servicios
├── output.txt          # Archivo de salida generado
├── README.md           # Este archivo
├── schema_gastos.proto # Esquema en formato Protocol Buffer
├── schema_gastos.avsc  # Esquema en formato Apache Avro
└── create_table_gastos.sql # Script SQL para crear tabla en BigQuery
```

## Componentes del Proyecto

### 1. Aplicación Docker
- Script Python que genera un archivo de salida
- Configuración Docker para ejecución en contenedor
- Manejo de volúmenes para persistencia de datos

### 2. Esquemas BigQuery
El proyecto incluye tres formatos de definición para la tabla de gastos:

1. **Protocol Buffer (proto3)**
   - Definición moderna y eficiente
   - Ideal para servicios gRPC
   - Archivo: `schema_gastos.proto`

2. **Apache Avro**
   - Formato JSON para definición de esquema
   - Soporte para tipos nullables
   - Archivo: `schema_gastos.avsc`

3. **SQL DDL**
   - Creación directa de tabla en BigQuery
   - Define tipos nativos de BigQuery
   - Archivo: `create_table_gastos.sql`

## Pasos para Ejecutar

### Docker
1. Crear el archivo output.txt:
```bash
touch output.txt
```

2. Asignar permisos al archivo:
```bash
chmod 666 output.txt
```

3. Construir y ejecutar con Docker Compose:
```bash
docker compose up --build
```

### BigQuery
Para crear la tabla en BigQuery:

1. Asegúrate de tener configurado el proyecto en BigQuery
2. Ejecuta el script SQL:
```bash
bq query --use_legacy_sql=false < create_table_gastos.sql
```

## Estructura de la Tabla de Gastos

La tabla incluye campos para:
- Información de subbloque y moneda
- Datos de pólizas y personal
- Referencias e IDs
- Fechas y tipos de cambio
- Importes en diferentes monedas

## Requisitos

- Docker
- Docker Compose
- Google Cloud SDK (para BigQuery)
- Permisos de escritura en el directorio del proyecto
- Acceso a un proyecto de Google Cloud

## Manejo de Errores

El proyecto incluye manejo de errores para:
- Problemas de permisos de archivo
- Errores de escritura/lectura
- Codificación de caracteres (UTF-8)
- Validación de tipos de datos en BigQuery