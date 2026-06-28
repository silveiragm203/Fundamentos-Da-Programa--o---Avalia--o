def verificar_situacao(media: float,verficar_honra: bool = True) -> tuple:
    """Retornar (situação, mensagem honra) com base na média."""
    if media >= 7.0:
        situacao ="APROVADO✅"
    elif media >= 5.0:
        situacao ="RECUPERAÇÃO⚠"
    else:
        situacao ="REPROVADO❌"

    honra = "Menção Honrosa✨"if (verficar_honra and media >= 9.0) else ""
    return situacao, honra

sit, honra = verificar_situacao(9.2)
print(f"{sit} {honra}")
sit, honra = verificar_situacao(6.1)
print(f"{sit} {honra}")
sit, honra = verificar_situacao(3.8, verficar_honra=False)
print(f"{sit} {honra}")