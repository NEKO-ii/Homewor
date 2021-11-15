package com.mialab.mybatis_DML_demo.mapper;

import java.util.List;

import com.mialab.mybatis_DML_demo.domain.Student;

public interface StudentMapper {
	public Student getStudent(String sno);

	public int addStudent(Student student);

	public List<Student> getSudentAll();

	public int updateStudent(Student student);

	public int deleteStudent(String sno);
}
