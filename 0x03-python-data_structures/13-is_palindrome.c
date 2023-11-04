#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - check if it is palindrome
 * @head: the head of list
 * Return: return (0) for not palindrome, return (1) if palindrome
*/
int is_palindrome(listint_t **head)
{
	return (check_palindrome(head, *head));
}
/**
 * check_palindrome - check if the list is palindrome
 * @head: head list double pointer
 * @tail: the end of the list
 * Return: return (1) for palindrome, return (0) for no palindrome
*/
int check_palindrome(listint_t **head, listint_t *tail)
{
	if (*head == NULL || head == NULL || tail == NULL)
	{
		return (1);
	}
	if (check_palindrome(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
