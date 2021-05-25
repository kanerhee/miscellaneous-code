// basic example of bare implementation of a stack containing integers

#include <iostream>
#include <cstdlib>
#include <cstddef>
using namespace std;

struct Node {
  int data;
  Node * next;
};

void push(Node * list, Node * node) {
  if (list == NULL) {
    list = node;
    list->next = NULL;
  }
  else {
    node->next = list;
    list = node;
  }
}

Node * pop(Node* list) {
  if (list == NULL) {
    return NULL;
  }
  else if (list->next == NULL) {
    Node * node = new Node;
    node = list;
    list = NULL;
    return node;
  }
  else {
    Node * node = new Node;
    node = list;
    list = list->next;
    return node;
  }
}

int main() {

  // P IS OLDEST NODE
  Node * p = new Node;
  p->data = 20;

  Node * q = new Node;
  q->data = 30;

  // R IS NEWEST NODE
  Node * r = new Node;
  r->data = 40;

  r->next = q;
  q->next = p;
  p->next = NULL;

  cout << "Before node s is pushed onto stack:" << endl;
  for (Node * node = r; node != NULL; node = node->next) {
    cout << node->data;
    cout << endl;
  }

  Node * s = new Node;
  s->data = 50;
  s->next = NULL;

  push(r, s);

  Node * t = new Node;
  t->data = 60;
 
  Node * u = new Node;
  u->data = 70;

  push(s, t);
  push(t, u);

  cout << "After node s is pushed onto stack:" << endl;
  for (Node * node = u; node != NULL; node = node->next) {
    cout << node->data;
    cout << endl;
  }

  pop(u);
  cout << "After 1st pop:" << endl;
  for (Node * node = t; node != NULL; node = node->next) {
    cout << node->data;
    cout << endl;
  }

  pop(t);
  pop(s);
  pop(r);
  
  cout << "After 3 more pops:" << endl;
  for (Node * node = q; node != NULL; node = node->next) {
    cout << node->data;
    cout << endl;
  }

  return 0;
}
