#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert node
 * @head: double pointer to head
 * @number: number
 * Return: return (NULL) if failed, on success return the adress of new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *old_node = *head;

	if (!head && !number)
	{
		return (NULL);
	}
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (!old_node || new_node->n < old_node->n)
	{
		new_node->next = old_node;
		return (*head = new_node);
	}
	while (old_node)
	{
		if (!old_node->next || new_node->n < old_node->next->n)
		{
			new_node->next = old_node->next;
			old_node->next = new_node;
			return (old_node);
		}
		old_node = old_node->next;
	}
	free(new_node), new_node = NULL;
	return (NULL);
}
