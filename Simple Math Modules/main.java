import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        Modules modules = new Modules();
        //modules.Check_Factors(12);
        int[] xlist = {10,0,3,2};
        //modules.GetMinimum(xlist);
        modules.Factors_Of_Polynomial(1,12,20);
    }
}

import java.util.ArrayList;

public class Modules {
    public void Check_if_even(int x){
        if (x%2==0){
            System.out.println(true);
        }
        else{
            System.out.println(false);
        }
    }


   public void Check_Factors(int x){
    String lst = " ";
    for(int i=1; i<=x;i++){
        if (x%i==0){
            lst += i+" ";
        }
    }
    System.out.println(lst);}

public void GetMaximun(int[] xlist){
    int max = 0;
    for (int i:xlist){
        if(i>max){
            max = i;
        }
    }
    System.out.println(max);
}
public void GetMinimum(int[] xlist){
    int Min = xlist[0];
    for (int i:xlist){
        if(i<Min){
            Min = i;
        }
    }
    System.out.println(Min);
}
public void ReverseList(ArrayList<Integer> xlist){
    for (int k = 0, j = xlist.size() - 1; k < j; k++){
        xlist.add(k, xlist.remove(j));
    }
    System.out.println(xlist);  
}
public void Factors_Of_Polynomial(int a, int b, int c){
    int descriminant = (int) (Math.pow(b, 2)-4*a*c);
    if(descriminant>=0){
        System.out.println((-(b)+ Math.sqrt(Math.abs(descriminant)))/2);
        System.out.println((-(b)- Math.sqrt(Math.abs(descriminant)))/2);
        }
    else{
        System.out.println("Not Factorable! ");
    }

}}
