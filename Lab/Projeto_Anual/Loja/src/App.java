package Loja.src;

public class App {
    public static void main(String[] args) throws Exception {
        
        Conta conta1 = new Conta("Isaac", 48, "janea.nitzsc@hotmail.com", "Brasil");
        Usuario usuario1 = new Usuario("Sac");

        conta1.setUsuario(usuario1);

        Jogo jogo1 = new Jogo("Castlevania", "Um clássico dos jogos 2D", 50.0);
        Jogo jogo2 = new Jogo("Metroid", "Um clássico dos jogos 2D", 20.0);

        usuario1.escreveReview(true, "Muito bom", jogo1);
        conta1.getUsuario().escreveReview(true, "Legal", jogo2);

        jogo1.adicionaTipo("Metroidvania");
        jogo1.adicionaTipo("Ação");
        jogo1.adicionaTipo("Plataforma");

        jogo2.adicionaTipo("Metroidvania");
        jogo2.adicionaTipo("Ação");
        jogo2.adicionaTipo("Plataforma");
       
        jogo1.mostraTipo();

        jogo1.mostraReview();
        jogo2.mostraReview();



        
    }
}
