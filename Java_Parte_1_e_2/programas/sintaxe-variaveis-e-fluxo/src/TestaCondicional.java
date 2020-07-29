
public class TestaCondicional {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");
		int idade = 16;
		int quantidadePessoas = 3;
		
		if (idade >= 18) {
			System.out.println("Você tem mais que 18");
			System.out.println("Seja bem vindo");
		} else {
			if (quantidadePessoas >= 2) {
                System.out.println("voce não tem 18, mas pode entrar, pois está acompanhado");
			} else {
				System.out.println("Infelizmente você não pode entrar");
			}
		} 
		
		
	}

}
