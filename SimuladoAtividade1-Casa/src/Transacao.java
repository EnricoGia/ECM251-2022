public class Transacao {

    public static String gerarQRCode(double valor, Conta conta) {
        String n = conta.getUsuario().getNome().toUpperCase();

        return (Integer.toString(conta.getId()) + ";" + n + ";" + String.valueOf(valor));
    }

}
