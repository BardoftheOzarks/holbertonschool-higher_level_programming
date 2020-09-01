#include "lists.h"
/**
 * check_cycle - checks if a linked list is cyclical
 * @list: singly linked list
 * Return: 0 if false, 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	while (list)
	{
		list = list->next;
		if (&list == &head)
			return (1);
	}
	return (0);
}
