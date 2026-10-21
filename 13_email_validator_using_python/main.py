PERMITS_RECIPIENT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
PERMITS_DOMAIN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
PERMITS_TOP = ['com', 'net', 'org', 'tech']

def validate(email):
    if not email.count('@') == 1:
        return "Email is invalid"

    recipient_name = email.split('@')[0]

    if len(recipient_name) > 24 or len(recipient_name) < 3:
        return "Email is invalid"

    for c in recipient_name:
        if c not in PERMITS_RECIPIENT:
            return "Email is invalid"

        if (
            '.' == recipient_name[0]
            or '.' == recipient_name[-1]
            or '_' == recipient_name[0]
            or '_' == recipient_name[-1]
        ):
            return "Email is invalid"


    after_at = (email.split('@')[1])

    domain_name = after_at.split('.')[0]

    if len(domain_name) > 12 or len(domain_name) < 3:
        return "Email is invalid"

    for c in domain_name:
        if c not in PERMITS_DOMAIN:
            return "Email is invalid"

    top_level_domain = after_at.split('.')[1]
    
    if top_level_domain not in PERMITS_TOP:
        return "Email is invalid"
    
    return 'Email is valid'

if __name__ == "__main__":
    email = input('Enter email:\n')
    call = validate(email)
    print(call)
