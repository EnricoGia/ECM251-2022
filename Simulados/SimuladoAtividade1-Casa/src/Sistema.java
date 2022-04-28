public class Sistema {

    public void run() {

        Usuario u1 = new Usuario("Testando", "test123", "Teste@gmail.com");
        Usuario u2 = new Usuario("All Might","allllll", "arumaito@gmail.com");
        Usuario u3 = new Usuario("Usuario3", "boring123","boringcompany@gmail.com");

        Conta c1 = new Conta(u1, 1000);
        System.out.println(c1);

        Conta c2 = new Conta(u2, 250);
        System.out.println(c2);

        Conta c3 = new Conta(u3, 3000);
        System.out.println(c3);
        
        String t1 = Transacao.gerarQRCode(250,c1);

        c2.pagarQRCode(c2, c1, t1);
        c3.pagarQRCode(c3, c1 ,t1);
        c2.pagarQRCode(c2, c1, t1);

        String t2 = Transacao.gerarQRCode(1000, c2);

        c3.pagarQRCode(c3, c2, t2);

        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);
    }

    
}
