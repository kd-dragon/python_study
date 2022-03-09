def person(name, **kwargs):
    for key, value in kwargs.items():
        print(f"key={key}, value={value}")


person('kdy', city='SEOUL', mobile='010-2423-9481', age=31)

# 매개변수 우선순위!

#일반변수 > *args > **kwargs
def abc(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

abc(1, 2, 3, 4, 5, id="kdy",pwd=1234)