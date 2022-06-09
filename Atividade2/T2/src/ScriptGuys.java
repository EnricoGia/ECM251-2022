public class ScriptGuys extends Membro {

    public ScriptGuys(String usuario, String email) {
        super(usuario, email, "ScriptGuys");
        
    }
    
    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno()?"Prazer em ajudar novos amigos de código!":"QU3Ro_S3us_r3curs0s.py";
        System.out.println(mensagem + "\n" + assinatura + "\n");
    }
    
}
