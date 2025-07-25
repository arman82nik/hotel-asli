from validation import*


assert name_checker("ali") == True
assert name_checker("mohammad") == True
assert name_checker("ali123") == False
assert name_checker("") == False
assert name_checker("1234") == False

assert family_checker("mohammadi") == True
assert family_checker("nikjafarian") == True
assert family_checker("nikjafarian123") == False
assert family_checker("") == False
assert family_checker("1234") == False

assert code_checker("12345") == True
assert code_checker("456987") == True
assert code_checker("a123") == False
assert code_checker("") == False



assert postalcode_checker("12345") == True
assert postalcode_checker("456987") == True
assert postalcode_checker("a123") == False
assert postalcode_checker("") == False

assert mobile_checker("09124590422") == True
assert mobile_checker("09054590421") == True
assert mobile_checker("9124590422") == False
assert mobile_checker("") == False
assert mobile_checker("9124590422a") == False


assert email_checker("arman2246@gmail.com") == True
assert email_checker("arm1234@gmail.com") == True
assert email_checker("arm123gmail.com") == False
assert email_checker("") == False
assert email_checker("098765") == False

print("All Tests PASSED")

