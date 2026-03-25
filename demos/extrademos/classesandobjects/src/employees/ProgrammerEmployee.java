package employees;

public class ProgrammerEmployee extends WageEmployee
{
  int lines;
  int bugs;

  public ProgrammerEmployee (String s)
  {
	  super(s);
	  lines = 0;
	  bugs = 0;
  }

  public void setLines(int l)
  {
	  lines = l;
  }

  public void setBugs(int b)
  {
	  bugs = b;
  }

  public int calcSal()
  {
	  return (super.calcSal() + (lines - bugs));
  }
}
