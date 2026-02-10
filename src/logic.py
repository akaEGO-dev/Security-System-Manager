from datetime import datetime
import os
import re

# Configuramos las rutas relativas para que funcione desde src
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 🔑 LLAVE MAESTRA (La lógica la necesita para validar)
ADMIN_PASSWORD = "TU CONTRASEÑA AQUÍ"


class SecurityManager:
    def __init__(self, db_file="blacklist.txt"):
        self.db_file = os.path.join(DATA_DIR, "blacklist.txt")
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w") as f:
                pass

    def is_valid_name(self, name):
        pattern = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,30}$"
        if re.match(pattern, name):
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

    with open(os.path.join(DATA_DIR, "access_log.txt"), "a", encoding="utf-8") as f:
        f.write(f"[{now}] {event_type}: {username}\n")

    def show_history(self):
        try:
            with open(
                os.path.join(DATA_DIR, "access_log.txt"), "r", encoding="utf-8"
            ) as f:
                print("\n" + "=" * 40 + "\n📜 HISTORIAL DE SEGURIDAD\n" + "=" * 40)
                print(f.read() or "El historial está vacío.")
        except FileNotFoundError:
            print("\n📭 No hay historial.")


# (Sustituye SecurityManager por el nombre real de tu clase)
