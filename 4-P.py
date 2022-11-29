# COMP.CS.100 The thirth Python program.
# Creator: Hamed Talebian
# Student id number: 150360360

study_benefit = input("Enter the amount of the study benefits: ")
study_benefit_num = float(study_benefit)
index_raise = 1.17 / 100
index_raise_o = 0.02353689000000007
study_benefit_raise = study_benefit_num + (study_benefit_num * index_raise)
study_benefit_raise_o = study_benefit_num + (study_benefit_num * index_raise_o)
print('If the index raise is 1.17 percent, the study benefit,')
print('after a raise, would be', round(study_benefit_raise, 10), 'euros')
print('and if there was another index raise, the study')
print('benefits would be as much as', study_benefit_raise_o, 'euros')
