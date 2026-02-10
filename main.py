from src.logic import SecurityManager, ADMIN_PASSWORD


def main():
    manager = SecurityManager()
    print("\n--- 🛡️ Security System Manager v7.0 ---")

    while True:
        print(
            "\n1. Verificar Acceso\n2. Bloquear (Admin)\n3. Desbloquear (Admin)\n4. Ver Historial (Admin)\n5. Salir"
        )
        opcion = input("\nSeleccione: ")

        if opcion in ["2", "3", "4"]:
            if input("🔑 Admin Pass: ") != ADMIN_PASSWORD:
                print("❌ Password incorrecto.")
                continue

        if opcion == "1":
            user = input("👤 Introduce usuario: ").strip()
            if not manager.is_valid_name(user):
                print("⚠️ Error: Nombre inválido.")
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
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    main()
