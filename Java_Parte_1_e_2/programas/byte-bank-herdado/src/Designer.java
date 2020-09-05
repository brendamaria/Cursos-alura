
public class Designer extends Funcionario {
	
	public double getBonificacao() {
		System.out.println("chamando bonificacao do designer");
		return super.getBonificacao() + 150;
	}
}
