import argparse

from atbashmmxx import core


def main():
    parser = _build_parser()
    args = parser.parse_args()
    if args.cipher:
        output = args.func(args)
        print(output)
    else:
        parser.print_help()


def _build_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="ciphers", dest="cipher")

    # ROTBASH
    rotbash_parser = subparsers.add_parser('rotbash', help='Rotbash')
    _build_text_rotate_argument(rotbash_parser)
    rotbash_parser.set_defaults(func=_rotbash_command)

    # KEYBASH
    keybash_parser = subparsers.add_parser('keybash', help='Keybash')
    _build_text_key_argument(keybash_parser)
    keybash_parser.set_defaults(func=_keybash_command)

    return parser


def _build_text_rotate_argument(parser):
    parser.add_argument('text')
    parser.add_argument('-r', '--rotate', type=int, default=0)


def _build_text_key_argument(parser):
    parser.add_argument('text')
    parser.add_argument('-k', '--key', type=str, default=' ')


def _rotbash_command(args):
    rotbash = core.Rotbash(args.rotate)
    return rotbash.cipher(args.text)


def _keybash_command(args):
    keybash = core.Keybash(args.key)
    return keybash.cipher(args.text)
