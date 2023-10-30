#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * check_cycle - check the lists cycle
 * @list: the list to be checked
 * Return: return (0) for no cycle, or return (1) for cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *last, *first;

	if (!list || !list->next)
	{
		return (0);
	}
	last = list->next;
	first = list->next->next;
	while (last && first && first->next)
	{
		last = last->next;
		first = first->next->next;
		if (last == first)
		{
			return (1);
		}
	}
	return (0);
}
