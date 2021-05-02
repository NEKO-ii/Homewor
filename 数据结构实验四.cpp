// 数据结构实验四  队列的应用

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <malloc.h>
#include <queue>
using namespace std;

#define MAXSIZE 100
#define OK 1
#define ERROR 0
#define OVERFLOW -1

typedef int Status;
typedef int QElemType;

//链队列的存储空间定义
typedef struct QNode {
	QElemType data;
	struct QNode* next;
}QNode, * QueuePtr;
typedef struct {
	QueuePtr front;  //队头
	QueuePtr rear;  //队尾
}LinkQueue;

//循环队列的存储空间定义
typedef struct {
	QElemType* base;
	int front;
	int rear;
}SqQueue;
/*-------------------------------------------------------链队列操作------------------------------------------------------------*/
//初始化空队列
Status InitQueue_L(LinkQueue& Q) {
	Q.front = Q.rear = (QueuePtr)malloc(sizeof(QNode));
	if (!Q.front) exit(OVERFLOW);
	Q.front->next = NULL;
	return OK;
}
//入队
Status EnQueue_L(LinkQueue& Q, QElemType e) {
	QueuePtr p;
	p = (QueuePtr)malloc(sizeof(QNode));
	if (!p) exit (OVERFLOW);
	p->data = e;
	p->next = NULL;
	Q.rear->next = p;
	Q.rear = p;
	return OK;
}
//出队
Status DeQueue_L(LinkQueue& Q, QElemType& e) {
	QueuePtr p;
	if (Q.front == Q.rear) return ERROR;
	p = Q.front->next;
	e = p->data;
	Q.front->next = p->next;
	if (Q.rear == p) Q.rear = Q.front;
	free(p);
	return OK;
}
//取队头
Status GetHead_L(LinkQueue Q, QElemType& e) {
	if (Q.front == Q.rear) return ERROR;
	e = Q.front->next->data;
	return OK;
}
//判断队空
Status QueueEmpty_L(LinkQueue Q) {
	if (Q.front == Q.rear) return OK;
	else return ERROR;
}
//输出
Status Print_L(LinkQueue& Q) {
	QueuePtr p;
	int a;
	p = Q.front;
	printf("当前队列为：（头）");
	while (p != Q.rear) {
		a = p->next->data;
		printf("%d ", a);
		p = p->next;
	 }
	printf("（尾）\n\n");
	return OK;
}

//构造杨辉三角
Status Yang_L(int n) {
	int a, s, r;
	int i, k, j;
	LinkQueue A, B, C;
	InitQueue_L(A);
	InitQueue_L(B);
	InitQueue_L(C);

	EnQueue_L(A, 1);
	EnQueue_L(A, 0);
	EnQueue_L(B, 1);
	EnQueue_L(B, 0);

	for (i = 2; i <= n; i++) {
		s = 0;
		while (1) {
			DeQueue_L(B, r);
			s = s + r;
			EnQueue_L(A, s);
			EnQueue_L(C, s);
			s = r;
			if (B.front == B.rear) break;
		}
		EnQueue_L(A, 0);
		EnQueue_L(C, 0);
		while (C.front != C.rear) {
			DeQueue_L(C, a);
			EnQueue_L(B, a);
		}
	}
	printf("构造完成！\n");
	if (n < 10) {
		for (k = 1; k <= 3 * n; k++) { printf(" "); }
		while (A.front != A.rear) {
			DeQueue_L(A, a);
			if (a == 0) { printf("\n"); for (k = 1; k <= 3 * (n - 1); k++) { printf(" "); } n = n - 1; }
			else printf("%d    ", a);
		}
	}
	if (n >= 10) {
		for (k = 1; k <= 4 * n; k++) { printf(" "); }
		while (A.front != A.rear) {
			DeQueue_L(A, a);
			if (a == 0) { printf("\n"); for (k = 1; k <= 4 * (n - 1); k++) { printf(" "); } n = n - 1; }
			else printf("%d      ", a);
		}
	}
	return OK;
}

/*-------------------------------------------------------循环队列操作----------------------------------------------------------*/
//初始化空队列
Status InitQueue_S(SqQueue& Q) {
	Q.base = (QElemType*)malloc(MAXSIZE * sizeof(QElemType));
	if (!Q.base) exit(OVERFLOW);
	Q.front = Q.rear = 0;
	return OK;
}
//入队
Status EnQueue_S(SqQueue& Q, QElemType e) {
	if ((Q.rear + 1) % MAXSIZE == Q.front) return ERROR;
	Q.base[Q.rear] = e;
	Q.rear = (Q.rear + 1) % MAXSIZE;
	return OK;
}
//出队
Status DeQueue_S(SqQueue& Q, QElemType& e) {
	if (Q.front == Q.rear) return ERROR;
	e = Q.base[Q.front];
	Q.front = (Q.front + 1) % MAXSIZE;
	return OK;
}
//取队头
Status GetHead_S(SqQueue Q, QElemType& e) {
	if (Q.front == Q.rear) return ERROR;
	e = Q.base[Q.front];
	return OK;
}
//判断队空
Status QueueEmpty_S(SqQueue Q) {
	if (Q.front == Q.rear) return OK;
	else return ERROR;
}
//输出
Status Print_S(SqQueue& Q) {
	SqQueue A;
	QElemType p=NULL;
	int a;
	A = Q;
	p = A.base[A.front];
	printf("当前队列为：（头）");
	while (A.front!=A.rear) {
		DeQueue_S(A, a);
		printf("%d ", a);
	}
	printf("（尾）\n\n");
	return OK;
}

//构造杨辉三角
Status Yang_S(int n){
	int a, s, r;
	int i, k, j;
	SqQueue A, B, C;
	InitQueue_S(A);
	InitQueue_S(B);
	InitQueue_S(C);

	EnQueue_S(A, 1);
	EnQueue_S(A, 0);
	EnQueue_S(B, 1);
	EnQueue_S(B, 0);

	for (i = 2; i <= n; i++) {
		s = 0;
		while (1) {
			DeQueue_S(B, r);
			s = s + r;
			EnQueue_S(A, s);
			EnQueue_S(C, s);
			s = r;
			if (B.front == B.rear) break;
		}
		EnQueue_S(A, 0);
		EnQueue_S(C, 0);
		while (C.front != C.rear) {
			DeQueue_S(C, a);
			EnQueue_S(B, a);
		}
	}
	printf("构造完成！\n");
	if (n < 10) {
		for (k = 1; k <= 3 * n; k++) { printf(" "); }
		while (A.front != A.rear) {
			DeQueue_S(A, a);
			if (a == 0) { printf("\n"); for (k = 1; k <= 3 * (n - 1); k++) { printf(" "); } n = n - 1; }
			else printf("%d    ", a);
		}
	}
	if (n >= 10) {
		for (k = 1; k <= 4 * n; k++) { printf(" "); }
		while (A.front != A.rear) {
			DeQueue_S(A, a);
			if (a == 0) { printf("\n"); for (k = 1; k <= 4 * (n - 1); k++) { printf(" "); } n = n - 1; }
			else printf("%d      ", a);
		}
	}
	return OK;
}

/*----------------------------------------------------------主函数-------------------------------------------------------------*/
int main()
{
	int q1,q2,q3,q4;  //分支
	int L_len,S_len;  //队列长度
	int a,in_l,in_s,en_l,en_s,de_l,de_s,head_l,head_s,h;//a控制循环，in为构造时的参数，en入队参数，de出队参数，head为队头返回参数
	char c[10] = {  };  //输入数据暂存
	int ce;//重置队列时的返回值，无作用
	LinkQueue L,Ly;
	SqQueue S,Sy;

	InitQueue_L(L);
	InitQueue_S(S);

	while (1) {
		while (L.front != L.rear) { DeQueue_L(L, ce); }
		while (S.front != S.rear) { DeQueue_S(S, ce); }
		printf("使用哪种队列？链队列:1  ; 循环队列:2     >");  //q1
		scanf_s("%d", &q1);
		//链队列
		if (q1 == 1) {
			printf("输入队列长度： _");
			scanf_s("%d", &L_len);
			for (a = 1; a <= L_len; a++) {
				printf("请输入第%d个元素：_", a);
				scanf_s("%d", &in_l);
				EnQueue_L(L, in_l);
			}
			printf("构造完成！");
			Print_L(L);
			while (1) {
				printf("执行操作？入队:1  ; 出队:2  ; 取队头:3  ; 输出杨辉三角:4   [输入0以退出操作]     >");  //q2
				scanf_s("%d", &q2);
				if (q2 == 1) {  //入队
					while (1) {
						printf("输入数字以入队：[输入x终止入队操作]   _");
						cin>>c;
						en_l = atoi(c);
						if (*c=='x') break;
						else EnQueue_L(L, en_l);
						printf("操作成功！");
						Print_L(L);
					 }
				}
				if (q2 == 2) {  //出队
					while (1) {
						printf("输入[1 以继续]；[2 退出操作]     >");  //q3
						scanf_s("%d", &q3);
						if (q3 == 2) break;
						if (DeQueue_L(L, de_l) == ERROR) printf("操作失败！队列为空\n");
						else {
							printf("操作成功！队头元素%d已出队\n", de_l);
							Print_L(L);
						}
					 }
				}
				if (q2 == 3) {  //取队头
					if (GetHead_L(L, head_l) == ERROR) printf("操作失败！队列为空\n");
					else {
						printf("队头元素为%d\n\n", head_l);
					}
				}
				if (q2 == 4) {  //输出杨辉三角
					printf("输入杨辉三角行数：  _");
					scanf_s("%d", &h);
					Yang_L(h);
				}
				if (q2 == 0) break;
			 }
		}
		
		//循环队列
		if (q1 == 2) {
			printf("输入队列长度： _");
			scanf_s("%d", &S_len);
			for (a = 1; a <= S_len; a++) {
				printf("请输入第%d个元素：_", a);
				scanf_s("%d", &in_s);
				EnQueue_S(S, in_s);
			}
			printf("构造完成！");
			Print_S(S);
			while (1) {
				printf("执行操作？入队:1  ; 出队:2  ; 取队头:3  ; 输出杨辉三角:4   [输入0以退出操作]     >");  //q2
				scanf_s("%d", &q2);
				if (q2 == 1) {  //入队
					while (1) {
						printf("输入数字以入队：[输入x终止入队操作]   _");
						cin >> c;
						en_s = atoi(c);
						if (*c == 'x') break;
						else EnQueue_S(S, en_s);
						printf("操作成功！");
						Print_S(S);
					}
				}
				if (q2 == 2) {  //出队
					while (1) {
						printf("输入[1 以继续]；[2 退出操作]     >");  //q3
						scanf_s("%d", &q3);
						if (q3 == 2) break;
						if (DeQueue_S(S, de_s) == ERROR) printf("操作失败！队列为空\n");
						else {
							printf("操作成功！队头元素%d已出队\n", de_s);
							Print_S(S);
						}
					}
				}
				if (q2 == 3) {  //取队头
					if (GetHead_S(S, head_s) == ERROR) printf("操作失败！队列为空\n");
					else {
						printf("队头元素为%d\n\n", head_s);
					}
				}
				if (q2 == 4) {  //输出杨辉三角
					printf("输入杨辉三角行数：  _");
					scanf_s("%d", &h);
					Yang_S(h);
				}
				if (q2 == 0) break;
			}
		}
		
		printf("是否重新开始？是:1  ; 退出程序:2     >");  //q?
		scanf_s("%d", &q4);
		if (q4 == 1) printf("\n");
		if (q4 == 2) break;
	 }
}