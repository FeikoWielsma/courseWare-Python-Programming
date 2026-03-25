package employees;

public class Employee {
	private String name;

	public Employee() {
		name = "Empty";
	}

	public Employee(String s) {
		name = s;
	}

	public String getName() {
		return name;
	}

	public void setName(String s) {
		s = name;
	}
}
