
public class TesteReferencia {

	public static void main(String[] args) {
		
		Gerente g1 = new Gerente();
		g1.setNome("Marcos");
		g1.setSalario(5000.0);
		
		EditorDeVideo ev = new EditorDeVideo();
		ev.setSalario(2500.0);
		
		Designer d = new Designer();
		d.setSalario(2000.0);
		
		ControleBonificacao controle = new ControleBonificacao();
		controle.registra(g1);
		controle.registra(ev);
		controle.registra(d);
		
		System.out.println(g1.getBonificacao());
		System.out.println(ev.getBonificacao());
		System.out.println(d.getBonificacao());

		
		
		System.out.println(controle.getSoma());
				
	}
}
