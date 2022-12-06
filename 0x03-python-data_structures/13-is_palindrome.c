#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: The first node of the list
 * Return: 0 if it is not a palindrom,
 *		   1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	listint_t *ptr = *head;
	listint_t *prev = NULL;
	listint_t *temp = NULL;

	while (h != NULL)
	{
		temp = h->next;
		h->next = prev;
		prev = h;
		h = temp;
	}
	*head = prev;
	while (ptr != NULL)
	{
		ptr = ptr->next;
	}
	while (h != NULL)
	{
		h = h->next;
	}
	if (ptr == h || h == NULL)
		return (1);
	else
		return (0);
}
