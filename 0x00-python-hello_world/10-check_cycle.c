#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: single linked list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);/*i.e. not a linked list*/
	while (slow && fast && fast->next)/*-> ponter to next*/
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)/*there's a cycle*/
			return (1);
	}
	return (0);/*there's no cycle*/
}
