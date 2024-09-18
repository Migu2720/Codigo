from Alumno import Alumno

def main():
    Jesus = Alumno("Jesus", "Cruz Hernandez")
    print(Jesus)

    Jesus.saludar()
    Jesus.adios()

    Goku = Alumno("Goku", "")
    Goku.saludar()
    Goku.adios()

if __name__ == "__main__":
    main()
