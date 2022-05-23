id_peca, q_peca, v_peca = map(float, input().split(' '))
id_peca2, q_peca2, v_peca2 = map(float, input().split(' '))

print('VALOR A PAGAR: R$', format((q_peca * v_peca) + (q_peca2 * v_peca2), '.2f'))