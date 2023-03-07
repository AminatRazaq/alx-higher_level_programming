#!/usr/bin/python3
#97 to 122 is for lowercase
#recall the lastgit in range function is excluded
#"chr" returns the character that reps the specified unicode.
for alp in range(97, 123):
    if chr(alp) != 'q' and chr(alp) != 'e':
    print("{}".format(chr(alp)), end="")
