Python est un peu différent des autres langages de programmation en ce qu'il n'a pas de portée de bloc.

Cela signifie que les variables créées imbriquées dans d'autres blocs de code, par exemple les boucles for, les instructions if, les boucles while, etc., n'obtiennent pas de portée locale. On leur donne une portée de fonction si elles sont dans une fonction ou une portée globale si elles ne le sont pas.

par exemple

```
# Accessible partout
my_global_var = 1

def my_function():
    # Accessible uniquement dans my_function()
    my_local_var = 2

for _ in range(10):
    # Accessible partout
    my_block_var = 3

```