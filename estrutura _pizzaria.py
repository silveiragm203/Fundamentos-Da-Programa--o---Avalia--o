# Variáveis da pizzaria
FRETE = 2 # =Constante Fake
pizza_sabor = input("Informe o sabor da pizza - [frango com requeijão],[calabresa],[mussarela],[banana com chocolate]:")
pizza_tamanho = input("Informe o tamanho da pizza - [pequena],[média],[grande]:")
dia_semana = input("informe o dia da semana - [quarta],[quinta],[sexta],[sábado],[domingo]:")

print(f"O sabor escolhido da pizza é{pizza_sabor}, o tamanho é{pizza_tamanho} e hoje é {dia_semana}.")
# Promoções -> Estruturas condicionais

# Comprando quaer pizza e qualquer tamanho no sábado,o refri é gratuito.
if dia_semana == "sábado":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Refri hoje é por conta da casa!.")
elif dia_semana =="Domingo":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Refri e o Frete rega hoje é por conta da casa!.")
elif pizza_sabor == "calabresa":and pizza_tamanho =="média":   
    
print(f"🍕Pedido aceito com sucesso!")
    
print(f"O Frete hoje é por conta da casa!.")



# Comprando uma pizza de calabresa tamanho médio,em qualquer dia,o frete é gratuito.

# Comprando qualquer pizza de qualquer tamanho no domingo,o frete e o refrigerante são gratuitos.

