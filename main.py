
class Regression(object):
    def lev(self, a, b):
        if not a:
            return len(b)
        if not b:
            return len(a)
        return min(self.lev(a[1:], b[1:]) + (a[0] != b[0]),
                   self.lev(a[1:], b) + 1,
                   self.lev(a, b[1:]) + 1)


def main():
    regression = Regression()
    print(regression.lev("dupadupa", "dupadupadupa"))


if __name__ == '__main__':
    main()
