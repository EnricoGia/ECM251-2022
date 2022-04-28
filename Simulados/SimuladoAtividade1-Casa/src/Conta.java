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

    public double getSaldo() {
        return this.saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void pagarQRCode(Conta conta1, Conta conta2, String dados) {
        String d[] = dados.split(";");

        int id = Integer.parseInt(d[0]);
        String usuario = d[1];
        double valor = Double.parseDouble(d[2]);

        String usuarioc2 = conta2.getUsuario().getNome().toUpperCase();

        if (usuario.equals(usuarioc2) && id == conta2.getId()) {
            if (conta1.getSaldo() - valor >= 0) {
                conta1.setSaldo(conta1.getSaldo() - valor);
                conta2.setSaldo(conta2.getSaldo() + valor);
            }
            else
                System.out.println("Saldo insuficiente");
        } else
            System.out.println("Usuario ou Id inválidos");

    }
}
