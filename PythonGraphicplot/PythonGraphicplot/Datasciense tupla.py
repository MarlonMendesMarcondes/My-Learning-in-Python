carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)

for tupla in carros:
    for item in tupla[-1]:
        print(item)
        