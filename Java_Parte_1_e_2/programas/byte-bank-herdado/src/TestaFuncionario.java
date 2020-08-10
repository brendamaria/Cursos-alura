
public class TestaFuncionario {
	public static void main(String[] args) {
		Funcionario nico = new Funcionario();
		
		nico.setCpf("934754632-22");
		nico.setNome("Nico");
		nico.setSalario(1000);
		
		System.out.println(nico.getNome());
		System.out.println(nico.getBonificacao());
		
		
	}
}
