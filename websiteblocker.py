host_path="hosts"
redirect="127.0.0.1"

website_list=["www.google.com","www.facebook.com","www.twitter.com"]
with open(host_path, 'r+') as file :
    content = file.read()
    for site in website_list:
        if site not in content:
            file.write(redirect+" "+ site+ "\n")