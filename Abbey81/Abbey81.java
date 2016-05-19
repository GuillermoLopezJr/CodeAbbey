import java.util.Scanner;

public class Abbey81{

	public static void main(String[] args){
		Scanner kbd = new Scanner(System.in);	
		
		System.out.println("input: ");
		int size = kbd.nextInt();
		String binNums[] = new String[size];
		kbd.nextLine();	//get rid of /n

		for(int i = 0; i < size; i++){
			int num = kbd.nextInt();
			String bin = Integer.toBinaryString(num);
			binNums[i] = appendZeroes(bin);
		}

		System.out.println("\nanswer: ");
		for(int i = 0; i < size; i++){
			int count = getOneCount(binNums[i]);
			System.out.print(count + " ");
		}
	}
	
	//adds zeroes if needed to make binary num 32 bit.
	public static String appendZeroes(String bin){
		String zeroes = "";

		for (int i = 0; i < 32-(bin.length()); i++){
			zeroes += "0";
		}

		return (zeroes + bin);
	}

	public static int getOneCount(String bin){
		int binCount = 0;

		for(int i = 0; i < bin.length(); i++){
			if(bin.charAt(i) == '1'){
				binCount++;
			}
		}
		return binCount;
	}
}
