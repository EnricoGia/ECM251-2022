public class Spock extends Jogada {

    public Spock() {
        super(EnumJogadas.PEDRA, EnumJogadas.TESOURA);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.SPOCK;
    }
}
