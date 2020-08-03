
public class Teste {
	
	public static void main(String[] args) {
		
		Conta conta = new Conta();
		
		
		Cliente marcela = new Cliente();
		
		marcela.setNome("marcela"); 
		
		conta.setTitular(marcela);
		
		System.out.println(marcela.getNome());
		
		System.out.println(marcela);
		System.out.println(conta.getTitular());
		
	}
	
	

}
