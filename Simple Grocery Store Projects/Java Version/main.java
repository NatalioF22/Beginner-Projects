import java.io.FileReader;

import com.opencsv.CSVReader;

public class App {
    public static void main(String[] args) throws Exception {
        Manager manager1 = new Manager("Natalio", "Gomes", 32, "Meat", 9000, "CapeVerdean", "Black","Meat","Vicentes");
        Manager manager2 = new Manager("Livy", "Fournier", 38, "Kitchen", 10000, "Canadian", "White","Grocery","Market basket");

        Employees employee1 = new Employees("Kevin", "Pina", 32, "Meat", 8000, "CapeVerdean", "Spanic", "Supermaket","Beto");
        Employees employee2 = new Employees("Leandro", "Push", 38, "Kitchen", 5000, "Canadian", "White","MiniMarket","Shaws");
        
    }
}


public class Employees extends Store{
    //first name
    //last anme
    //age
    //department
    //email
    //salary
    //Type
    //ethnicity
    Double raise = 1.3;
    public Employees(String First_Name,String Last_Name, int Age, String department, double salary, String ethnicity, String race, String commercialtype, String store_name){
        this.First_Name = First_Name;
        this.Last_Name = Last_Name;
        this.Age = Age;
        this. department = department;
        this.salary = salary;
        this.type = "Employee";
        this.ethnicity = ethnicity;
        this.race = race;
        this.commercialtype = commercialtype;
        this.store_name = store_name;
        Store.total_members +=1;
        Store.employees+=1;
    }

    @Override
    public String GetName() {
        return this.First_Name+ " "+ this.Last_Name;
    }

    @Override
    public int GetAge() {

        return this.Age;
    }

    @Override
    public String GetDepartment() {
        return this.department;
    }

    @Override
    public String GetEmail() {
        return this.Last_Name +this.Last_Name+this.type+"@"+this.store_name+"."+this.commercialtype.strip();
    }

    @Override
    public String GetType() {
        // TODO Auto-generated method stub
        return this.type;
    }

    @Override
    public Double GetSalary() {
        return this.salary;
    }

    @Override
    public String GetEtchnicity() {
        
        return this.ethnicity;
    }

    @Override
    public String GetRace() {
        return this.race.toUpperCase();
    }

    @Override
    public String GetStoreName() {
        
        return this.store_name;
    }

    @Override
    public String GetCommercialType() {
        return this.commercialtype.strip();
    }

    @Override
    public Double SetRaise(double amount) {
        return this.raise = amount;
    }

    @Override
    public Double ApplyRaise() {
        return this.salary*=raise;
    }
}

public class Manager extends Store {
    Double raise = 1.2;
    public Manager(String First_Name,String Last_Name, int Age, String department, double salary, String ethnicity, String race, String commercialtype, String store_name){
        this.First_Name = First_Name;
        this.Last_Name = Last_Name;
        this.Age = Age;
        this. department = department;
        this.salary = salary;
        this.type = "Manager";
        this.ethnicity = ethnicity;
        this.race = race;
        this.commercialtype = commercialtype;
        this.store_name = store_name;
        Store.managers+=1;
        Store.total_members+=1;
        
    }

    @Override
    public String GetName() {
        return this.First_Name+ " "+ this.Last_Name;
    }

    @Override
    public int GetAge() {

        return this.Age;
    }

    @Override
    public String GetDepartment() {
        return this.department;
    }

    @Override
    public String GetEmail() {
        return this.Last_Name +this.Last_Name+this.type+"@"+this.store_name+"."+this.commercialtype;
    }

    @Override
    public String GetType() {
        return this.type;
    }

    @Override
    public Double GetSalary() {
        return this.salary;
    }

    @Override
    public String GetEtchnicity() {
        
        return this.ethnicity;
    }

    @Override
    public String GetRace() {
        return this.race.toUpperCase();
    }

    @Override
    public String GetStoreName() {
        
        return this.store_name;
    }

    @Override
    public String GetCommercialType() {
        return this.commercialtype.strip();
    }
   

    @Override
    public Double SetRaise(double amount) {
        return this.raise = amount;
    }

    @Override
    public Double ApplyRaise() {
        return this.salary*=raise;
    }
}


public abstract class Store {
    protected static int total_members= 0;
    protected static int employees= 0;
    protected static int managers= 0;
    protected String First_Name;
    protected String Last_Name;
    protected int Age;
    protected String department;
    protected double salary;
    protected String type;
    protected String ethnicity;
    protected String race;
    protected String store_name;
    protected String commercialtype;


    public abstract String GetName();
    public abstract int GetAge();
    public abstract String GetDepartment();
    public abstract String GetEmail();
    public abstract String GetType();
    public abstract Double GetSalary();
    public abstract String GetEtchnicity();
    public abstract String GetRace();
    public abstract String GetStoreName();
    public abstract String GetCommercialType();
    public abstract Double SetRaise(double amount);
    public abstract Double ApplyRaise();


    
}
