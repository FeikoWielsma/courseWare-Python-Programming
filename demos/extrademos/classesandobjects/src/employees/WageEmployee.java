package employees;

public class WageEmployee extends Employee
{
  int wage;
  int hours;

  public WageEmployee (String s)
  {
	  super(s);
	  wage = 0;
	  hours = 0;
  }

  public void setWage(int w)
  {
	  wage = w;
  }

  public void setHours(int h)
  {
	  hours = h;
  }

  public int calcSal()
  {
	  return wage*hours;
  }
}