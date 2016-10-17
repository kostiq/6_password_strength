import re
import argparse


def get_password_strength(password):
    if len(password) < 8:
        return 1
    result = round((len(password) % 21)/7 + 1, 1)
    if re.search('[A-Z]', password):
        result += 2
    if re.search('[0-9]', password):
        result += 2
    if re.search('[\W]', password):
        result += 2
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--password', help="Input your password", type=str, required=True)

    args = parser.parse_args()
    print ('Strength your password is:', get_password_strength(args.password))
