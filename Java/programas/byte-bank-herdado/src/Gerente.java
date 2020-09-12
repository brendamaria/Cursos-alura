
public class Gerente extends Funcionario implements Autenticavel {
	
	private int senha;
	
	@Override
	public double getBonificacao(){
		return this.getSalario() + 500;
	}
	
	public boolean autentica(int senha) {
		if(this.senha == senha) {
			return true;
		}
		return false;
	}

	public int getSenha() {
		return senha;
	}

	public void setSenha(int senha) {
		this.senha = senha;
	}
	

	
}
