# from app.calculations import sum,multiply,divide,subtract,BackAccount
# import pytest 

# #avoid repetitions
# @pytest.fixture
# def zero_bank_account():
#     return BackAccount()

# @pytest.fixture
# def bank_account():
#     return BackAccount()

# def test_bank_amount(bank_account):
    
#     assert bank_account.balance==0

# def test_withdraw_amount(bank_account):
#     bank_account.Withdraw(0)
    
#     assert bank_account.balance==0


# @pytest.mark.parametrize("deposit,withdraw,result",[(4,3,1),(50,30,20),(50,5,45)])
# def test_multiple(bank_account,deposit,withdraw,result):
#     bank_account.Deposit(deposit)
    
#     bank_account.Withdraw(withdraw)
#     assert bank_account.balance==result

# def insufficient_funds(bank_account):
#     with pytest.raises(Exception):
#         bank_account.Withdraw(100)
        





# # multiple testing scenario
# @pytest.mark.parametrize("x,y,result",[(4,3,7),(5,6,11),(5,5,10)])
# def test_sum(x,y,result):
#     assert sum(x,y)==result


# def test_multiply():

#     assert multiply(4,3)==12
# test_multiply()

# def test_divide():

#     assert divide(12,3)==4
# test_divide()

# def test_subtract():

#     assert subtract(4,4)==0
# test_subtract()