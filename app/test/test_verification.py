def test_pass_case():
    assert verify_receipt(valid_receipt) == "PASS"


def test_fail_case():
    assert verify_receipt(tampered_receipt) == "FAIL"