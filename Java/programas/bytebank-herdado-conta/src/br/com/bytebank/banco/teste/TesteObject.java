package br.com.bytebank.banco.teste;

public class TesteObject {
	
	public static void main(String[] args) {
		
		int[] idades = new int[5];
		
		idades[0] = 29;
		idades[1] = 43;
		idades[2] = 23;
		idades[3] = 54;
		idades[4] = 12;
		
		int idade4 = idades[3];
		
		System.out.println(idade4);
		System.out.println(idades.length);
		
		int[] num = new int[5];
		
		for(int i = 0; i < num.length; i++) {
			num[i] = i * i;
		}
		
		for(int i = 0; i < num.length; i++) {
			System.out.println(num[i]);
		}
		
		
		
		
	}
	
}
