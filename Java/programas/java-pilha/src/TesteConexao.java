
public class TesteConexao {

	public static void main(String[] args) {
		
		try(Conexao con = new Conexao()){
			con.leDados();
		} catch(IllegalStateException ex) {
			System.out.println("Deu erro na conexao");
		}
		// o finally fica oculto por causa da implementacao do 
		//AutoCloseable usando o metodo close() ele é
		//automaticamente implementado 
		
		
// ---------------------------------------------		
		
		
//		Conexao con = null;
//		try {
//			con = new Conexao();
//			con.leDados();
//			con.fecha();
//		
//		} catch(IllegalStateException ex) {
//			System.out.println("deu erro na conexao ");
//		} finally {
//			con.fecha();
//		}
		
	}

}
