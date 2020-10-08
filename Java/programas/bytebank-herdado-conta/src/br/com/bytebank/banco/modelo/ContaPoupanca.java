package br.com.bytebank.banco.modelo;

public class ContaPoupanca extends Conta {

	public ContaPoupanca(int agencia, int numero) {
		super(agencia, numero);
		System.out.println("criando uma conta poupança");
	}

	@Override
	public void deposita(double valor) {
		super.saldo += valor;
	}
	
}
