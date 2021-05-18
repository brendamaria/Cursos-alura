package br.com.bytebank.banco.teste.util;

import java.util.ArrayList;

import br.com.bytebank.banco.modelo.*;

public class Teste {
	public static void main(String[] args) {
		
		ArrayList lista = new ArrayList();
		
        Conta cc = new ContaCorrente(22, 11);
        lista.add(cc);

        Conta cc2 = new ContaCorrente(22, 22);
        lista.add(cc2); // adicionar na lista 

        System.out.println("Tamanho: " + lista.size());

        Conta ref = (Conta) lista.get(0);
        System.out.println(ref.getNumero());

        lista.remove(0); // remover da lista por um indice 
        
        System.out.println("Tamanho: " + lista.size()); // retorna o tamanho da lista 

        Conta cc3 = new ContaCorrente(33, 311);
        lista.add(cc3);

        Conta cc4 = new ContaCorrente(33, 322);
        lista.add(cc4);
        
        for(int i = 0; i < lista.size(); i++) { // varrer array
        	Object oRef = lista.get(i);
        	System.out.println(oRef);
        }
        
        for(Object oRef : lista) { // forma mais simples para varrer o array (para cada 
        							//		objeto oRef dentro de lista ele imprime(sysout	))
        	System.out.println(oRef); 
        }
        
        
	}
}
