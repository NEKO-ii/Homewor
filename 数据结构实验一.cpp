//数据结构实验课一  对顺序表的操作

#include "stdio.h"
#include"stdlib.h"
#include "malloc.h"
using namespace std;

#define OK 1
#define OVERFLOW -1
#define ERROR 0
#define LIST_INIT_SIZE 100
#define LISTINCREMENT  10

typedef int ElemType;
typedef int Status;

typedef  struct {
	ElemType* elem;
	int  length;
	int  listsize;
}sqlist;

//初始化顺序表
Status InitList_sq(sqlist* L) {
	L->elem = (ElemType*)malloc(LIST_INIT_SIZE * sizeof(ElemType));
	if (!L->elem) exit(OVERFLOW);
	L->length = 0;
	L->listsize = LIST_INIT_SIZE;
	return OK;
}
//顺序表插入
Status ListInsert_Sq(sqlist* L, int i, ElemType e) {
	ElemType* newbase, * p, * q;
	if (i<1 || i>L->length + 1) return ERROR;
	if (L->length == L->listsize) {
		newbase = (ElemType*)realloc(L->elem, (L->listsize + LISTINCREMENT) *
			sizeof(ElemType));
		if (!newbase) exit(OVERFLOW);
		L->elem = newbase;
		L->listsize = L->listsize + LISTINCREMENT;
	}
	q = &(L->elem[i - 1]);
	for (p = &(L->elem[L->length - 1]); p >= q; --p) *(p + 1) = *p;
	*q = e;
	++L->length;
	return OK;
}
//顺序表删除
Status ListDelete_Sq(sqlist* L, int i, ElemType& e) {
	ElemType* p, * q;
	if (i<1 || i>L->length) return ERROR;
	p = &(L->elem[i - 1]);
	e = *p;
	q = L->elem + L->length - 1;
	for (++p; p <= q; ++p) *(p - 1) = *p;
	--L->length;
	return OK;
}
//顺序表输出
Status ListPrint_Sq(sqlist L) {
	int* p, * q;
	if (L.length == 0)return ERROR;
	else {
		q = L.elem + L.length - 1;
		for (p = L.elem; p <= q; ++p)printf("%d ", *p);
	}
	printf("\n");
	return OK;
}
//顺序表读取
void GetElem(sqlist L, int i, ElemType& e) {
	int* p;
	p = &(L.elem[i - 1]);
	e = *p;
}
//顺序表排序合并
void Merglist_sq(sqlist* La, sqlist* Lb, sqlist* Lc) {
	int ai = 0;
	int bj = 0;
	int i = 1;
	int j = 1;
	int k = 0;
	while ((i <= La->length) && (j <= Lb->length)) {
		GetElem(*La, i, ai);
		GetElem(*Lb, j, bj);
		if (ai <= bj) {
			ListInsert_Sq(Lc, ++k, ai);
			++i;
		}
		else {
			ListInsert_Sq(Lc, ++k, bj);
			++j;
		}
	}
	while (i <= La->length) {
		GetElem(*La, i++, ai);
		ListInsert_Sq(Lc, ++k, ai);
	}
	while (j <= Lb->length) {
		GetElem(*Lb, j++, bj);
		ListInsert_Sq(Lc, ++k, bj);
	}
}

//主函数
int main()
{
	sqlist La, Lb, Lc;  //声明表
	int i, j;  //控制循环
	int s, r;  //数据暂存
	int ins, del, pos;  //ins插入，del删除，pos表示位置
	int dowhat, cwho, swho, again, go_on, back;  //判断执行何操作

	while (1) {
		//初始化
		InitList_sq(&La);
		InitList_sq(&Lb);
		InitList_sq(&Lc);

		printf("是否使用已有顺序表？是：1；否：2\n");
		scanf_s("%d", &dowhat);


		if (dowhat == 1) {
			//若使用已有顺序表，从此处开始 
			for (j = 1; j <= 8; j++) {
				ListInsert_Sq(&La, j, j);
			}
			for (j = 1; j <= 11; j++) {
				ListInsert_Sq(&Lb, j, j);
			}
		}
		else {
			//若不使用已有顺序表，执行以下操作
			printf("请输入顺序表La的长度");
			scanf_s("%d", &La.length);
			for (i = 0; i < La.length; i++) {
				printf("请输入顺序表La的第%d个元素：", i + 1);
				scanf_s("%d", &La.elem[i]);
			}
			printf("请输入顺序表Lb的长度");
			scanf_s("%d", &Lb.length);
			for (i = 0; i < Lb.length; i++) {
				printf("请输入顺序表Lb的第%d个元素：", i + 1);
				scanf_s("%d", &Lb.elem[i]);
			}
			printf("\n");
		}
		while (1) {
			//输出当前顺序表
			printf("当前顺序表为\nLa：\n");
			ListPrint_Sq(La);
			printf("Lb：\n");
			ListPrint_Sq(Lb);
			printf("\n");

			//判断所要执行的操作
			printf("接下来要做点什么吗【雾~】？\n插入请按1  ⁄(⁄⁄•⁄ω⁄•⁄⁄)⁄\n删除请按2  (。-＿-。)\n合体请按3！ (*ﾉωﾉ)（ps:是两个顺序表的合体）\n");
			scanf_s("%d", &dowhat);
			if (dowhat == 1) {
				while (1) {
					printf("插La：1；插Lb：2\n");
					scanf_s("%d", &cwho);
					if (cwho == 1) {
						printf("\n请输入插入的位置和数字，中间用空格连接\n当前La：");
						ListPrint_Sq(La);
						scanf_s("%d %d", &pos, &ins);
						if (ListInsert_Sq(&La, pos, ins) != OK)
						{
							printf("你是在为难我么（ps：插入元素失败）\n当前顺序表La：");
							ListPrint_Sq(La);
						}
						else
						{
							printf("\n(ps：插入成功！)\n当前顺序表La：");
							ListPrint_Sq(La);
							printf("\n");
						}

					}
					else {
						printf("\n请输入插入的位置和数字，中间用空格连接\n当前Lb：");
						ListPrint_Sq(Lb);
						scanf_s("%d %d", &pos, &ins);
						if (ListInsert_Sq(&Lb, pos, ins) != OK)
						{
							printf("你是在为难我么（ps：插入元素失败）\n当前顺序表Lb：");
							ListPrint_Sq(Lb);
						}
						else
						{
							printf("\n(ps：插入成功！)\n当前顺序表Lb：");
							ListPrint_Sq(Lb);
							printf("\n");
						}
					}
					printf("还要再插么？要：1；算了：2\n");
					scanf_s("%d", &again);
					if (again == 2) break;
				}
			}//插入

			if (dowhat == 2) {
				while (1) {
					printf("要删La还是Lb??  删La：1；Lb：2\n");
					scanf_s("%d", &swho);
					if (swho == 1) {
						printf("\n请输入删除的位置\n当前La：");
						ListPrint_Sq(La);
						scanf_s("%d", &pos);
						if (ListDelete_Sq(&La, pos, del) != OK) {
							printf("（ps：插入元素失败）\n当前顺序表La：");
							ListPrint_Sq(La);
						}
						else {
							printf("元素%d已和您说拜拜。\n当前顺序表La：", del);
							ListPrint_Sq(La);
							printf("\n");
						}
					}
					else {
						printf("\n请输入删除的位置\n当前Lb：");
						ListPrint_Sq(Lb);
						scanf_s("%d", &pos);
						if (ListDelete_Sq(&Lb, pos, del) != OK) {
							printf("（ps：插入元素失败）\n当前顺序表Lb：");
							ListPrint_Sq(Lb);
						}
						else {
							printf("元素%d已和您说拜拜。\n当前顺序表Lb：", del);
							ListPrint_Sq(Lb);
							printf("\n");
						}
					}
					printf("还要再删么？要：1；算了：2\n");
					scanf_s("%d", &again);
					if (again == 2) break;
				}
			}//删除

			if (dowhat == 3) {
				printf("正在合并La和Lb...\n");
				Merglist_sq(&La, &Lb, &Lc);
				printf("合并成功！\n当前表Lc：");
				ListPrint_Sq(Lc);
			}//合并

			else {}
			printf("\n还要执行其他命令吗？要：1；算了：2\n");
			scanf_s("%d", &go_on);
			if (go_on == 2) break;
		}

		//判断是否重新建表
		printf("\n是否重新建表？是：1；算了：2\n");
		scanf_s("%d", &back);
		if (back == 2) break;
	}
}