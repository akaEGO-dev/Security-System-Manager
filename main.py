import os


class SecurityManager:
    def __init__(self, db_file="blacklist.txt"):
        self.db_file = db_file
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        """Asegura que la base de datos existe sin borrar datos previos."""
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w", encoding="utf-8") as f:
                pass

    def check_access(self, username):
        """Verifica si un usuario está en la lista negra."""
        with open(self.db_file, "r", encoding="utf-8") as f:
            blacklist = [line.strip().lower() for line in f.readlines()]
        return username.lower() not in blacklist

    def add_to_blacklist(self, username):
        """Añade un usuario a la lista negra si no existe."""
        if not self.check_access(username):
            print(f"⚠️  {username} ya está en la lista negra.")
            return False

        with open(self.db_file, "a", encoding="utf-8") as f:
            f.write(f"{username}\n")
        return True


# --- Lógica de Interfaz (akaEGO-dev Interface) ---
def main():
    manager = SecurityManager()
    print("--- 🛡️ Security System Manager v4.0 ---")

    while True:
        print("\n1. Verificar Acceso\n2. Bloquear Usuario\n3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            user = input("Introduce usuario: ")
            if manager.check_access(user):
                print(f"✅ Acceso CONCEDIDO a {user}.")
            else:
                print(f"❌ Acceso DENEGADO. {user} está en la lista negra.")

        elif opcion == "2":
            user = input("Usuario a bloquear: ")
            if manager.add_to_blacklist(user):
                print(f"🚫 {user} ha sido añadido a la lista negra.")

        elif opcion == "3":
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
