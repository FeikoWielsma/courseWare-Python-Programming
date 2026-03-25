package employees;

public class ManagerEmployee extends Employee
{
  public int weekSal;

  public ManagerEmployee (String s) {
	  super(s);
	  weekSal = 10;
  }

  public ManagerEmployee (String s, int sal) {
	  super(s);
	  weekSal = sal;
  }

  public void setSal(int w) {
	  weekSal = w;
  }

  public int calcSal() {
	  return weekSal;
  }
}
