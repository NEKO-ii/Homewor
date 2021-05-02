//数据结构实验三  栈的基础操作

#include <iostream>
#include <stdlib.h>
#include <malloc.h>
using namespace std;

#define OK 1
#define OVERFLOW -1
#define ERROR 0
#define STACK_INIT_SIZE 100
#define STACKINCREMENT 10

typedef char SElemType;
typedef int ElemType;
typedef int Status;

typedef struct {
	SElemType* base;
	SElemType* top;
	int stacksize;
}SqStack;

//构造空栈
Status InitStack(SqStack& S) {
	S.base = (SElemType*)malloc(STACK_INIT_SIZE * sizeof(SElemType));
	if (!S.base) exit(OVERFLOW);
	S.top = S.base;
	S.stacksize = STACK_INIT_SIZE;
	return OK;
}
//取栈顶元素
Status GetTop(SqStack S, SElemType& e) {
	if (S.top == S.base) return ERROR; 
	e = *(S.top - 1);
	return OK;
}
//插入
Status Push(SqStack& S, SElemType e) {
	if (S.top - S.base >= S.stacksize) {
		S.base = (SElemType*)realloc(S.base, (S.stacksize + STACKINCREMENT) * sizeof(SElemType));
		if (!S.base)exit(OVERFLOW);
		S.top = S.base + S.stacksize;
		S.stacksize = S.stacksize + STACKINCREMENT;
	}
	*S.top++ = e;
	return OK;
}
//删除
Status Pop(SqStack& S, SElemType& e) {
	if (S.top == S.base) return ERROR;
	e = *--S.top;
	return OK;
}
//判断栈是否为空
Status Empty(SqStack S) {
	if (S.top == S.base) return OK;
	else return ERROR;
}
//输出
void Print(SqStack S) {
	char a = 0;
	SqStack A;
	A = S;
	if (Empty(A) == OK) { printf("栈已空"); }
	else {
		printf("当前栈的元素为（由栈顶到栈底）：\n");
		while (Empty(A) != OK) { Pop(A, a); printf("%d ", a); }
	}
	printf("\n");
}
//括号匹配算法
Status Match(SqStack &K,char& ch) {
	SElemType p,x;

	p = ch;

	if (p == '(' || p == '[' || p == '{') { Push(K, ch); printf("左括号已存储，请继续"); return OK; }
	else if (p == ')' || p == ']' || p == '}') {
		if (Empty(K) == OK) { printf("无左括号，右括号多余\n"); return ERROR; }
		else {
			if (*(K.top - 1)=='('&&p==')') { 
				printf("右括号匹配\n"); 
				Pop(K,x); 
				return OK;
				if (Empty(K) == OK)return ERROR;
			}
			if (*(K.top - 1) == '[' && p == ']') {
				printf("右括号匹配\n");
				Pop(K, x);
				return OK;
				if (Empty(K) == OK)return ERROR;
			}
			if (*(K.top - 1) == '{' && p == '}') {
				printf("右括号匹配\n");
				Pop(K, x);
				return OK;
				if (Empty(K) == OK)return ERROR;
			}
			else {
				printf("右括号不匹配，请重新");
				return OK;
			}
		}
	}
	else { printf("输入错误\n"); return ERROR; }
}

int main()
{
	int q1,q2,q3,q4,q5,q6;  //分支
	int i;
	int a,b,c,f;
	char d,e;
	SqStack S;  //存储数字
	SqStack K;  //存储括号
	SElemType p;

	InitStack(S);
	InitStack(K);

	printf("是否使用已有栈？是：1；否：2\n");  //q1
	scanf_s("%d", &q1);
	//若使用已有栈，从此处开始
	if (q1 == 1) {
		for (i = 5; i >= 1; i--) {
			Push(S, i);
		}
	}
	//若不使用已有栈，从此处开始
	else {
		printf("输入栈的长度：  ");
		scanf_s("%d", &a);
		for (i = 1; i <= a; i++) {
			printf("输入第%d个入栈元素:  ",i);
			scanf_s("%d", &b);
			Push(S, b);
		}
	}
	Print(S);

	while (1) {
		printf("执行操作？\n入栈：1；出栈：2；取栈顶：3；判断栈是否为空：4；括号匹配检验：5\n");  //q2
		scanf_s("%d", &q2);
		//入栈
		if (q2 == 1) {
			while (1) {
				printf("请输入入栈元素： ");
				scanf_s("%d", &c);
				if (Push(S, c) == OK)printf("成功！");
				else printf("操作失败");
				Print(S);
				printf("继续入栈操作？是：1；否：2\n");  //q3
				scanf_s("%d", &q3);
				if (q3 == 2) break;
			}
		}
		//出栈
		if (q2 == 2) {
			while (1) {
				if (Empty(S) == OK)printf("失败！栈已空\n");
				else {
					Pop(S, d);
					printf("成功！栈顶元素%d已出栈\n", d);
					Print(S);
				}
				printf("继续出栈操作？是：1；否：2\n");  //q3
				scanf_s("%d", &q3);
				if (q3 == 2) break;
			}
		}
		//取栈顶
		if (q2 == 3) {
			if (GetTop(S, e) == OK)printf("栈顶元素为：%d\n", e);
			else printf("栈为空，无栈顶元素\n");
		}
		//检验空
		if (q2 == 4) {
			if (Empty(S) == OK) printf("栈为空\n");
			else printf("栈非空\n");
		}
		//括号匹配
		if(q2==5) {
			while (1) {
				while (Empty(K) != OK) Pop(K, e);
				printf("请注意以下输入均为英文括号\n");
				while (1) {
					printf("输入括号： ");
					cin >> p;
					if (Match(K, p) == ERROR) {
						printf("是否继续？是：1；否：2\n");  //q4
						scanf_s("%d", &q4);
						if (q4 == 2)break;
					}
				}
				printf("是否清空存储重新开始？是：1；否：2\n");  //q5
				scanf_s("%d", &q5);
				if (q5 == 2)break;
			}
		}
		printf("是否执行其他操作？是：1；否：2\n");  //q6
		scanf_s("%d", &q6);
		if (q6 == 2)break;
	 }
} 