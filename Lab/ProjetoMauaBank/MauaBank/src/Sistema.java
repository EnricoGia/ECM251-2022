import java.time.LocalDate;

public class Sistema{

    public void run(){
        Cliente cliente = new Cliente("Mcree","123456","cole@gmail.com");

        Conta conta = new Conta(cliente, 1234);

        Titulo steam = new Titulo(200,LocalDate.of(2022,03,25),5);

        conta.depositar(300);

        System.out.println(conta);

        pagarTitulo(steam,conta);

        System.out.println(conta);
    }

    public boolean pagarTitulo(Titulo titulo, Conta conta){
        double valorPagar;
        LocalDate dataTitulo = titulo.getData();
        LocalDate hoje = LocalDate.now();

        if (dataTitulo.compareTo(hoje)>=0){
            valorPagar = titulo.getValor();

        }
        else{
            //Calcula o valor a pagar baseado na multaDiaria do título
            valorPagar = titulo.getValor()-
            titulo.getValor()*dataTitulo.compareTo(hoje)*
            titulo.getMultaDiaria()/100;
        }

        if(conta.sacar(valorPagar))
            System.out.println("Título pago");
        else
            System.out.println("Saldo insuficiente");

        return true;

    }
}