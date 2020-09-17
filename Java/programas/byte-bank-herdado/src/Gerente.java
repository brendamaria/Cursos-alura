
public class Gerente extends Funcionario implements Autenticavel {
	
	private AutenticacaoUtil autentificador;
    
    public Gerente() {
    	this.autentificador = new AutenticacaoUtil();
    }
    
	@Override
	public double getBonificacao(){
		return this.getSalario() + 500;
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
