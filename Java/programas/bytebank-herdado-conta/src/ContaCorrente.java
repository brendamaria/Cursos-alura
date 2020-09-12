
public class ContaCorrente extends Conta {
	
	public ContaCorrente(int agencia, int numero) {
		super(agencia, numero);
		System.out.println("criando uma conta corrente");

	}
	
	@Override
	public boolean saca(double valor) {
		return super.saca(valor + 0.2);
	}

	@Override
	public void deposita(double valor) {
		super.saldo += valor;
		
	}
	
}
