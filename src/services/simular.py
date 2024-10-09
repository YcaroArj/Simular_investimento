class Simular_investimento:
    def __init__(self, inv_inicial, inv_mensal, prazo, rentabilidade):
        self.inv_inicial = float(inv_inicial)
        self.inv_mensal = float(inv_mensal)
        self.prazo  = float(prazo)
        self.rentabilidade = float(rentabilidade / 100)
    
    def valor_investido(self) -> float:
        return self.inv_inicial + (self.inv_mensal * self.prazo)
    
    def valor_bruto(self) -> float:
        return self.inv_inicial * (1 + self.rentabilidade) ** self.prazo + self.inv_mensal * ((1 + self.rentabilidade) ** self.prazo - 1 ) / self.rentabilidade
    
    def valor_juros(self) -> float:
        return self.valor_bruto() - self.valor_investido()
    
    def valor_pago_IR(self) -> float:
        return self.valor_juros() * 0.15
    
    def valor_liquido(self) -> float:
        return self.valor_bruto() - self.valor_pago_IR()