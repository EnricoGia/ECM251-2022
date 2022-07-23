package Loja.src;

public class Review {
    Usuario usuario;
    boolean recomendacao;
    String texto;
    

    public Review(Usuario usuario, boolean recomendacao, String texto) {
        this.usuario = usuario;
        this.recomendacao = recomendacao;
        this.texto = texto;
    }

    public String toString() {
        return ("\n\nUsuário: " + usuario.getNickname() +
                "\nRecomenda: " + this.recomenda2String() +
                "\n" + this.texto);
    }

    public String recomenda2String() {
        return (this.recomendacao) ? "Sim" : "Não";
    }
}
