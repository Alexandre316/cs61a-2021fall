def email(s):
    """Return whether string s has form <name>@<domain> where <domain> ends in .___

    (Note: the actual rules for well-formed email addresses are much more complicated.)

    >>> email('oski@berkeley.edu')
    True
    >>> email('oski_bear@cs.berkeley.edu')
    True
    >>> email('oski@berkeley.EDU')
    True
    >>> email('oski@berkeley.cal')
    True
    >>> email('oski @berkeley.edu')
    False
    >>> email('oski@berkeley!.edu')
    False
    >>> email('oski!@berkeley.edu')
    False
    >>> email('oski@berkeley..edu')
    False
    >>> email('oski@berkeley.3du')
    False
    >>> email('oski@berkeley')
    False
    >>> email('oski@berkeley.info')
    False
    >>> email('oski@oski@berkeley.edu')
    False
    """
    def letter(c):
        return 'a' <= c.lower() and c.lower() <= 'z'
    def number(c):
        return '0' <= c  and c <= '9'
    def allowed(c):
        return c in ['@', '_', '.'] or letter(c) or number(c)
    if not all(map(allowed, s)): # No spaces or exclamation points
        return False
    parts = s.split('@')
    if len(parts) != 2: # Exactly one @
        return False
    domain_parts = parts[1].split('.')
    if len(domain_parts) <= 1: # At least one .
        return False
    if not all(domain_parts): # No two . in a row
        return False
    tld = domain_parts[-1]
    return len(tld) == 3 and all([letter(c) for c in tld])  # exactly three letters













import re


def email_regex(s):
    """Return whether string s has form <name>@<domain> where <domain> ends in .___

    (Note: the actual rules for well-formed email addresses are much more complicated.)

    >>> email_regex('oski@berkeley.edu')
    True
    >>> email_regex('oski_bear@cs.berkeley.edu')
    True
    >>> email_regex('oski@berkeley.EDU')
    True
    >>> email_regex('oski@berkeley.cal')
    True
    >>> email_regex('oski @berkeley.edu')
    False
    >>> email_regex('oski!@berkeley.edu')
    False
    >>> email_regex('oski@berkeley!.edu')
    False
    >>> email('oski@berkeley..edu')
    False
    >>> email_regex('oski@berkeley.3du')
    False
    >>> email_regex('oski@berkeley')
    False
    >>> email_regex('oski@berkeley.info')
    False
    >>> email_regex('oski@oski@berkeley.edu')
    False
    """
    return bool(re.fullmatch(r'\w+@(\w+\.)+[A-Za-z]{3}', s))

def groups_demo():
    """Groups demo

    >>> s = 'boskier graybeard'
    >>> m = re.fullmatch(r'b(.*)er.{5}(.*).', s)
    >>> m.group(0) == s
    True
    >>> m.group(1)
    'oski'
    >>> m.group(2)
    'bear'
    """

