package Loja.src;

public class Conta {
    private String nome;
    private Integer idade;
    private String email;
    private Float saldo = 0.0f;
    private String pais;
    private String telefone = null;
    private Usuario usuario = null;

    public Conta(String nome, Integer idade, String email, String pais) {
        this.nome = nome;
        this.idade = idade;
        this.email = email;
        this.pais = pais;
    }


    public void setUsuario(Usuario usuario){
        this.usuario = usuario;
    }

    public Usuario getUsuario(){
        return this.usuario;
    }
    
 }


