package br.com.bytebank.banco.teste;

import br.com.bytebank.banco.modelo.*;

public class TesteArrayReferencias {

	public static void main(String[] args) {
		
		Conta[] contas = new Conta[5];
		
		ContaCorrente contaC = new ContaCorrente(01, 01);
		ContaPoupanca contaP = new ContaPoupanca(01, 02);
		
		contas[0] = contaC;
		contas[1] = contaP;
		
		System.out.println(contas[0].getNumero());
		
		ContaCorrente ref = (ContaCorrente) contas[0];
		
		System.out.println(ref.getNumero());
		
	}
	
}
