
public class Administrador extends Funcionario implements Autenticavel {
	
	private AutenticacaoUtil autentificador;
    
    public Administrador() {
    	this.autentificador = new AutenticacaoUtil();
    
    }

	@Override
	public double getBonificacao() {
		return this.getSalario() + 50;
	}

	@Override
	public void setSenha(int senha) {
        this.autentificador.setSenha(senha);
	}

	@Override
	public boolean autentica(int senha) {
    	return this.autentificador.autentica(senha);
	}

}
