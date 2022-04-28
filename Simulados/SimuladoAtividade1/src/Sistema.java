public class Sistema {

    public void run() {

        Usuario u1 = new Usuario("Testando", "test123", "Teste@gmail.com");
        System.out.println(u1);

        Conta c1 = new Conta(u1, 200);
        System.out.println(c1);

        Conta c2 = new Conta(u1, 300);
        System.out.println(c2);

        System.out.println(Transacao.gerarQRCode(400, c1));
    }

    public void pagarQRCode(Usuario usuario){
        


    }
}
