package br.com.bytebank.banco.teste;

import br.com.bytebank.banco.modelo.Conta;
import br.com.bytebank.banco.modelo.ContaCorrente;

public class TesteBiblioteca {

    public static void main(String[] args) {
        Conta c = new ContaCorrente(123, 321);
    }
}
