print('====== LOJA DO TAIGO ======')
dinheiro = float(input('qual o valor da compra? '))
print('''FORMA DE PAGAMENTO
[1] a vista dinheiro/chque
[2] a vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('qual vai ser a opção? '))
if opcao == 1:
    total = dinheiro - ( dinheiro * 10 / 100)
    print('sua compra foi de {:.2f} e com desconto fica {:.2f}'.format(dinheiro, total))
elif opcao == 2:
    total = dinheiro - ( dinheiro * 5 / 100)
    print('sua compra foi de {:.2f} e com desconto fica {:.2f}'.format(dinheiro, total))
elif opcao == 3:
     print('sua compra foi de {:.2f}'.format(dinheiro))
elif opcao == 4:
    total = dinheiro + ( dinheiro * 20 / 100)
    parcelatotal = int(input('quantas parcelas?'))
    parcela = total / parcelatotal
    print('sua compra sera parcelada em {}x de R${:.2f}'.format(parcelatotal,parcela))
    print('sua compra foi de {:.2f} e com parcelas de {} a compra fica {:.2f}'.format(dinheiro, parcela, total))
else:
    print('opção invalida')
    print('sua compra será de {}'.format(dinheiro))