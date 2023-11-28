#include "lists.h"

/**
 * insert_node - add elements to node
 * @head: node starting point
 * @number: node value to be inserted
 *
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;
	listint_t *holder;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	temp = *head;
	holder = NULL;

	/* covers head is null */
	if (temp == NULL || number < temp->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* traverse node for correct position */
	while (temp != NULL && number > temp->n)
	{
		holder = temp;
		temp = temp->next;
	}

	/* position to insert node found */
	holder->next = new;
	new->next = temp;

	return (new);
}