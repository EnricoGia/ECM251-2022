// Enrico Giannobile 19.00610-0

import java.util.concurrent.ThreadLocalRandom;

public class Veiculo {

    private int id;
    private String tipo;

    public Veiculo() {
        this.id = ThreadLocalRandom.current().nextInt(10000, 99999); // Gera um inteiro aleatório de 10000 à 99999

    }

    public void testar() { // Imprime as informações do veículo
        System.out.println("id = " + this.getId());
        System.out.println("tipo = " + this.getTipo());
        System.out.println();
    }

    public String getTipo() {
        return tipo;
    }

    protected void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

}
