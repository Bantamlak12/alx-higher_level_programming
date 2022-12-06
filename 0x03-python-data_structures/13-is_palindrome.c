#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: Head pointer to the first list
 * Return: 0 if it is not a palindrom,
 *		   1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *next_node = *head;
	listint_t *current_node = *head;
	listint_t *ptr = *head;
	listint_t *h = *head;
	listint_t *prev_node = NULL;

	while (next_node != NULL)
	{
		next_node = next_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}
	*head = prev_node;
	while (ptr != NULL)
		ptr = ptr->next;

	while (h != NULL)
		h = h->next;

	if (ptr == h || h == NULL)
		return (1);
	else
		return (0);
}
