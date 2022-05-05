public class Lagarto extends Jogada {

    public Lagarto() {
        super(EnumJogadas.SPOCK, EnumJogadas.PAPEL);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.LAGARTO;
    }
}
