import java.util.ArrayList;
import java.util.List;

final class Sistema {
    private static boolean turno = true;
    private static List<Membro> membros;

    static void run() {
        System.out.println("Bem vindo, Membro!\n");

        membros = new ArrayList<Membro>();
        membros.add(new BigBrothers("Bus", "Bus123@gmail.com"));
        membros.add(new HeavyLifters("Hus", "Hus123@gmail.com"));
        membros.add(new MobileMembers("Mus", "Mus123@gmail.com"));
        membros.add(new ScriptGuys("Sus", "Sus123@gmail.com"));

        Sistema.papoDeMembros("Estou Trabalhando...");
        
        Sistema.trocarTurno();

        Sistema.papoDeMembros("3st0u H4ck34nd0...");

        Sistema.trocarTurno();

        membros.remove(1);
        membros.remove(2);

        Sistema.papoDeMembros("Estou Trabalhando...");

        System.out.println("\nSistema Encerrado...");
    }

    public static boolean getTurno() {
        return turno;
    }

    public static void setTurno(boolean turno) {
        Sistema.turno = turno;
    }

    public static void trocarTurno() {
        boolean proximoTurno = Sistema.getTurno() ? false : true;
        Sistema.setTurno(proximoTurno);
        System.out.println(getTurno()?"Horário regular!" : "Horário extra!");
        System.out.println("\n");
    }
    public static void papoDeMembros(String mensagem){
        for(Membro membro : Sistema.membros){
            membro.postarMensagem(mensagem);
        }
        
    }


}
