import os

# Esto detecta la carpeta real donde está tu main.py
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
# Esto crea el archivo justo ahí al lado
DB_FILE = os.path.join(carpeta_actual, "blacklist.txt")


def load_list():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        # Leemos el archivo y  lo limpiadmos de espacios/saltos de linea.
        return [line.strip() for line in f.readlines()]


def save_name(nombre):
    with open(DB_FILE, "a") as f:
        f.write(nombre + "\n")


# --- INICIO DEL PROGRAMA ---
black_list = load_list()
admin_pass = "2026_secure"

while True:
    print(f"\n--- SISTEMA DE SEGURIDAD V3 (DB Activa) ---")
    user_input = input("Nombre a verificar (o 'admin'): ").lower().strip()

    if user_input == "salir":
        break

    # 1. CARGAMOS LA LISTA ACTUALIZADA Y EN MINÚSCULAS
    black_list = [n.lower() for n in load_list()]

    # 2. CASO ADMINISTRADOR:
    if user_input == "admin":
        if input("Password: ") == admin_pass:
            print(f"--- LISTA NEGRA ACTUAL: {black_list} ---")
            target_user = (
                input("Nombre a gestionar (Bloquear/Desbloquear): ").lower().strip()
            )

            if target_user in black_list:
                # LÓGICA DE DESBLOQUEO
                black_list.remove(target_user)
                with open(DB_FILE, "w") as f:
                    for n in black_list:
                        f.write(n + "\n")
                print(f"✅ {target_user} ha sido DESBLOQUEADO y eliminado del archivo.")
            else:
                # LÓGICA DE BLOQUEO (La que ya tenías)
                save_name(target_user)
                print(f"🚫 {target_user} ha sido BLOQUEADO permanentemente.")
        else:
            print("ACCESO DENEGADO (Password incorrecto)")

    # 3. CASO USUARIO NORMAL:
    else:
        if user_input in [n.lower() for n in black_list]:
            print(f"ALERTA: {user_input} está bloqueado")
        else:
            print(f"ACCESO PERMITIDO PARA {user_input}")
