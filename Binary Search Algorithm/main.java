
public class App{

    public static void main(String[] args){
        int[] xlist = {1,2,3,4,5,6,7,8,9,0};
        int item = 2;
        Binary_Search_Algorithm search = new Binary_Search_Algorithm(xlist, item);
        search.Binary();
    }
}

public class Binary_Search_Algorithm {
    private int[] sequence;
    private int item;
    
    
    public Binary_Search_Algorithm(int[] sequence, int item){
        this.sequence = sequence;
        this.item = item;
    }
    public void Binary(){
        long start_time = System.currentTimeMillis();

        int begin_index = 0;
        int end_index = this.sequence.length-1;
        
        while (begin_index<=end_index){
           
            int midpoint = begin_index + (end_index -begin_index)/2;
            int midpoint_value = sequence[(int)midpoint];

            if(midpoint_value == this.item){
                System.out.println("Found at the index: "+ (midpoint));
                break;
            }
            else if(midpoint_value<item){
                begin_index = midpoint-1;
            }
            else{
                end_index = midpoint+1;
            }
            
        }
        long end_time = System.currentTimeMillis();
        long elapsed_time = end_time-start_time;
        System.out.println("Time elapsed: " + elapsed_time + " seconds");
    }
}
