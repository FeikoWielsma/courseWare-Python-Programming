import employees.*;

class Company
{
  public static void main(String args[])
  {
    Employee e = new Employee("E1");
	System.out.println("Hello generic employee " + e.getName());

    WageEmployee w = new WageEmployee ("W1");
	System.out.println("Hello wage worker " + w.getName());
	w.setHours (10);
	w.setWage (10);

	System.out.println("Salary : " + w.calcSal());

    ManagerEmployee m = new ManagerEmployee ("M1", 1000);
	System.out.println("Hello manager " + m.getName());
	System.out.println("Salary : " + m.calcSal());
	m.weekSal = 500;
	System.out.println("Salary : " + m.calcSal());

    ProgrammerEmployee p = new ProgrammerEmployee ("P1");
	System.out.println("Hello programmer " + p.getName());
	p.setHours (10);
	p.setWage (10);
	p.setLines (1000);
	p.setBugs (100);
	System.out.println("Salary : " + p.calcSal());
  }
}