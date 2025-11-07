# Add weekend detection program based on country input
# get the country name
contry = input("Enter contry name: ").lower()

# lists of countries and their weekends
countries_fri_sat = ['egypt', 'saudi arabia', 'ksa', 'kuwait']
countris_sat_sun = ['australia', 'usa', 'united states',
'united kingdom', 'uk']

if contry in countries_fri_sat:
    print(f'friday and sunday are the weekends in {contry.title()}')
elif contry in countris_sat_sun:
    print(f'saturday and sunday are the weekend in {contry.title()}')
else :
    print('sorry, I don\'t know')