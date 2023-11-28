#include "lists.h"

/**
 * check_cycle - checks if linked list is looped
 * @list: linked list
 * Return: 0 no cycle, otherwise 1 cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);

	fast = list->next->next;
	slow = list;
	while (fast != NULL && slow != NULL)
	{
		if (fast == slow)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}

	return (0);
}