public class Papel extends Jogada {

    public Papel() {
        super(EnumJogadas.PEDRA,EnumJogadas.SPOCK);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.PAPEL;
    }
      }