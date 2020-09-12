
public class SistemaInterno {

	private int senha = 2222;
	
	public void autentica(Autenticavel aa){
		
		boolean autenticou = aa.autentica(this.senha);
		
		if(autenticou) {
			System.out.println("Pode entrar no sistema.");
		
		}else {
			System.out.println("Não pode entrar no sistema.");
		}
		
	}
	
}
