public class MobileMembers extends Membro{
    
    public MobileMembers(String usuario, String email) {
        super(usuario, email, "MobileMembers");
        
    }

    @Override
    public void postarMensagem(String mensagem){
        String assinatura = Sistema.getTurno()?"Happy Coding!":"Happy_C0d1ng. Maskers";
        System.out.println(mensagem + "\n" + assinatura + "\n" );
    }

}
