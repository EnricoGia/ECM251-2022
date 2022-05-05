public class Jogada {
    private EnumJogadas[] venco = new EnumJogadas[2];
    
    public Jogada(EnumJogadas venco, EnumJogadas venco2) {
        this.venco[0] = venco;
        this.venco[1] = venco2;
    }

    public boolean verificarVenceu(Jogada jogada){
        if(jogada.getTipo().equals(venco[1]) || jogada.getTipo().equals(venco[0]))
            return true;
        return false;
    }

    public EnumJogadas getTipo(){
        return EnumJogadas.PAPEL;
    }
}
