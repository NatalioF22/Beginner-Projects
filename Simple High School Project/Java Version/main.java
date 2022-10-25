import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        ArrayList<String> courses_name = new ArrayList<String>();
        courses_name.add("Math");
        courses_name.add("English");
        courses_name.add("CS");
        courses_name.add("Chemistry");
        courses_name.add("Portuguese");

        float[] grades = {100,100,100,0};

        Student student1 = new Student("Natalio", "Fernandes", "Cape Verdean", 'M', 19, "BSU", courses_name, grades);
        student1.Get_Courses_list();
        System.out.println(student1.Get_Age());
        System.out.println(student1.Get_Full_Name());
        System.out.println(student1.Get_GPA());
        System.out.println(student1.Get_Nationality());
        System.out.println(student1.Get_Gender());

        System.out.println("Teachers info ");

        Teacher Teacher1 = new Teacher("Anna", "Antunes", "French", 'F', 39, "BSU", 80000,student1);
        System.out.println(Teacher1.GetStudents());
       
        
    

    
    }
}

import java.util.ArrayList;

public abstract class School {
    public School(){}
    protected String f_name;
    protected String l_name;
    protected String nationality;
    protected char gender;
    protected int age;
    protected String School_Name;
    protected String type;
    //Speciffically for Teachers
    protected double raise_amount = 1.05;
    protected float Salary;
    //Speciffically for Students
    protected ArrayList<String> courses;
    protected String Course1;
    protected String Course2;
    protected String Course3;
    protected String Course4;
    protected String Course5;
    protected float[] grades;
    protected double GPA;

    public abstract String Get_Full_Name();
    public abstract String Get_Nationality();
    public abstract char Get_Gender();
    public abstract int Get_Age();
    public abstract String Get_email();
   
    

   
}

import java.util.ArrayList;


public class Student extends School {
    
    public Student(String f_name,String l_name, String nationality, char gender, int age, String School_Name, ArrayList<String> courses,float[] grades){
        this.f_name = f_name;
        this.l_name = l_name;
        this.nationality = nationality;
        this.gender = gender;
        this.age = age;
        this.School_Name = School_Name;
        this.courses = courses;
        this.grades = grades;
        this.type = "Student";

    }
    @Override
    public String Get_Full_Name(){
        return this.f_name + " " + this.l_name;
    }
    @Override
    public String Get_Nationality(){
        return this.nationality;
    }
    @Override
    public char Get_Gender(){
        return this.gender;
    }
    @Override
    public int Get_Age(){
        return this.age;
    }
    @Override
    public String Get_email(){
        return  this.l_name.charAt(0)+"." + this.f_name + "@"+this.School_Name+"."+this.type+".edu";
    }

    public void Get_Courses_list(){
        System.out.println("Courses List: ");
        for (int i=0;i<courses.size();i++){
            System.out.println(courses.get(i));
        }
        
    }

    public double Get_GPA(){
        
        double total = 0;
        for (int i =0 ; i<this.grades.length;i++){
            total += grades[i];
        }
        double gpa = (total * 4) / grades.length/100;

        return +gpa;
    }
    
    
}




public class Teacher extends School {

    private Student students;
    public Teacher(String f_name,String l_name, String nationality, char gender, int age, String School_Name, float Salary, Student students){
        this.f_name = f_name;
        this.l_name = l_name;
        this.nationality = nationality;
        this.gender = gender;
        this.age = age;
        this.School_Name = School_Name;
        this.Salary = Salary;
        this.type = "Teachers";
        this.students =students;
    }
    @Override
    public String Get_Full_Name(){
        return this.f_name + " " + this.l_name;
    }
    @Override
    public String Get_Nationality(){
        return this.nationality;
    }
    @Override
    public char Get_Gender(){
        return this.gender;
    }
    @Override
    public int Get_Age(){
        return this.age;
    }
    @Override
    public String Get_email(){
        return this.l_name.charAt(0)+"." + this.f_name + "@"+this.School_Name+"."+this.type+".edu";
    }
    public void Set_Salary(float amount){
        this.Salary += amount;
    }
    public double Get_Salary(){
        return this.Salary;
    }
    public double ApplyRaise(){
        return this.Salary *= raise_amount;
    }
    public String GetStudents(){
       return students.Get_Full_Name();
        }
    }


    
        //get full name
        //get nationality
        //get age
        //get gender
        //get email
    
    

