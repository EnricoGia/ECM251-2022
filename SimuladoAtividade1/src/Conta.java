public class Conta {
    private Usuario usuario;
    private int id;
    private double saldo;
    private static int idAtual = 1;

    public Conta(Usuario usuario, double saldo) {
        this.usuario = usuario;
        this.id = Conta.idAtual;
        this.saldo = saldo;
        Conta.idAtual++;
    }

    public String toString() {
        return ("Usuario: " + this.usuario.getNome() + "\nID: " + this.id + "\nSaldo: " + this.saldo + "\n");
    }

    public int getId() {
        return this.id;
    }

    public Usuario getUsuario() {
        return this.usuario;
    }
}
