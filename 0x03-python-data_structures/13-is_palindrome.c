#include "lists.h"

/**
 * reverse_list - reverse list
 * @head: Pointer to the head  list
 * Return: Pointer to the new head  list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return prev;
}

/**
 * is_palindrome - is a singly linked list a palindrome
 * @head: Pointer to the head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return 1;

	listint_t *slow = *head;
	listint_t *fast = *head;

	/* Use the slow and fast pointers to find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse the second half of the list */
	listint_t *second_half = reverse(slow);

	/*Compare the first and reversed second halves of the list */
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			return 0;

		*head = (*head)->next;
		second_half = second_half->next;
	}

	return 1;
}