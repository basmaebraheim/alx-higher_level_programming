#include "lists.h"

/**
 * check_cycle - checks  if singly linked list has a cycle in it.
 * @list: pointer to head node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *next;

	if (!list || !list->next)
		return (0);
	current = list;
	next = list->next;

	while (current && next->next
		&& next->next->next)
	{
		if (current == next)
			return (1);
		current = current->next;
		next = next->next->next;
	}
	return (0);
}
