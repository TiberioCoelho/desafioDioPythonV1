import datetime
import os
import platform

data=datetime.datetime.now()
dataHoje=data.strftime("%d/%m/%Y")
cabecalho="""
Aluno=Tiberio Coelho
Sistema Bancário: versão 1.0
"""
print(cabecalho)
menu=f"""
Menu
Data : {dataHoje}
-------------------------------------------
(d) Deposito
(s) Saque
(e) Extrato
(q) Sair
-------------------------------------------
"""
plataforma=platform.system()
saldo=0
limite=500
extrato=""
numero_saques=0
LIMITE_SAQUES=3
while True:    
    opcao=input(menu)
    if(opcao=="d"):
        valor_deposito=float(input("Informe o valor do depósito: "))
        if valor_deposito>0:
            saldo+=valor_deposito
            extrato+=f"Depósito: R$ {valor_deposito:.2f}\n"
            if plataforma=="Windows":
                os.system('cls')
            else:
                os.system('clear')                     
    elif(opcao=="s"):
        valor_saque=float(input("Informe o valor do saque: "))
        os.system('cls') 
        if(LIMITE_SAQUES>numero_saques):
            if(valor_saque<=saldo):
                saldo-=valor_saque
                numero_saques+=1
                extrato+=f"Saque: R$ {valor_saque:.2F}\n" 
                if plataforma=="Windows":
                    os.system('cls')
                else:
                    os.system('clear')                 
            else:
                print("Valor excedeu o seu limite de saldo")
                
        else:
            print("Limite de 3 saques do dia excedeu")  
           
            
    elif(opcao=="e"):
        print("---------Extrato bancário---------")
        print("Não foram realizadas movimentações." if not extrato else extrato )
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("----------------------------------")
        print("Número de saques permitidos para o dia: ",LIMITE_SAQUES-numero_saques)
        
    elif(opcao=="q"):
        break
    else:
        print("Opção inválida, selecione uma opção valida")
