
public class EditorDeVideo extends Funcionario {
	
	public double getBonificacao() {
		System.out.println("chamando bonificacao do editor de video");
		return super.getBonificacao() + 200;
	}
}



