
public class Teste {
	
	public static void main(String[] args) {
		
		Conta conta = new Conta(123, 456);
		Conta conta2 = new Conta(532, 837);
		
		
		Cliente marcela = new Cliente();
		Cliente paulo = new Cliente();
		
		
		marcela.setNome("Marcela"); 
		conta.setTitular(marcela);
		
		
		
		paulo.setNome("Paulo");
		conta2.setTitular(paulo);
		
		System.out.println(marcela.getNome());
		System.out.println(paulo.getNome());
		
		System.out.println(Conta.getTotal());
		
	}
	
	

}
