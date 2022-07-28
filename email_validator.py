class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def is_domain_valid(d_main, valid_d_mains):
    result = True
    for valid_domain in valid_d_mains:
        if d_main.endswith(valid_domain):
            result = False
            break
        return result


mails = input()
username, domain = mails.split('@')
valid_domains = ['.com', '.bg', '.net', '.org']

while not mails == 'End':
    if len(username) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if '@' not in mails:
        raise MustContainAtSymbolError('Email must contain @')

    if is_domain_valid(domain, valid_domains):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print('Email is valid')
    mails = input()

