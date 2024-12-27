from instagram import Instagram
account = Instagram()
account.set_driver()
account.login()
username = input("Enter the username you want to follow: ")
account.search_account(username)
no_of_followers = int(input("Enter no of users you want to follow: "))
account.follow(no_of_followers)