package com.mialab.mybatis_DML_demo.main;

import java.io.InputStream;
import java.util.List;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.apache.log4j.Logger;

import com.mialab.mybatis_DML_demo.domain.Student;
import com.mialab.mybatis_DML_demo.mapper.StudentMapper;
import com.mialab.mybatis_DML_demo.utils.DBOperatorMgr;

public class DML_Main {	
	
	public static void main(String[] args) {
		//testInsert();
		//testSelectAll();
		//testSelect("20171509");
		//testUpdate();
		//testDelete("20171622");
	}	

	private static void testDelete(String sno) {
		Logger log = Logger.getLogger(DML_Main.class);
		SqlSession session = null;
		try {
			session = DBOperatorMgr.getInstance().getSqlSessionFactory().openSession();
			StudentMapper mapper = session.getMapper(StudentMapper.class);			
			mapper.deleteStudent(sno);			
			session.commit();
		} catch(Exception ex) {
			session.rollback();
			ex.printStackTrace();
		} finally {
			if (session != null) {
				session.close();
			}
		}		
	}

	private static void testSelectAll() {
		Logger log = Logger.getLogger(DML_Main.class);
		SqlSession session = null;
		try {
			session = DBOperatorMgr.getInstance().getSqlSessionFactory().openSession();
			StudentMapper mapper = session.getMapper(StudentMapper.class);
			List<Student> stu_list = mapper.getSudentAll();
			for(Student stu:stu_list) {
				//System.out.println(stu);
				log.info(stu);
			}			
		} finally {
			if (session != null) {
				session.close();
			}
		}		
	}

	private static void testInsert() {
		Logger log = Logger.getLogger(DML_Main.class);
		SqlSession session = null;
		try {
			session = DBOperatorMgr.getInstance().getSqlSessionFactory().openSession();
			StudentMapper mapper = session.getMapper(StudentMapper.class);
			Student student = new Student();
			student.setSno("20171622");
			student.setName("李白");
			student.setAge(88);
			student.setSex("男");
			student.setDept_no("2609");
			log.info(student);
			mapper.addStudent(student);			
			session.commit();
		} catch(Exception ex) {
			session.rollback();
			ex.printStackTrace();
		} finally {
			if (session != null) {
				session.close();
			}
		}		
	}

	private static void testSelect(String sno) {
		Logger log = Logger.getLogger(DML_Main.class);
		SqlSession session = null;
		try {
			session = DBOperatorMgr.getInstance().getSqlSessionFactory().openSession();
			StudentMapper mapper = session.getMapper(StudentMapper.class);
			Student student = mapper.getStudent(sno);
			//System.out.println(student);
			log.info(student);
		} finally {
			if (session != null) {
				session.close();
			}
		}		
	}
	
	private static void testUpdate() {
		Logger log = Logger.getLogger(DML_Main.class);
		SqlSession session = null;
		try {
			session = DBOperatorMgr.getInstance().getSqlSessionFactory().openSession();
			StudentMapper mapper = session.getMapper(StudentMapper.class);
			Student student = new Student();
			student.setSno("20171622");
			student.setName("苏东坡");
			student.setAge(68);
			student.setSex("女");
			student.setDept_no("2612");
			log.info(student);
			mapper.updateStudent(student);			
			session.commit();
		} catch(Exception ex) {
			session.rollback();
			ex.printStackTrace();
		} finally {
			if (session != null) {
				session.close();
			}
		}		
	}
}
