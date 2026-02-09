ENG

# 🛡️ Security System Manager (v3.0)

This is a lightweight access control system developed in **Python**. It features persistent user blacklist management via text files, including real-time administrative functions to block or grant access.

## 🚀 Key Features
* **Data Persistence:** Blocked entries are stored in a `blacklist.txt` file, ensuring data is retained after program termination.
* **Dynamic Management (CRUD):** Administrators can manage the blacklist directly through the console interface.
* **Smart File Routing:** Utilizes the `os` library to automatically resolve file paths, ensuring cross-platform compatibility regardless of the execution directory.
* **Security:** Password-protected administrative control panel.

## 📂 Project Structure
To ensure proper execution, the following structure is maintained:
- `main.py`: Main source code.
- `blacklist.txt`: Database file (automatically generated upon execution).

## 🛠️ Usage Flow

### 👤 Standard Users
1. Enter your username.
2. The system cross-references the input with `blacklist.txt`.
3. Access is **GRANTED** or **DENIED** instantly.

### 🔑 Administrator Mode
* Access by entering `admin` at the username prompt.
* Requires authentication (Default password: `2026_secure`).
* **Block Action:** If the username is not listed, it is added to the blacklist.
* **Unblock Action:** If the username exists in the list, the system automatically removes it (granting access again).

## 💻 Requirements
* Python 3.x
* `os` Library (Native Python module).

---
*Educational project focused on mastering file I/O logic and path management in Python.*

# Author: akaEGO-dev
# Project: Security System Manager v3.0


ESP

# 🛡️ Security System Manager (v3.0)

Este es un sistema de control de acceso básico desarrollado en **Python**. Permite gestionar una lista negra de usuarios almacenada de forma persistente en un archivo de texto, con funciones de administrador para bloquear y desbloquear accesos en tiempo real.

## 🚀 Características
* **Persistencia de Datos:** Los nombres bloqueados se guardan en un archivo `blacklist.txt` para que no se pierdan al cerrar el programa.
* **Gestión Dinámica (CRUD):** El administrador puede añadir o eliminar usuarios de la lista negra directamente desde la consola.
* **Rutas Inteligentes:** Utiliza la librería `os` para localizar los archivos automáticamente, sin importar en qué carpeta o PC se ejecute.
* **Seguridad:** Panel de control protegido por contraseña.

## 📂 Estructura del Proyecto
Para que el programa funcione correctamente, debe mantenerse en una carpeta propia:
- `main.py`: Código fuente principal.
- `blacklist.txt`: Base de datos (se genera automáticamente al ejecutar).

## 🛠️ Cómo funciona

### 👤 Usuarios Normales
1. Ingresan su nombre.
2. El sistema verifica si el nombre existe en `blacklist.txt`.
3. El acceso es **PERMITIDO** o **DENEGADO** instantáneamente.

### 🔑 Administrador
* Se accede escribiendo `admin` en el prompt de nombre.
* Requiere contraseña (por defecto: `2026_secure`).
* **Bloqueo:** Si el nombre ingresado no está en la lista, se añade.
* **Desbloqueo:** Si el nombre ya está en la lista, el sistema lo elimina automáticamente (lo "perdona").

## 💻 Requisitos
* Python 3.x
* Librería `os` (incluida de forma nativa en Python).

---
*Proyecto educativo desarrollado para entender la lógica de archivos y rutas en Python.*

# Autor: akaEGO-dev
# Proyecto: Security System Manager v3.0