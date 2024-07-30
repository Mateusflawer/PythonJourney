from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, valor: float, parcelas: int, 
                 data_emprestimo: datetime, data_vencimento: datetime) -> None:
        self.valor = valor
        self.parcelas = parcelas
        self.data_emprestimo = datetime.strptime(data_emprestimo, '%d/%m/%Y')
        self.data_vencimento = datetime.strptime(data_vencimento, '%d/%m/%Y')

    def pegar_parcelas(self) -> list:
        parcelas = []
        valor_parcela = self.valor / self.parcelas
        dia = self.data_vencimento.day
        mes = self.data_vencimento.month
        ano = self.data_vencimento.year
        for n in range(1, self.parcelas+1):
            if mes > 12:
                ano += 1
                mes = 1
            data_parcela = datetime(ano, mes, dia).strftime("%d/%m/%Y")
            resultado = f'{n}° parcela, valor: R$ {valor_parcela:,.2f}, data: {data_parcela}'
            parcelas.append(resultado)
            mes += 1
        return parcelas
    
    def ver_parcelas(self) -> None:
        parcelas = self.pegar_parcelas()
        for parcela in parcelas:
            print(parcela)
        print()
        print(f'Você pegou um empréstimo de R$ {self.valor:,.2f} para pagar em {self.parcelas/12:.0f} anos ' \
              f'({self.parcelas} meses) em parcelas de R${self.valor / self.parcelas:,.2f}')

    def __repr__(self) -> str:
        valor = self.valor
        parcelas = self.parcelas
        data_emprestimo = self.data_emprestimo.strftime('%d/%m/%Y')
        data_vencimento = self.data_vencimento.strftime('%d/%m/%Y')
        class_name = type(self).__name__
        class_attr = f"({valor=!r}, {parcelas=!r}, {data_emprestimo=!r}, {data_vencimento=!r})"
        class_repr = f"{class_name}{class_attr}"
        return class_repr

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.emprestimos = []

    def pegar_emprestimo(self, emprestimo: Emprestimo) -> None:
        print(self.nome, f'pegou empréstimo de R${emprestimo.valor:,.2f}')
        self.emprestimos.append(emprestimo)

    def ver_emprestimos(self) -> None:
        print()
        print(f'EMPRESTIMOS do/a {self.nome}:')
        for emprestimo in self.emprestimos:
            print(emprestimo)

    def ver_parcelas_emprestimos(self) -> None:
        print()
        print(f'EMPRESTIMOS do/a {self.nome}:')
        for emprestimo in self.emprestimos:
            print(emprestimo)
            emprestimo.ver_parcelas()
            print()

    def __repr__(self) -> str:
        nome = self.nome
        idade = self.idade
        emprestimos = len(self.emprestimos)
        class_name = type(self).__name__
        class_attr = f"({nome=!r}, {idade=!r}, {emprestimos=!r})"
        class_repr = f"{class_name}{class_attr}"
        return class_repr


if __name__ == "__main__":
    p1 = Pessoa('Karina', 21)
    e1 = Emprestimo(1000000, 5*12, '21/07/2024', '20/08/2024')

    p1.pegar_emprestimo(e1)
    p1.ver_parcelas_emprestimos()
