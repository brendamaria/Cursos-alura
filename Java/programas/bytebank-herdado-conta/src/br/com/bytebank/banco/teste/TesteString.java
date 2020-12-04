package br.com.bytebank.banco.teste;

public class TesteString {

	public static void main(String[] args) {
		
		String nome = "Mario";
		String outroNome = new String("Alura");
		
		String novo = outroNome.replace("A", "a");
		System.out.println(novo);
		
		String novoN = outroNome.toUpperCase();
		System.out.println(novoN);
	
		char c = nome.charAt(3); 
		System.out.println(c);

		int pos = nome.indexOf("rio");
		System.out.println(pos);

		String sub = nome.substring(1);
		System.out.println(sub);
		
		for(int i = 0; i < nome.length(); i++) {
		    System.out.println(nome.charAt(i));
		} 
		
	}

}
