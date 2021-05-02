//数据结构实验二   链表的基本操作

#include <iostream>
#include<stdio.h>
#include<malloc.h>
using namespace std;

#define OK 1
#define ERROR 0
#define OVERFLOW -1

typedef int ElemType;
typedef int Status;

typedef struct LNode {
	ElemType data;
	struct LNode* next;
}LNode, * LinkList;

//正序创建单链表
void SCreateList_L(LinkList& L, int n) {
	int i;
	LinkList p,q;
	L = (LinkList)malloc(sizeof(LNode));
	q = L;  //因为想让链表输出函数能同时输出正序和逆序的链表，所以加一个指针q来代替L的变化，使L一直指向链表开头
	if (L) {
		for (i = 1; i <= n; i++) {
			p = (LinkList)malloc(sizeof(LNode));
			if (p) {
				printf("请输入第%d个元素：", i);
				scanf_s("%d", &(p->data));
				q->next = p;
				q = p;
			}
		}
		q->next = NULL;
	}
}
//逆序创建单链表
void BCreateList_L(LinkList& L, int n) {
	int i;
	LinkList p;
	L = (LinkList)malloc(sizeof(LNode));
	if (L) {
		L->next = NULL;
		for (i = n; i > 0; --i) {
			p = (LinkList)malloc(sizeof(LNode));
			if (p) {
				printf("请输入第%d个元素：", n);
				scanf_s("%d", &(p->data));
				p->next = L->next;
				L->next = p;
			}
		}
	}
}
//链表插入
Status ListInsert_L(LinkList& L, int i, ElemType e) {
	int j;
	LinkList p,s;
	p = L; j = 0;
	while (p && j < i - 1) { p = p->next; ++j; }
	if (!p || j > i - 1)return ERROR;
	s = (LinkList)malloc(sizeof(LNode));
	if (s) {
		s->data = e;
		s->next = p->next;
		p->next = s;
		return OK;
	}
}
//链表删除
Status ListDelete_L(LinkList& L, int i, ElemType& e) {
	int j;
	LinkList p,q;
	p = L; j = 0;
	while (p->next && j < i - 1) { p = p->next; ++j; }
	if (!(p->next) || j > i + 1)return ERROR;  //删除位置不合理
	q = p->next;
	p->next = q->next;
	e = q->data;
	free(q);  //释放节点
	return OK;
}
//链表合并
Status MergeList_L(LinkList& La, LinkList& Lb, LinkList& Lc) {
	LinkList pa, pb, pc;
	pa = La->next;
	pb = Lb->next;
	Lc = pc = La;
	while (pa && pb) {
		if (pa->data <= pb->data) { pc->next = pa; pc = pa; pa = pa->next; }
		else { pc->next = pb; pc = pb; pb = pb->next; }
	}
	pc->next = pa ? pa : pb;
	free(Lb);
	return OK;
}
//链表输出
void ListPrint(LinkList L) {
	LinkList p;
	p = L->next;
	while (p) { printf("%d ", p->data); p = p->next; }
	printf("\n");
}

int main()
{
	LinkList La,Lb,Lc;
	ElemType e;
	LinkList p;
	int i;  //控制循环
	int q1,q2,q3,q4,q5,q6;  //存储用户选择分支
	int ListLen,Ipos,ins,Dpos,Lb_Len;  //存储数据

	while (1) {
		printf("是否使用已有链表？是：1；否：2\n");  //q1
		scanf_s("%d", &q1);
		//使用已有链表，从当前开始
		if (q1 == 1) {
			La = (LinkList)malloc(sizeof(LNode));
			if (La) {
				La->next = NULL;
				for (i = 5; i > 0; --i) {
					p = (LinkList)malloc(sizeof(LNode));
					if (p) {
						p->data = i;
						p->next = La->next;
						La->next = p;
					}
				}
			}
			printf("构建成功，当前La:\n");
			ListPrint(La);
		}
		//自行输入链表，从当前开始
		else {
			printf("选择创建方式？正序：1；逆序：2\n");  //q2
			scanf_s("%d", &q2);
			if (q2 == 1) {
				printf("请输入所要创建的链表长度：   ");
				scanf_s("%d", &ListLen);
				SCreateList_L(La, ListLen);
				printf("构建成功，当前La:\n");
				ListPrint(La);
			}
			else {
				printf("请输入所要创建的链表长度：   ");
				scanf_s("%d", &ListLen);
				BCreateList_L(La, ListLen);
				printf("构建成功，当前La:\n");
				ListPrint(La);
			}
		}

		while (1) {
			//判断接下来的操作
			printf("接下来要执行的操作是？插入：1；删除：2；合并：3\n");  //q3
			scanf_s("%d", &q3);
			//插入操作
			if (q3 == 1) {
				while (1) {
					printf("输入要插入的位置和元素，中间用空格连接\n当前La：");
					ListPrint(La);
					scanf_s("%d %d", &Ipos, &ins);
					if (ListInsert_L(La, Ipos, ins)) { printf("插入成功！当前链表为La："); ListPrint(La); printf("\n"); }
					else { printf("插入失败！当前链表为La："); ListPrint(La); printf("\n"); }
					printf("\n");
					printf("是否继续插入？是：1；否：2\n");  //q4
					scanf_s("%d", &q4);
					if (q4 == 2) break;
				 }
			}
			//删除操作
			if (q3 == 2) {
				while (1) {
					printf("输入要删除的位置\n当前La：");
					ListPrint(La);
					scanf_s("%d", &Dpos);
					if (ListDelete_L(La, Dpos, e) == ERROR) { printf("删除失败！删除位置不合理\n当前La为："); ListPrint(La); }
					else {
						printf("删除成功！元素%d已删除。当前La为：\n", e);
						ListPrint(La);
					}
					printf("\n");
					printf("是否继续删除？是：1；否：2\n");  //q4
					scanf_s("%d", &q4);
					if (q4 == 2) break;
				}
			}
			//合并操作
			if (q3 == 3) {
				printf("请输入要与La合并的Lb。\nLb的长度为：");
				scanf_s("%d", &Lb_Len);
				SCreateList_L(Lb, Lb_Len);
				MergeList_L(La, Lb, Lc);
				printf("\n");
				printf("正在合并...\n合并成功！合并后的Lc为：\n");
				ListPrint(Lc);
				printf("\n");
			}

			//判断是否执行其他操作
			printf("是否执行其他操作？是：1；否：2\n");  //q5
			scanf_s("%d", &q5);
			if (q5 == 2) break;
		 }
		

		//判断是否重新开始
		printf("是否重新建表？是：1；否：2\n");  //q6
		scanf_s("%d", &q6);
		if (q6 == 2) break;
	 }
}