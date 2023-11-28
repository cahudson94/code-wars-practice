"""
We have the following recursive function:

f(0) = 1, f(1) = 1, f(2) = 2, f(3) = 2, f(4) = 3, f(5) = 3

f(n) = f(n - 1) * f(n - 2) * f(n - 3) - f(n - 4) * f(n - 5) * f(n - 6)

The 15-th term; f(14) is the first term in having more that 100 digits.

In fact,

f(14) = 2596253046576879973769082409566059879570061514363339324718953988724415850732046186170181072783243503881471037546575506836249417271830960970629933033088

It has 151 digits.

Make the function something_acci(), that receives num_dig (number of digits of the value) as unique argument.

something_acci() will output a tuple/array with the ordinal number in the sequence for the least value in having equal or more than the given number of digits.

Let's see some cases:

something_acci(20) == (12, 25)
# f(11) = 1422313222839141753028416

something_acci(100) == (15, 151)

The number of digits given will be always more than 5. num_dig > 5.

Happy coding!!!

And the name for this kata? You have three words of the same meaning in Asian Languages.
"""

def something_acci(num_digits):
	a, b, c, d, e, f = 1, 1, 2, 2, 3, 3
	n = 6
	while len(str(f)) < num_digits:
		n += 1
    	a, b, c, d, e, f = b, c, d, e, f, (d * e * f - a * b * c)
    return n, len(str(f))
