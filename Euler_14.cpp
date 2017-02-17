/*
    The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
    finish at 1.

    Which starting number, under one million, produces the longest chain?
    (Once the chain starts the terms are allowed to go above one million)

*/

#include <iostream>

using namespace std;

int main()
{
    unsigned int num, N, terms, mNum = 1, mTerms = 1;

    for (num = 1; num < 1000000; ++num)
    {
        N = num;
        terms = 1;

        while (N != 1)
        {
            if (N % 2 == 0)
                N /= 2;
            else
                N = 3*N + 1;
            ++terms;
        }

        if (terms > mTerms)
        {
            mTerms = terms;
            mNum = num;
        }
    }

    cout << "Number giving the longest chain = " << mNum;

    return 0;
}
