from observer_pattern import CheckSpec,FactoryMode


def main():
    fm:FactoryMode = FactoryMode(6.0)
    csp = CheckSpec(8.7, 3.3)
    fm.add_observer(csp)
    fm.point = 6.0
    fm.point = 2.0
    fm.point = 9.0


if __name__ == '__main__':
    main()