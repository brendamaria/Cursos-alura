
public abstract class Conta {
	
	protected double saldo;
	private int agencia;
	private int numero;
	private Cliente titular;
	private static int total;
	
	public Conta(int agencia, int numero) {
		this.agencia = agencia;
		this.numero = numero;
		Conta.total++;
	}
	
	public static int getTotal(){
		return Conta.total;
	}
	
	public abstract void deposita(double valor);
	
	
	public void saca(double valor) throws SaldoInsuficienteException{

        if(this.saldo < valor) {
            throw new SaldoInsuficienteException("Saldo: " + this.saldo + ", Valor: " + valor);
        } 

        this.saldo -= valor;       
	}
	
	public void transfere(double valor, Conta destino) throws SaldoInsuficienteException {
			this.saca(valor);
			destino.deposita(valor);
	}
	
	public double getSaldo() {
		return this.saldo;
		
	}

	public int getAgencia() {
		return this.agencia;
	}

	public void setAgencia(int agencia) {
		this.agencia = agencia;
	}

	public int getNumero() {
		return this.numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public Cliente getTitular() {
		return titular;
	}

	public void setTitular(Cliente titular) {
		this.titular = titular;
	}

}
