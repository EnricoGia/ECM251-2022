// Enrico Giannobile 19.00610-0

final class Aplicacao {

    static void rodar() {
        System.out.println("---- INICIALIZANDO APLICAÇÃO ----");
        System.out.println();

        Usuario usuario = new Usuario("SudoAdmin123");

        System.out.println("----- VEÍCULOS DISPONÍVEIS -----");
        System.out.println();

        Moto m1 = new Moto();
        m1.testar();

        Bicicleta b1 = new Bicicleta();
        b1.testar();

        Carro c1 = new Carro();
        c1.testar();

        Patinete p1 = new Patinete();
        p1.testar();

        System.out.println("---------------------------------");
        System.out.println();
        System.out.println("--- USUÁRIO TESTANDO VEÍCULOS ---");
        System.out.println();

        usuario.trocaVeiculo(m1);
        usuario.testar();

        usuario.trocaVeiculo(b1);
        usuario.testar();

        usuario.trocaVeiculo(c1);
        usuario.testar();

        usuario.trocaVeiculo(p1);
        usuario.testar();

        System.out.println("-----> FINALIZANDO APLICAÇÃO");
        System.out.println();

    }

}
