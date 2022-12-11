#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the first node of the singly linked list
 * @number: the data to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = temp;
		return (new);
	}

	while (temp->next->n < number)
		temp = temp->next;

	new->next = temp->next;
	temp->next = new;

	return (new);
}
