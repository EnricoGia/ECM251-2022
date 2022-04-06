public class Usuario {
    private String nome;
    private String senha;
    private String email;

    public Usuario(String nome, String senha, String email) {
        this.nome = nome;
        this.senha = senha;
        this.email = email;

    }

    public String toString() {
        return ("Nome: " + this.nome + "\nSenha: " + this.senha + "\nEmail: " + this.email + "\n");
    }

    public String getNome() {
        return this.nome;
    }

}
