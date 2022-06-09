public class HeavyLifters extends Membro {

    public HeavyLifters(String usuario, String email) {
        super(usuario, email, "HeavyLifters");
        
    }

    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno()?"Podem contar conosco!":"N00b_qu3_n_Se_r3pita.bat";
        System.out.println(mensagem + "\n" + assinatura + "\n" );
    }
}
