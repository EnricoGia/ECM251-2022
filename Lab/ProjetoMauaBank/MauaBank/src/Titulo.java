import java.time.LocalDate;

public class Titulo {
    private double valor;
    private LocalDate data;
    private double multaDiaria;


    public Titulo(double valor,LocalDate data, double multaDiaria){
        this.valor = valor;
        this.data = data;
        this.multaDiaria = multaDiaria;

    }


    public double getValor() {
        return valor;
    }


    public double getMultaDiaria() {
        return multaDiaria;
    }


    public LocalDate getData() {
        return data;
    }


}
