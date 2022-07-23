package Loja.src;

public class App {
    public static void main(String[] args) throws Exception {
        

        Usuario user1 = new Usuario("José", 22,"JGames",22.3f);
        Jogo jogo1 = new Jogo("Castlevania", "Um clássico dos jogos 2D", 50.0);

        Usuario user2 = new Usuario("Luigi", 22,"LL__",22.3f);
        Jogo jogo2 = new Jogo("Metroid", "Um clássico dos jogos 2D", 20.0);

        jogo1.adicionaTipo("Metroidvania");
        jogo1.adicionaTipo("Ação");
        jogo1.adicionaTipo("Plataforma");

        jogo2.adicionaTipo("Metroidvania");
        jogo2.adicionaTipo("Ação");
        jogo2.adicionaTipo("Plataforma");
       
        jogo1.mostraTipo();
        
        user1.escreveReview(true, "Muito Bom", jogo1);
        user2.escreveReview(true, "Maneiro", jogo2);

        jogo1.mostraReview();
        jogo2.mostraReview();



        
    }
}
