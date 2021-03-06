package oving3;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

public class Ordbok{

    public static Node bygg(String[] ordliste){
        // SKRIV DIN KODE HER
    	return new Node();
    }

    public static ArrayList posisjoner(String ord, int index, Node currentNode){
        // SKRIV DIN KODE HER
    	return new ArrayList();
    }


    public static void main(String[]  args){
        try{
            BufferedReader in;
            if (args.length > 0) {
                try {
                    in = new BufferedReader(new FileReader(args[0]));
                }
                catch (FileNotFoundException e) {
                    System.out.println("Kunne ikke �pne filen " + args[0]);
                    return;
                }
            }
            else {
                in = new BufferedReader(new InputStreamReader(System.in));
            }
            StringTokenizer st = new StringTokenizer(in.readLine());
            String[] ord = new String[st.countTokens()];
            int i=0;
            while(st.hasMoreTokens()) ord[i++]=st.nextToken();
            Node rotNode = bygg(ord);
            String sokeord= in.readLine();
            while(sokeord!=null){
                sokeord=sokeord.trim();
                System.out.print(sokeord+":");
                ArrayList pos = posisjoner(sokeord, 0, rotNode);
                int[] posi = new int[pos.size()];
                for(i=0;i<posi.length;i++)posi[i]=((Integer)pos.get(i)).intValue();
                Arrays.sort(posi);
                for(i=0;i<posi.length;i++) System.out.print(" "+posi[i]);
                System.out.println();
                sokeord=in.readLine();
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}

class Node{
    public ArrayList posisjoner;
    public HashMap barn;

    public Node(){
        posisjoner=new ArrayList();
        barn=new HashMap();
    }
}
