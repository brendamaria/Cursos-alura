
public class TesteIR {
	public static void main(String[] args) {

        double salario = 3300.0;
        //De 1900.0 até 2800.0, o IR é de 7.5% e 
        //pode deduzir na declaração o valor de R$ 142


        if (salario >= 1900.0 && salario <= 2800.0) {
        	System.out.println("a sua aliquota é de 7.5%");
        	System.out.println("pode deduzir na declaração até R$ 142");
        }else if(salario >= 2800.0 && salario <= 3751.0){
        	System.out.println("a sua aliquota é de 15%");
        	System.out.println("pode deduzir na declaração até R$ 350");
        }else if(salario >= 3751.0 && salario <= 4664.00) {
        	System.out.println("a sua alioquota é de 22.5%");
        	System.out.println("pode deduzir na declaração até R$ 636");
        }
        
    }

}
