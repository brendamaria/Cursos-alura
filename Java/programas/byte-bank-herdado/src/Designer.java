
public class Designer extends Funcionario {
	
	@Override
	public double getBonificacao() {
		return this.getSalario() + 150;
	}
}
