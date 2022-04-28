// Enrico Giannobile 19.00610-0

public class Usuario {
    private String nome;
    private Veiculo veiculo;

    public Usuario(String nome) {
        this.nome = nome;
    }

    public void testar() { // Imprime as informações do veículo do usuário
        System.out.println("id = " + this.getVeiculo().getId());
        System.out.println("tipo = " + this.getVeiculo().getTipo());
        System.out.println();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Veiculo getVeiculo() {
        return veiculo;
    }

    public void trocaVeiculo(Veiculo veiculo) {
        this.veiculo = veiculo;
    }

}
