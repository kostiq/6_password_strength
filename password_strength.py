import re
import argparse


def get_password_strength(password):
    good_len_pass = 21
    weak_len_pass = 8
    pass_lvl_up = 2
    if len(password) < weak_len_pass:
        return 1

    pass_legth_and_strength = round(
        (len(password) % good_legth_pass)/weak_len_pass, 1)
    if re.search('[A-Z]', password):
        pass_legth_and_strength += pass_lvl_up
    if re.search('[0-9]', password):
        pass_legth_and_strength += pass_lvl_up
    if re.search('[\W]', password):
        pass_legth_and_strength += pass_lvl_up
    return pass_legth_and_strength


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--password', help="Input your password", type=str, required=True)

    args = parser.parse_args()
    print ('Strength your password is:', get_password_strength(args.password))
