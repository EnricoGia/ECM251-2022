package Loja.src;

public class Usuario {
    private String nome;
    private int idade;
    private String nickname;
    private float saldo;
    
    public Usuario(String nome, int idade, String nickname, float saldo) {
        this.nome = nome;
        this.idade = idade;
        this.nickname = nickname;
        this.saldo = saldo;
    }

    public void escreveReview(boolean recomendacao, String texto, Jogo jogo){
        Review review = new Review(this,recomendacao,texto);
        jogo.adicionaReview(review);
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    @Override
    public String toString() {
        return "Usuario [idade=" + idade + ", nickname=" + nickname + ", nome=" + nome + ", saldo=" + saldo + "]";
    }
}
