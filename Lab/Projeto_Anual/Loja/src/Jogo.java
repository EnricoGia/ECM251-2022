package Loja.src;

import java.util.*;

public class Jogo {
    private String nome;
    private String descricao;
    private double preco;
    private ArrayList<String> tipos;
    private ArrayList<Review> reviews;

    public Jogo(String nome, String descricao, double preco) {
        this.nome = nome;
        this.descricao = descricao;
        this.preco = preco;
        this.tipos = new ArrayList<String>();
        this.reviews = new ArrayList<Review>();
    }

    public String getNome() {
        return nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public ArrayList<String> getTipos() {
        return tipos;
    }

    public void adicionaTipo(String tipo) {
        this.tipos.add(tipo);
    }
    
    public void adicionaReview(Review review) {
        this.reviews.add(review);
    }

    public void mostraTipo() {
        this.ordenaTipo();
        System.out.print(this.getNome() + " é um jogo do tipo :");
        for (String t : this.tipos) {
            System.out.print(" " + t + ";");
        }
    }

    public void mostraReview() {
        System.out.print("\n\n" + this.getNome() + " tem as seguintes reviews :");
        for (Review t : this.reviews) {

            System.out.print(" " + t + " ");
        }
    }

    public void ordenaTipo() {
        Collections.sort(this.tipos);
    }


    @Override
    public String toString() {
        return "Jogo [nome = " + nome + ", descricao = " + descricao + ", preco = " + preco + ", tipo = " + tipos + "]";
    }
}
