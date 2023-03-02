import javax.swing.JFrame;

public class Ventana{
	public static void main(String args[]){
		Ventana ventana = new Ventana("Ventana en Java");
	}
	public Ventana(String titulo){
		JFrame ventanaM = new JFrame(titulo);

		ventanaM.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		ventanaM.setSize(290,150);
		ventanaM.setResizable(false);
		ventanaM.setVisible(true);
	}
}
