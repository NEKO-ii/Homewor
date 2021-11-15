package com.mialab.mybatis_DML_demo.domain;

public class Student {
	private String sno;
	private String name;
	private String sex;
	private int age;
	private String dept_no;

	public String getSno() {
		return sno;
	}

	public void setSno(String sno) {
		this.sno = sno;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSex() {
		return sex;
	}

	public void setSex(String sex) {
		this.sex = sex;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getDept_no() {
		return dept_no;
	}

	public void setDept_no(String dept_no) {
		this.dept_no = dept_no;
	}

	@Override
	public String toString() {
		return "Student [sno=" + sno + ", name=" + name + ", sex=" + sex + ", age=" + age + ", dept_no=" + dept_no
				+ "]";
	}

}
