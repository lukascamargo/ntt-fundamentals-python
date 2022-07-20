import random
import perguntar
import calcular

def main():
  A = perguntar.exec()
  B = int(random.random() * 100)
  calcular.exec(A,B)

if (__name__ == "__main__"):
    main()