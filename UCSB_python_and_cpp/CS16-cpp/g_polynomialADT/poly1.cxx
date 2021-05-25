// By Phillip Kane Rhee 
// Date: 1 - 29 - 16
//
// FILE: poly1.cxx

#include <iostream>
#include <cassert>
#include <cmath>
#include <climits>
#include <algorithm>
#include "poly1.h"
using namespace std;

namespace main_4
{
  // MEMBER CONSTANTS
  const unsigned int polynomial::DEFAULT_CAPACITY;
  
  // CONSTRUCTORS AND DESTRUCTOR

  // Standard Constructor
  polynomial::polynomial(double c, unsigned int exponent)
  {
    size = DEFAULT_CAPACITY;          // set size of the dynamic array 
    coef = new double[size];          // set *coef (pointer to dynamic array)
    current_degree = -1;              // sets degree of polynomial to 0
    for (int i=0; i <= size; i++)
      coef[i] = 0.0;
    current_degree = exponent;        // sets degree to work on to input value
    coef[current_degree] = c;
    if (c == 0.0)
      current_degree = 0;
  }

  // Copy Constructor
  polynomial::polynomial(const polynomial& source)
  {
    coef = new double[source.size];
    size = source.size;
    current_degree = source.current_degree;
    for (int i=0; i < size; i++)
      coef[i] = source.coef[i];
  }

  // Destructor
  polynomial::~polynomial()
  {
    delete [] coef;
  }



  // MODIFICATION MEMBER FUNCTION

  // Assignment Operator - GOOD
  polynomial& polynomial::operator =(const polynomial& source)
  {
    double* new_coef;
    if (this == &source)
      return *this;
    if (size != source.size) 
      {
	new_coef = new double[source.size];
	delete [] coef;
	coef = new_coef;
	size = source.size;
	current_degree = source.current_degree;
      }
    current_degree = source.current_degree;
    for (int i=0; i < size; i++)
      coef[i] = source.coef[i];
    return *this; 
  }

  void polynomial::add_to_coef(double amount, unsigned int exponent)
  {
    if (current_degree == size)
      reserve(size+1);
    current_degree = exponent;
    coef[current_degree] += amount;
    while (coef[current_degree] == 0.0)
      current_degree--;
  }

  void polynomial::assign_coef(double coefficient, unsigned int exponent)
  {
    if (degree() == size)
      reserve(size+300);
    coef[exponent] = coefficient;
    if (coefficient != 0.0 && exponent >= degree())
      current_degree = exponent;
    int i = current_degree;
    while (i >= 0 && coef[i] == 0.0)
      {
	current_degree--;
	i--;
      }
  }

  void polynomial::clear()
  {
    current_degree = 0;
    for (int i=size; i>=0; i--)
      coef[i] = 0.0;
  }

  void polynomial::reserve(unsigned int number)
  {
    double *larger_array;
    if (number == size)
      return;
    if (number < degree())
      number = current_degree;
    larger_array = new double[number];
    current_degree = degree();
    for (int i=0; i <= number; i++)
      {
	larger_array[i] = coef[i];
	if (i > degree())
	  larger_array[i] = 0.0;
      }
    delete [] coef;
    coef = larger_array;
    size = number;
  }

  // CONSTANT MEMBER FUNCTIONS
  double polynomial::coefficient(unsigned int exponent) const
  {
    if (exponent > size)
      return 0.0;
    else
      return coef[exponent];
  }

  polynomial polynomial::derivative() const
  {
    polynomial answer;
    answer.reserve(250);
    size_t derivArrSize = degree()-1;
    for (int j=0; j<=derivArrSize; j++)
      answer.assign_coef(0.0, j);
    for (int i=1; i<=degree(); i++)
      {
	double newCoef = coefficient(i)*i;
	int k = i-1;
	answer.assign_coef(newCoef, k);
      }
    answer.add_to_coef(0.0, derivArrSize);
    return answer;
  }

  double polynomial::eval(double x) const
  {
    double answer = 0.0;
    for (unsigned int i=0; i<=size; i++)
      {
	double term = 0.0;
	double multiple = pow(x,i);
	term = multiple * coef[i];
	answer += term;
      }
    return answer;
  }

  unsigned int polynomial::next_term(unsigned int e) const
  {
    unsigned int next = 0;
    for (int i=e; i<=size; i++)
      if (coefficient(i+1) != 0)
	{
	  next = i+1;
	  break;
	}
    if (next == 0)
      return 0;
    else
      return next;
  }

  unsigned int polynomial::previous_term(unsigned int e) const
  {
    unsigned int prev = UINT_MAX;
    for (int i=e; i>=-1; i--)
      if (coefficient(i-1) != 0)
	{
	  prev = i-1;
	  break;
	}
    if (prev == UINT_MAX)
      return UINT_MAX;
    else
      return prev;
  }

  void polynomial::find_root(double& answer,
			     bool& sucess,
			     unsigned int& iterations,
			     double guess,
			     unsigned int maximum_iterations,
			     double epsilon) const
  {
    assert( epsilon > 0);
    polynomial deriv = derivative();
    answer = guess;
    double f = eval(answer);
    double fprime = deriv.eval(answer);
    iterations = 0;
    sucess = false;
    // iteration forloop
    for (int i = iterations; i<=maximum_iterations; i++)
      {
	double newAnswer = answer;
	if (fabs(f) <= epsilon)  // success
	  {
	    sucess = true;
	    iterations = i;
	    answer = newAnswer;
	    break;
	  }
	else if (fabs(fprime) <= epsilon)  // flat failure
	  {
	    sucess = false;
	    iterations = i;
	    answer = newAnswer;
	    break;
	  }
	else if (i == maximum_iterations-1) // max iterations
	  {
	    sucess = false;
	    answer = newAnswer;
	    iterations = maximum_iterations;
	    break;
	  }
	i++;
	newAnswer = answer - f/fprime;
	f = eval(newAnswer);
	fprime = deriv.eval(newAnswer);
	answer = newAnswer;
      }
  }

  // NON-MEMBER BINARY OPERATORS
  polynomial operator+(const polynomial& p1, const polynomial& p2)
  {
    polynomial answer;    
    if (p1.degree() > p2.degree())
      {
	for (int i=0; i<=p1.degree(); i++)
	  answer.assign_coef(p1.coefficient(i), i);
	for (int i=0; i<=p2.degree(); i++)
	  answer.add_to_coef(p2.coefficient(i), i);
	for (int i=0; i<=p1.degree(); i++)
	  answer.add_to_coef(0.0, i);
      }
    else if (p1.degree() == p2.degree())
      {
	for (int i=0; i<=p1.degree(); i++)
	  {
	    answer.assign_coef(p1.coefficient(i), i);
	    answer.add_to_coef(p2.coefficient(i), i);
	  }
      }
    else
      {
	for (int i=0; i<=p2.degree(); i++)
	  answer.assign_coef(p2.coefficient(i), i);
	for (int i=0; i<=p1.degree(); i++)
	  answer.add_to_coef(p1.coefficient(i), i);
	for (int i=0; i<=p2.degree(); i++)
	  answer.add_to_coef(0.0, i);
      }
    return answer;
  }

  polynomial operator-(const polynomial& p1, const polynomial& p2)
  {
    polynomial answer;
    if (p1.degree() > p2.degree())
      {
	for (int i=0; i<=p1.degree(); i++)
	  answer.assign_coef(p1.coefficient(i), i);
	for (int i=0; i<=p2.degree(); i++)
	  answer.add_to_coef((p2.coefficient(i)*-1), i);
	for (int i=0; i<=p1.degree(); i++)
	  answer.add_to_coef(0.0, i);
      }
    else if (p1.degree() == p2.degree())
      {
	for (int i=0; i<=p1.degree(); i++)
	  {
	    answer.assign_coef(p1.coefficient(i), i);
	    answer.add_to_coef((p2.coefficient(i)*-1), i);
	  }
      }
    else
      {
	for (int i=0; i<=p2.degree(); i++)
	  answer.assign_coef(p2.coefficient(i), i);
	for (int i=0; i<=p1.degree(); i++)
	  answer.add_to_coef((p1.coefficient(i)*-1), i);
	for (int i=0; i<=p2.degree(); i++)
	  answer.add_to_coef(0.0, i);
      }
    return answer;
  }

  polynomial operator *(const polynomial& p1, const polynomial& p2)
  {
    polynomial answer;
    int m = p1.degree();
    int n = p2.degree();
    answer.reserve(m+n);
    for (int i=0; i<=m+n; i++)
      answer.assign_coef(0.0, i);
    for (int i=0; i<=m; i++)
      {
	for (int j=0; j<=n; j++)
	  {
	    int cdegree = i+j;
	    double camount = 0.0;
	    camount = p1.coefficient(i) * p2.coefficient(j);
	    answer.add_to_coef(camount, cdegree);
	  }
      }
    return answer;
  }

  // NON-MEMBER OUTPUT FUNCTIONS
  ostream& operator <<(ostream& out, const polynomial& p)
  {
    if (p.degree() == -1)
      {
	out << 0;
	return out;
      }
    
    if (p.degree() == 0)
      {
	out << p.coefficient( p.degree() ) << "\n";
	return out;
      }

    out << p.coefficient( p.degree() ) << "x^" << p.degree();
    for (int i = p.degree()-1 ; i>= 0; i--)
      {
	if ( p.coefficient(i) < 0)
	  {
	    if (i == 0)
	      {
		out << " - " << p.coefficient(i)*-1;
	      }
	    else if (i == 1)
	      {
		out << " - " << p.coefficient(i)*-1 << "x";
	      }
	    else
	      {
		out << " - " << p.coefficient(i)*-1 << "x^" << i;
	      }
	  }
	else if ( p.coefficient(i) == 0)
	  {
	    NULL;
	  }
	else
	  {
	    if (i == 0)
	      {
		out << " + " << p.coefficient(i);
	      }
	    else if (i == 1)
	      {
		out << " + " << p.coefficient(i) << "x";
	      }
	    else
	      {
		out << " + " << p.coefficient(i) << "x^" << i;
	      }
	  }
      }
    out << "\n";
    return out;
  }

}
