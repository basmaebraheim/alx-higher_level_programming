#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in linked list
 * @head: pointer to head of list
 * @number: data for new node in list
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL && current->next->n < number)
            current = current->next;
        new->next = current->next;
        current->next = new;
    }

    return (new);
}