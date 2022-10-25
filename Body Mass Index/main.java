
public class App {
    public static void main(String[] args) throws Exception {
        BMI person1 = new BMI(100, 1.98f);
        System.out.println(person1.GetBMI());
    }
}



public class BMI {
    private float weight;
    private float heigth;
    public BMI(float weight, float heigth){
        this.heigth = heigth;
        this.weight = weight;
    }
    public float GetBMI(){
        float bmi = (float) (this.weight/Math.pow(heigth, 2.0f));
        return bmi;
        
    }
    
}
