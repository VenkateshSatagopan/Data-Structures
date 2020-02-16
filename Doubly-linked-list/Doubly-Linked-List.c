/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include<stdlib.h>


struct Node
{
  int data;
  struct Node *previous;
  struct Node *next;
};
struct Node *
GetNewNode (int data)
{
  struct Node *node = (struct Node *) malloc (sizeof (struct Node));
  node->data = data;
  node->previous = NULL;
  node->next = NULL;
  return node;
}

struct Node *
Insert (struct Node *head, int position, int data)
{
  int i;
  struct Node *node = NULL;
  // To check whether the doubly linked list is  empty
  if (head == NULL)
    {
      node = GetNewNode (data);
      head = node;
      return head;
    }
  //Procedure to Insert elements when list size is greater than 2
  node = head;
  for (i = 0; i < position - 2; i++)
    {
      node = node->next;
    }
  // To check whether have to add second element at the tail
  if (node->next == NULL)
    {
      struct Node *temp = GetNewNode (data);
      node->next = temp;
      temp->previous = node;
      return head;
    }
  else
    {
      struct Node *temp = GetNewNode (data);
      temp->next = node->next;
      temp->previous = node;
      node->next = temp;
      node = temp->next;
      node->previous = temp;
      return head;
    }
  return head;
}

struct Node *
Reverse_List (struct Node *head)
{


  struct Node *temp = head->previous;
  head->previous = head->next;
  head->next = temp;
  if (head->previous == NULL)
    return head;


  head = Reverse_List (head->previous);
  return head;
}


void
print (struct Node *head)
{
  struct Node *node = head;
  printf ("\n Doubly Linked-List data:\n");
  while (node != NULL)
    {
      printf ("%d\t", node->data);
      node = node->next;
    }
}

int
main ()
{
  //printf("Hello World");
  int i;
  struct Node *head = NULL;
  // Insert First element
  head = Insert (head, 1, 3);
  // Insert second element at the tail
  head = Insert (head, 2, 4);
  // Insert elemet at position 2 
  head = Insert (head, 2, 10);
  // Insert fourth element at the tail
  head = Insert (head, 4, 4);
  head = Insert (head, 4, 9);
  //print(head);
  head = Insert (head, 3, 12);
  print (head);
  // Reverse Doubly linked list
  head = Reverse_List (head);
  printf ("\nReversing Doubly linked list");
  print (head);
  return 0;
}
