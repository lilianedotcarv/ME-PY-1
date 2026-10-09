def matrizSala():
    sala = [
        ["Ana", "Bruno"],
        ["Carla", "Daniel"]
    ]
    print("Disposição dos alunos na sala (2x2):")
    for fileira in sala:
        print(" | ".join(fileira))
