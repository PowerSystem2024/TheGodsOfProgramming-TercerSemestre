from db.conexion import conectar

def main():
    conectar()
    print("Conexión a MongoDB exitosa.")

if __name__ == "__main__":
    main()