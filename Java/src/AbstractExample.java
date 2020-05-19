public class AbstractExample {
    public static void main(String[] args){
        PersegiPanjang persegipanjang = new PersegiPanjang();
        Lingkaran lingkaran = new Lingkaran();


        persegipanjang.getKeliling();
        lingkaran.getLuas();
    }
}
abstract class BangunRuang {

    public abstract void getLuas();

    public abstract void getKeliling();
}

class Lingkaran extends BangunRuang{
    public double r = 7;
    public double phi = 3.14;

    public void getLuas(){
        System.out.println("Luas : " + (phi * r * r));
    }

    public void getKeliling(){
        System.out.println("Keliling : ");
    }
}

class PersegiPanjang extends BangunRuang{
    public float p = 7;
    public float l = 4;

    public void getLuas(){
        System.out.println("Luas : ");
    }

    public void getKeliling(){
        System.out.println("Keliling : "+ (2 * p + 2 * l));
    }

}


