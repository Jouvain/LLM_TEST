# ---- etape 1
import torch


# ---- ouvrir le fichier en lecture avec encodage utf-8
with open("input.txt", "r", encoding="utf-8") as textfile:
    texte = textfile.read()
print("Nombre de caractères :", len(texte))
# print(texte[:200])

# ---- définir le vocabulaire
uniques_chars = sorted(set(texte))
vocab_size = len(uniques_chars)
print("Nombre de caractères unique dans ce vocabulaire :", vocab_size)

# ---- encoder /décoder
string_to_int = {ch: i for i, ch in enumerate(uniques_chars)}
int_to_string = {i: ch for i, ch in enumerate(uniques_chars)}

encode = lambda s: [string_to_int[c] for c in s]
decode = lambda l: "".join([int_to_string[i] for i in l])

print(encode("hello"))
print(decode(encode("hello")))

print(decode(encode(texte)) == texte)

# ---- utilisation d'un tensor
data = torch.tensor(encode(texte), dtype=torch.long)
print(data.shape)
print(data.dtype)

