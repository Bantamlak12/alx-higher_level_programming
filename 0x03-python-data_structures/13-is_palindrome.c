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
	listint_t *prev_node = NULL;

	while (next_node != NULL)
	{
		next_node = next_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}
	*head = prev_node;

	if (ptr == NULL || ptr->next == NULL)
		return (1);

	while (ptr->next != NULL)
	{
		ptr = ptr->next;
	}

	while ((*head)->next != NULL)
	{
		*head = (*head)->next;
	}

	if (ptr == *head)
		return (1);

	return (0);
}
