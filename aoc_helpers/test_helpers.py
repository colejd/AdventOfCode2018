def test(result, expected):
    if result == expected:
        print("Test passed.")
    else:
        print("Test failed! {0} != {1}".format(result, expected))