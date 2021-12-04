from Booking.booking import Booking

try:

    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input("where to go to ?"))
        bot.select_dates(check_in_date=input("what is the check in date?"),
                         check_out_date=input("what is the check out date"))
        bot.select_adults(int(input("How many people")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh() # A work around to let our bot grab the data proper
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print("there is a problem running this program")
    else:
        raise