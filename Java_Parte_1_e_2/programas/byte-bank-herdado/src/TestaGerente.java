
public class TestaGerente {

	public static void main(String[] args) {
		
		Gerente gerente = new Gerente();
		
		gerente.setNome("Nico");
		gerente.setCpf("439283475-22");
		gerente.setSalario(1500);

		System.out.println(gerente.getNome());
		System.out.println(gerente.getCpf());
		System.out.println(gerente.getSalario());
		
		gerente.setSenha(2222);
		
		boolean autentica = gerente.autentica(2222);  
		
		System.out.println(autentica);

	}
}
