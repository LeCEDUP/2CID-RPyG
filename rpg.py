import random, time, sys
# -------------------- EFEITOS DE TEXTO --------------------
def slow(texto, delay=0.03):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sep(simbolo='-', n=60):
    print(simbolo * n)

def pause():
    input("\n[Pressione Enter para continuar...]\n")
    