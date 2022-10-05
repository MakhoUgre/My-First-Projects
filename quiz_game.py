print('wecome to my computer quiz !')

playing =input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()
print("Okay! Let's play: )")
score = 0

answer = input ('what dose CUP stand for? ')
if answer.lower() == 'central processing unit' :
    print ('correct!')
    score += 1
else:
    print('Incorrect!')

answer = input ('what dose GPU stand for? ')
if answer.lower() == 'graphics processing unit' :
    print ('correct!')
    score += 1
else:
    print('Incorrect!')

answer = input ('what dose RAM stand for? ')
if answer.lower() == 'random access memory' :
    print ('correct!')
    score += 1
else:
    print('Incorrect!')

answer = input ('what dose PSU stand for? ')
if answer.lower() == 'power supply' :
    print ('correct!')
    score += 1
else:
    print('Incorrect!')
print('You got ', (score), 'questions correct!' )
print('You got ', str((score / 4) * 100), '% !' )