package com.mialab.mybatis_DML_demo.utils;

import java.io.InputStream;
import java.io.Reader;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.apache.log4j.Logger;

public class DBOperatorMgr {
	static Logger logger = Logger.getLogger(DBOperatorMgr.class.getName());
	private static DBOperatorMgr dbMgr;
	private SqlSessionFactory sqlSessionFactory;

	private DBOperatorMgr() {
		String resource = "mybatis-config.xml";
		InputStream inputStream;

		try {
			inputStream = Resources.getResourceAsStream(resource);
			sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
		} catch (Exception e) {
			logger.error(e.toString());
		}
	}

	public static DBOperatorMgr getInstance() {
		if (dbMgr == null) {
			dbMgr = new DBOperatorMgr();
		}
		return dbMgr;
	}
	
	public SqlSessionFactory getSqlSessionFactory() {
		return sqlSessionFactory;
	}	
}
