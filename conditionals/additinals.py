# if the num is div of 3 prit div of fizz
# if the num is div of 5 prit div of buzz
# if the num is div of both prit div of fizzbuzz
# if the num is not div of both prit div of not fizzbuzz
num=9
if num%3==0 and num%5==0:
    print('fizzbuzz')
elif num%5==0:
    print("buzz")
elif num%3==0 :
    print("fizz")
else:
    print('not fizzbuzz')