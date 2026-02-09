from datetime import datetime
import os
import re
from datetime import datetime
import os

# 🔑 LLAVE MAESTRA
ADMIN_PASSWORD = "TU CONTRASEÑA AQUÍ / UR PASSWORD HERE" # Replace with your actual password locally

class SecurityManager:
    def __init__(self, db_file="blacklist.txt"):
        self.db_file = db_file
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w", encoding="utf-8") as f:
                pass

    def is_valid_name(self, name):
        """Filtra nombres falsos, repetidos o con números"""
        # Solo letras y espacios, de 2 a 30 caracteres
        pattern = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,30}$"
        if re.match(pattern, name):
            # Bloquea 'aaa', 'xxx', etc. (debe tener al menos 2 letras distintas)
            if len(set(name.lower().replace(" ", ""))) < 2:
                return False
            return True
        return False

    def check_access(self, username):
        with open(self.db_file, "r", encoding="utf-8") as f:
            blacklist = [line.strip().lower() for line in f.readlines()]
        return username.lower() not in blacklist

    def add_to_blacklist(self, username):
        if self.check_access(username):
            with open(self.db_file, "a", encoding="utf-8") as f:
                f.write(f"{username}\n")
            return True
        return False

    def remove_from_blacklist(self, username):
        if not self.check_access(username):
            with open(self.db_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open(self.db_file, "w", encoding="utf-8") as f:
                for line in lines:
                    if line.strip().lower() != username.lower():
                        f.write(line)
            return True
        return False

    def log_event(self, event_type, username):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("access_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{now}] {event_type}: {username}\n")

    def show_history(self):
        try:
            with open("access_log.txt", "r", encoding="utf-8") as f:
                print("\n" + "="*40 + "\n📜 HISTORIAL DE SEGURIDAD\n" + "="*40)
                print(f.read() or "El historial está vacío.")
        except FileNotFoundError:
            print("\n📭 No hay historial.")

def main():
    manager = SecurityManager()
    print("\n--- 🛡️ Security System Manager v7.0 ---")

    while True:
        print("\n1. Verificar Acceso\n2. Bloquear (Admin)\n3. Desbloquear (Admin)\n4. Ver Historial (Admin)\n5. Salir")
        opcion = input("\nSeleccione: ")

        if opcion in ["2", "3", "4"]:
            if input("🔑 Admin Pass: ") != ADMIN_PASSWORD:
                print("❌ Password incorrecto.")
                continue

        if opcion == "1":
            user = input("👤 Introduce usuario: ").strip()
            if not manager.is_valid_name(user):
                print("⚠️ Error: Introduce un nombre real (sin números ni letras repetitivas).")
                continue
            
            if manager.check_access(user):
                print(f"✅ Acceso CONCEDIDO a {user}.")
            else:
                print(f"❌ Acceso DENEGADO a {user}.")
                manager.log_event("ACCESO DENEGADO", user)

        elif opcion == "2":
            user = input("🚫 Usuario a bloquear: ").strip()
            if not manager.is_valid_name(user):
                print("⚠️ Error: Nombre inválido.")
                continue
            if manager.add_to_blacklist(user):
                manager.log_event("USUARIO BLOQUEADO", user)
                print(f"✔️ {user} bloqueado.")

        elif opcion == "3":
            user = input("🔓 Usuario a desbloquear: ").strip()
            if manager.remove_from_blacklist(user):
                manager.log_event("USUARIO DESBLOQUEADO", user)
                print(f"✅ {user} desbloqueado.")
            else:
                print(f"⚠️ {user} no estaba en la lista.")

        elif opcion == "4":
            manager.show_history()

        elif opcion == "5":
            break

if __name__ == "__main__":
    main()