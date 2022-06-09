public class BigBrothers extends Membro {

    public BigBrothers(String usuario, String email) {
        super(usuario, email,"BigBrothers");
        
    }

    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno()?"Sempre ajudando as pessoas membros ou não S2!":"...";
        System.out.println(mensagem + "\n" + assinatura + "\n");
    }
    
}
