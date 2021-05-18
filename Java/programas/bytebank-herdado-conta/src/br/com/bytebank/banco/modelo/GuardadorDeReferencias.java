package br.com.bytebank.banco.modelo;

public class GuardadorDeReferencias {

	private Object[] referencias;
	private int ultimaPosicao;
	
	public GuardadorDeReferencias() {
		this.referencias = new Conta[10];
		this.ultimaPosicao = 0;  /*não é necessario, logo que a variavel 
									já se inicia com um valor padrao 0 */
		
	}
	
	public void adiciona(Object ref) {
		this.referencias[this.ultimaPosicao] = ref;
		this.ultimaPosicao++;
		
	}

	public int getTamanhoDoGuardador() {
		return this.ultimaPosicao;
	}

	public Object getReferencia(int pos) {
		return this.referencias[pos];
	}
	
}
