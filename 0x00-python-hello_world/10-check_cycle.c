#include "lists.h"
/**
 * check_cycle - checks if a linked list is cyclical
 * @list: singly linked list
 * Return: 0 if false, 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *this = list, *that = list->next;

	while (this && that)
	{
		if (this == that)
			return (1);
		this = this->next;
		if (that->next != NULL)
			that = that->next->next;
		else
			break;
	}
	return (0);
}
