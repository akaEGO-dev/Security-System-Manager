# 🛡️ Security Access Manager (v7.0)

![Python](https://img.shields.io/badge/Language-Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Validated-success?style=for-the-badge&logo=shield)
![Status](https://img.shields.io/badge/Status-Finalized-green?style=for-the-badge)
---

## 📖 Descripción / Description

**ES:** Sistema bilingüe de gestión de acceso con arquitectura modular. Separa la lógica de negocio del punto de entrada para mayor escalabilidad, incluyendo validación avanzada, control de listas negras y auditoría.

**EN:** Bilingual access management system with modular architecture. It separates business logic from the entry point for better scalability, including advanced validation, blacklist control, and auditing.

---

## 📊 Características / Features

| Característica / Feature | Detalle / Detail |
| :--- | :--- |
| **Engine** | Python 3.x |
| **Architecture** | Modular (Main / Logic separation) |
| **Validation** | Regex (Regular Expressions) |
| **Storage** | Local .txt (Persistence) |
| **Logging** | Datetime stamped activity |

---

## 📁 Estructura del Proyecto / Project Structure

**ES:**
* `main.py`: Punto de entrada de la aplicación y menú interactivo.
* `src/logic.py`: Núcleo del sistema (Clase `SecurityManager`).
* `data/`: Almacenamiento local (Blacklist y Logs).

**EN:**
* `main.py`: Application entry point and interactive menu.
* `src/logic.py`: System core (`SecurityManager` class).
* `data/`: Local storage (Blacklist and Logs).

---

## 🚀 Instalación / Installation

**ES:**
1. Clonar el repositorio: 
   `git clone https://github.com/akaEGO-dev/Security-System-Manager.git`
2. Entrar a la carpeta: 
   `cd Security-System-Manager`
3. Ejecutar la aplicación (desde la raíz): 
   `python main.py`

**EN:**
1. Clone the repository: 
   `git clone https://github.com/akaEGO-dev/Security-System-Manager.git`
2. Enter the folder: 
   `cd Security-System-Manager`
3. Run the application (from root): 
   `python main.py`

---

## 🔒 Privacidad y Seguridad / Privacy & Security

> [!IMPORTANT]
> **ES:** Este repositorio utiliza un archivo `.gitignore`. Las bases de datos locales (`blacklist.txt`) y los registros de actividad (`access_log.txt`) se mantienen exclusivamente en tu máquina local y **nunca** se suben a la nube.
>
> **EN:** This repository utilizes a `.gitignore` file. Local databases (`blacklist.txt`) and activity logs (`access_log.txt`) are kept exclusively on your local machine and are **never** uploaded to the cloud.

---

## 👤 Autor / Author

* **Developer:** [Francisco Cruz / akaEGO-dev]
* **GitHub:** [@akaEGO-dev](https://github.com/akaEGO-dev)
* **Status:** 🟢 Finalized / Stable

---
**Developed with 🐍 by akaEGO-dev**
*"Building secure code, one module at a time."*
