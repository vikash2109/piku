known_users=['Alice', 'Bob', 'Claire', 'Dam','Emma']

while True:
    print "Hi! My Name is Travis"
    name=raw_input("What is your name?:").strip().capitalize()

    if name in known_users:
        print 'Hello {}!'.format(name)

    else:
        print 'i dont think i have met you'
        
