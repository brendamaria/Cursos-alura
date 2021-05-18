package br.com.bytebank.banco.teste;

import br.com.bytebank.banco.modelo.Conta;
import br.com.bytebank.banco.modelo.ContaCorrente;
import br.com.bytebank.banco.modelo.GuardadorDeReferencias;

public class TesteReferencias {
	public static void main(String[] args) {
		GuardadorDeReferencias guardador = new GuardadorDeReferencias();
		
		Conta cc = new ContaCorrente(22, 11);
		Conta cc2 = new ContaCorrente(22, 22);
		
		guardador.adiciona(cc);
		guardador.adiciona(cc2);
		
		int tamanho = guardador.getTamanhoDoGuardador();
		System.out.println(tamanho);
		
		Conta ref = (Conta) guardador.getReferencia(1);
		System.out.println(ref.getNumero());
		
		
	}

}
