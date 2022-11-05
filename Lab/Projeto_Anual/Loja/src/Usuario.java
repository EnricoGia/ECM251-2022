package Loja.src;

public class Usuario {
    private String nickname;
    
    
    public Usuario(String nickname) {
        this.nickname = nickname; 
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public void escreveReview(boolean recomendacao, String texto, Jogo jogo){
        Review review = new Review(this, recomendacao,texto);
        jogo.adicionaReview(review);
    }

}
