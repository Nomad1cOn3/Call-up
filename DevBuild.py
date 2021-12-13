import sys,time,random,os

begin = 0 #begin input variable
supportChoice = 0 #support choice variable
choice = 0 #global choice variable
aware = 0 #displays starting sentence "suddenly aware etc."
walked_back = 0 #modfies values when walking backwards
menu_count = 4 #used to display error range of acceptable responses
house = 0
mailbox = 0 #communicates if mailbox has been searched
car = 0 #communicates if car has been searched
walker_counter = 0 #displays house counter
walk_midder = 0 #communicates to walker_counter
houseIntroDone = 0 #controls house intro display


typing_speed = 100 #wpm

def slowprint(t): #typing sim function
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def fastprint(t): #image printing function
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*5.0/typing_speed)
    print('')

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def start(): #prints intro screen
  slowprint('Welcome to Call Up - A Text Adventure Game!')
  slowprint(' ')
  slowprint(' ')
  fastprint('         ____________')  
  fastprint('       /   ,,____,,   \:.')
  fastprint('       |__| [][][] |__|:  :')
  fastprint('         /  [][][]  \   :  :')
  fastprint('        /   [][][]   \   :  :')
  fastprint('       /    [][][]    \   ..')
  fastprint('======|________________|')
  slowprint(' ')
  slowprint(' ')
  slowprint(' ')
  slowprint('A game by Benjamin Ostroff')
  slowprint(' ')
  slowprint('----------------')
  slowprint(' ')
  slowprint('Press 1 to begin, or')
  slowprint(' ')
  slowprint('Press 2 for customer support...')
  slowprint(' ')

def easteregg742(): #easter egg shhhhhhhh
    slowprint('Suddenly all your surroundings are different.')
    slowprint('You are standing in front of a house painted pink.')
    slowprint('There is a small garage attached to the left side')
    slowprint('of the house. ')
    slowprint('The house number is different from all the')
    slowprint("others you've walked past. It is 742.")
    slowprint('You look around and notice that a street sign in')
    slowprint('the distance. It says "Evergreen Terrace"')
    slowprint('')
    slowprint(' ')
    fastprint('   * ')
    fastprint('    *  *')
    fastprint('       *     ')
    fastprint('     [-]     ')                                   
    fastprint('     [-]___________________ ')                          
    fastprint('     [-]^=^-^-^=^-^^=^-^-^-\      ')             
    fastprint('    /^-^-^-^-^-^-^-^-^-^-^-^\________  ')               
    fastprint('    |  [///]        [///]   |-^-^-^-^\     ')
    fastprint('    |                       |-^-^-^-^-\ ')
    fastprint('    |   [}{]  .==.  [}{]    |---------|')
    fastprint('  ^^|   [}{]  |LI|  [}{]    |---------|')
    fastprint('  &&|_________|__|__________|---------|    ')        
    fastprint('               ====          \         \ ')
    fastprint('                 ====         \         \ ')
    fastprint('                               \         \  ')
    slowprint('(25th house)')
    slowprint(' ')
    slowprint(' ')
    slowprint('--------------------')
    slowprint(' ')
    slowprint('Press 1 to walk down the street')
    slowprint('Press 2 to go back to the previous house')

def intro(): #global intro screen/main menu
  if walker_counter == 24:
    easteregg742()
  else:
    if aware == 0:
      slowprint('You suddenly become aware of your surroundings.')
    slowprint('You are standing in front of a white house,')
    slowprint('with a red car in the driveway, and a blue mailbox.')
    slowprint('There are copies of the house, car, and mailbox')
    slowprint('for as far as you can see.')
    slowprint('You can vaguely see the house number, which is 0.')
    slowprint('Strange.')
    slowprint(' ')
    fastprint('                )')                 
    fastprint('               (')           
    fastprint('       ________[]_')            
    fastprint('      /^=^-^-^=^-^\ ')   
    fastprint('     /^-^-^-^-^-^-^\ ')
    fastprint('    /__^_^_^_^^_^_^_\ ')
    fastprint('     |  .==.       |       ___')
    fastprint('   ^^|  |LI|  [}{] |^^^^^ /___\ ^^^^')
    fastprint('   &&|__|__|_______|&&   ." | ". ')
    fastprint('        ====       =     (o_|_o)    ')
    fastprint('         ====      |      u   u       ')
    if walker_counter > 0:
      if walker_counter == 1:
        slowprint('(2nd house)')
      elif walker_counter == 2:
        slowprint('(3rd house)')
      elif walker_counter == 21:
        slowprint('22nd house')
      elif walker_counter == 22:
        slowprint('23rd house')
      elif walker_counter == 31:
        slowprint('22nd house')
      elif walker_counter == 32:
        slowprint('23rd house')
      elif walker_counter == 41:
        slowprint('22nd house')
      elif walker_counter == 42:
        slowprint('23rd house')
      elif walker_counter == 51:
        slowprint('22nd house')
      elif walker_counter == 52:
        slowprint('23rd house')
      elif walker_counter == 61:
        slowprint('22nd house')
      elif walker_counter == 62:
        slowprint('23rd house')
      elif walker_counter == 71:
        slowprint('22nd house')
      elif walker_counter == 82:
        slowprint('23rd house')
      elif walker_counter == 91:
        slowprint('22nd house')
      elif walker_counter == 92:
        slowprint('23rd house')
      elif walker_counter > 2:
        print('( '"{}"'th house )'.format(walker_counter+1))
    slowprint(' ')
    slowprint(' ')
    slowprint('--------------------')
    slowprint(' ')
    if walker_counter == 0:
      if car == 0:
        if mailbox == 1:
          slowprint('Press 1 to search the car')
          slowprint('Press 2 to approach the house')
          slowprint('Press 3 to walk down the street')
        elif mailbox == 0:
          slowprint('Press 1 to search the mailbox')
          slowprint('Press 2 to search the car')
          slowprint('Press 3 to approach the house')
          slowprint('Press 4 to walk down the street')
      if car == 1:
        if mailbox == 0:
          slowprint('Press 1 to search the mailbox')
          slowprint('Press 2 to approach the house')
          slowprint('Press 3 to walk down the street')
      if mailbox == 1 and car == 1:
        slowprint('Press 1 to approach the house')
        slowprint('Press 2 to walk down the street')
    elif walker_counter > 0:
      if car == 1:
        if mailbox == 0:
          slowprint('Press 1 to search the mailbox')
          slowprint('Press 2 to approach the house')
          slowprint('Press 3 to walk down the street')
          slowprint('Press 4 to go back to previous house.')
      if car == 0:
        if mailbox == 1:
          slowprint('Press 1 to search the car')
          slowprint('Press 2 to approach the house')
          slowprint('Press 3 to walk down the street')
          slowprint('Press 4 to go back to the previous house.')
        elif mailbox == 0:
          slowprint('Press 1 to search the mailbox')
          slowprint('Press 2 to search the car')
          slowprint('Press 3 to approach the house')
          slowprint('Press 4 to walk down the street')
          slowprint('Press 5 to go back to the previous house.')
      if mailbox == 1 and car == 1:
        slowprint('Press 1 to approach the house')
        slowprint('Press 2 to walk down the street')
        slowprint('Press 3 to go back to the previous house.')

def menu(list, question): #i have no idea what this does
	for item in list:
		print(list.index(item), item)

	while True:
		result = input(question)
		try:
			result = int(result)
			break
		except: 
			print("Selection must be whole number between 0-9:")

	return result

def Mailbox(mailbox): #mailbox code
  choice = 0
  clear()
  slowprint("You open the mailbox and peek inside.")
  slowprint("A letter rests at the back of the mailbox.")
  slowprint('You are unsure if you want to read it or not.')
  slowprint(' ')
  slowprint(' ')
  fastprint('          ..--""|')
  fastprint('          |     |')
  fastprint("          | .---'")
  fastprint('    (\-.--| |---------.')
  fastprint('   / \) \ | |          \ ')
  fastprint('   |:.  | | |           |')
  fastprint('   |:.  | |o|           |')
  fastprint('   |:.  | `"`           |')
  fastprint('   |:.  |_ __  __ _  __ /')
  fastprint('   `""""`""|=`|"""""""`')
  fastprint('           |=_|')
  fastprint('           |= |')
  slowprint(' ')
  slowprint(' ')
  slowprint('--------------------')
  slowprint(' ')
  slowprint('Press 1 to take the letter')
  slowprint('Press 2 to close the mailbox')
  slowprint(' ')
  slowprint(' ')
  while True:
    if choice == 1:
      choice = 0
      break
    while True:
      if choice == 1:
        break
      choice = 0
      choice = input()
      try:
        choice = int(choice)
        slowprint(' ')
      except Exception:
        slowprint(' ')
        slowprint('Selection must be whole number between 1-2:')
        slowprint(' ')
        continue
      if choice == 1:
        clear()
        slowprint('You pick up the letter and look at the address')
        slowprint('written on the front.')
        slowprint('It reads: "To New Arrival"')
        slowprint('You open the envelope and remove the letter.')
        slowprint('The letter contains but a single word: Explore')
        slowprint(' ')
        slowprint(' ')
        fastprint('    __________________')
        fastprint('   | \              / | ')
        fastprint('   |\                /|')
        fastprint('   | /\____________/\ | ')
        fastprint('   |/                \| ')
        fastprint('   |__________________| ')
        slowprint(' ')
        slowprint(' ')
        slowprint('--------------------')
        slowprint(' ')
        slowprint('Press 1 to continue')
        slowprint(' ')
        slowprint(' ')
        while True:
          choice = 0
          choice = input()
          slowprint(' ')
          try:
            choice = int(choice)
          except Exception:
            slowprint('Selection must be whole number between 1-1')
            slowprint(' ')
            continue
          if choice == 1:
            slowprint('You close the mailbox and walk away.')
            time.sleep(1)
            return(1)
            break
          else:
            slowprint('Selection must be whole number between 1-1')
            slowprint(' ')

      elif choice == 2:
        slowprint(' ')
        time.sleep(1)
        slowprint('You close the mailbox and walk away.')
        slowprint(' ')
        return(0)
        break
      
      else:
        slowprint('Selection must be whole number between 1-2:')
        slowprint(' ')

def Car(car): #car code
  choice = 0
  clear()
  slowprint("You approach the car. ")
  slowprint('Perhaps you could drive away and find') 
  slowprint('someone else.')
  slowprint('You try the doors and find them unlocked.')
  slowprint('You wonder if the previous owner may have') 
  slowprint('hidden the keys somewhere.')
  slowprint(' ')
  slowprint(' ')
  fastprint('   ---------------------------.')
  fastprint(' `/""""/""""/ |""|  |""""""|   \.')
  fastprint(' /    /    /  |__|  |______|    |')
  fastprint('/----------=====================|')
  fastprint('| \  /V\  /    _.               |')
  fastprint('|()\ \W/ /()   _            _   |')
  fastprint('|   \   /     / \          / \  |')
  fastprint('=C========C==_| ) |--------| ) _/==]')
  fastprint(' \_\_/__..  \_\_/_ \_\_/ \_\_/__.__.')
  slowprint(' ')
  slowprint(' ')
  slowprint('--------------------')
  slowprint(' ')
  slowprint('Press 1 to search around the car')
  slowprint('Press 2 to walk away')
  slowprint(' ')
  slowprint(' ')
  while True:
    if choice == 1:
      choice = 0
      break
    while True:
      choice = 0
      choice = input()
      try:
        choice = int(choice)
      except:
        slowprint(' ')
        slowprint('Selection must be whole number between 1-2:')
        slowprint(' ')
        continue
      if choice == 1:
        clear()
        slowprint('You check in the sun visor. ')
        slowprint('The keys fall into your lap.')
        slowprint('Attached to the key is a note that says:')
        slowprint('"Don'"'"'t run".')
        slowprint("Perhaps you'd better look around before")
        slowprint('you drive away. ')
        slowprint(' ')
        slowprint(' ')
        fastprint('   .--.')
        fastprint("  /.-. '----------.")
        fastprint("  \ '-' .----'-''-'")
        fastprint("   '--'")
        slowprint(' ')
        slowprint(' ')
        slowprint('--------------------')
        slowprint(' ')
        slowprint('Press 1 to continue')
        slowprint(' ')
        slowprint(' ')
        while True:
          choice = 0
          choice = input()
          slowprint(' ')
          try:
            choice = int(choice)
          except:
            slowprint('Selection must be whole number between 1-1')
            slowprint(' ')
            continue
          if choice == 1:
            slowprint('You walk away from the car.')
            time.sleep(1)
            return(1)
            break
          else:
            slowprint('Selection must be whole number between 1-1')
            slowprint(' ')

      elif choice == 2:
        slowprint(' ')
        slowprint('You walk away from the car.')
        time.sleep(1)
        slowprint(' ')
        return(0)
        break
    
      else:
        slowprint(' ')
        slowprint('Selection must be whole number between 1-2:')
        slowprint(' ')
  
def house(choice): #code for house
  choice = 0
  clear()
  slowprint("You approach the house. ")
  slowprint("As you noticed earlier the house number is 0.")
  slowprint('You try the door knob, to find it unlocked.')
  slowprint('You are unsure if going inside is a good idea.') 
  slowprint(' ')
  slowprint(' ')
  fastprint('              ________')
  fastprint('             / ______ \ ')
  fastprint('             || _  _ ||')
  fastprint('             ||| || |||  ___')
  fastprint('             |||_||_||| | 0 |')
  fastprint('             || _  _o|| | • |')
  fastprint('             ||| || ||| |___|')
  fastprint('             |||_||_|||      ')
  fastprint('             ||______||     ')
  fastprint('            /__________\   ')
  fastprint('____________|__________|___________')
  fastprint('           /____________\ ')
  fastprint('           |____________|')
  slowprint(' ')
  slowprint(' ')
  slowprint('--------------------')
  slowprint(' ')
  slowprint('Press 1 to go inside the house')
  slowprint('Press 2 to walk away')
  slowprint(' ')
  slowprint(' ')
  while True:
    if choice == 1:
      choice = 0
      break
      if choice == 1:
        choice = 0
        break
  
    while True:
      choice = 0
      choice = input()
      try:
        choice = int(choice)
      except:
        slowprint('Selection must be whole number between 1-2:')
      if choice == 1:
        clear()
        slowprint('You turn the doorknob and push the door')
        slowprint('open. ')
        slowprint('On your left is a stairway heading upwards,')
        slowprint('and on your right is a empty room.')
        slowprint('Ahead is a hallway leading to some more rooms.')
        slowprint('The walls appear barren and are painted')
        slowprint('a light shade of off-white.')
        slowprint('')
        slowprint(' ')
        slowprint(' ')
        slowprint('--------------------')
        slowprint(' ')
        slowprint('Press 1 to continue')
        slowprint(' ')
        slowprint(' ')
        break
      elif choice == 2:
        slowprint(' ')
        slowprint('You walk away from the house.')
        time.sleep(1)
        break
    if choice == 1:
      choice = 0
      while True:
        choice = input()
        slowprint(' ')
        try:
          choice = int(choice)
        except:
          slowprint('Selection must be whole number between 1-1')
        if choice == 1:
          return(1)
        
        else:
          slowprint('Selection must be whole number between 1-1')
          slowprint(' ')
          continue

    elif choice == 2:
      return(0)
      break

    else:
      slowprint('Selection must be whole number between 1-2:')

def walk_down(walk_midder): #controls walking down the street
  choice = 0
  clear()
  slowprint('You walk down the sidewalk to the next house.')
  slowprint('The house looks identical to the one you just left.')
  slowprint('The same red car and blue mailbox.')  
  slowprint('The house is also labeled 0, very odd.')
  slowprint(' ')
  slowprint(' ')
  slowprint('--------------------')
  slowprint(' ')
  slowprint('Press 1 to continue')
  slowprint('Press 2 to go back to the previous house.')
  slowprint(' ')
  slowprint(' ')
  while True:
    choice = input()
    slowprint(' ')
    try:
      choice = int(choice)
    except:
      slowprint('Selection must be whole number between 1-2')
    if choice == 1:
      return(1)
      break
    elif choice == 2:
      slowprint('You walk back to the previous house.')
      time.sleep(1)
      return(2)
      break
    elif choice == 404:
      return(3)
      break
    else:
      slowprint('Selection must be whole number between 1-2')

def walk_back(): #controls walking backwards down the street
  clear()
  slowprint('You walk back to the previous house.')
  slowprint(' ')
  slowprint(' ')
  slowprint('--------------------')
  slowprint(' ')
  slowprint('Press 1 to continue')
  slowprint(' ')
  slowprint(' ')
  while True:
    choice = input()
    slowprint(' ')
    try:
      choice = int(choice)
    except:
      slowprint('Selection must be whole number between 1-1')
    if choice == 1:
      break
    else:
      slowprint('Selection must be whole number between 1-2')
      continue

def Phone(code): #will control phone input
  slowprint('You pick up the phone and hear an eerie dial tone,')
  slowprint(' than you hear "Enter a number..." from a deep voice.')
  slowprint('It must be the operator,'" you'd" 'better enter')
  slowprint('a number quickly.')
  while True:
	  try:
		  option1 = int(input("Digit one: "))
		  break
	  except:
		  slowprint("Digit one must be a whole number between 0-9:")

  while True:
	  try:
		  option2 = int(input("Digit two: "))
		  break
	  except:
		  slowprint("Digit two must be a whole number between 0-9:")

  while True:
	  try:
		  option3 = int(input("Digit three: "))
		  break
	  except:
		  slowprint("Digit three must be a whole number between 0-9:")
  chosenCode = int(str(option1) + str(option2) + str(option3))
  slowprint("")
  if chosenCode == code:
	  slowprint("You hear a click, and the padlock shifts. As you press open the door a rush of fresh, warm air caresses your face. At last, you are free.")
	  return (1)
  else:
	  slowprint("You jiggle the padlock, but to no avail. The code is incorrect.")
	  return(0)

while True: #main game loop init
  if begin == 1:
    break
  #typing_speed = 125
  typing_speed = 5000
  clear()
  start()
  while True:
    if supportChoice == '#':
      supportChoice = 0
      break
    begin = input()
    try:
      begin = int(begin)
      if begin == 1:
        clear()
        break
      elif begin == 2:
        clear()
        supportChoice = 0
        while True:
          clear() #support menu
          slowprint('------- Support -------')
          slowprint(' ')
          slowprint("The game is played by reading the story")
          slowprint('and entering numbers to progress foward.')
          slowprint('The goal of the game is to find a phone') 
          slowprint('number and call it...')
          slowprint("The rest you'll have to figure out for yourself...")
          slowprint("Have fun! ")
          slowprint(' ')
          typing_speed = 40
          time.sleep(1)
          slowprint("Or don't...")
          time.sleep(1)
          typing_speed = 125
          slowprint(' ')
          slowprint(' ')
          slowprint('--------------')
          slowprint(' ')
          slowprint('Press # to go back')
          while True:
            slowprint(' ')
            supportChoice = input()
            if supportChoice == '#':
              clear()
              break
            else:
              slowprint(' ')
              slowprint('Selection must be #: ')
              slowprint(' ')
              continue
          if supportChoice == '#':
            slowprint(' ')
            slowprint(' ')
            break
      else:
        slowprint(' ')
        slowprint("Selection must be whole number between 1-2:")
        slowprint(' ')
    except Exception:
      slowprint(' ')
      slowprint("Selection must be whole number between 1-2: ")
      slowprint(' ')
while True: #second main game loop init
  if menu_count == 2: #determines what the error message will shows
      menu_count = '2:'
  if menu_count == 3:
      menu_count = '3:'
  if menu_count == 4:
      menu_count = '4:'
  if menu_count == 5:
      menu_count = '5:'
  if walked_back == 1:
    walked_back = 0
    walk_back()
  slowprint(' ')
  #typing_speed = 60
  clear()
  intro()
  aware = aware+1
  slowprint(' ')
  slowprint(' ')
  choice = 0
  while True:
    if choice == 6:
      choice == 0
      break
    try:         #actual game stuff below here
                 #controls what menu options are accepted based on what is displayed
      choice = int(input())
      if walker_counter == 0:
        if car == 0:
            if mailbox == 1:
              if choice == 1:
                car = Car(0)
                continue
              elif choice == 2:
                houseIntroDone = house(choice)
              elif choice == 3: 
                walk_midder = walk_down(0)
                if walk_midder == 1:
                  walker_counter = walker_counter+1
                elif walk_midder == 0:
                  walker_counter = walker_counter
                elif walk_midder == 2:
                  if walker_counter == 0:
                    walker_counter = walker_counter
                  elif walker_counter > 0:
                    walker_counter = walker_counter-1
            elif mailbox == 0:
              if choice == 1:
                mailbox = Mailbox(0)
                continue
              elif choice == 2:
                car = Car(0)
                continue
              elif choice == 3:
                houseIntroDone = house(choice)
              elif choice == 4: 
                walk_midder = walk_down(0)
                if walk_midder == 1:
                  walker_counter = walker_counter+1
                elif walk_midder == 0:
                  walker_counter = walker_counter
                elif walk_midder == 2:
                  if walker_counter == 0:
                    walker_counter = walker_counter
                  elif walker_counter > 0:
                    walker_counter = walker_counter-1
                elif walk_midder == 3:
                  walker_counter = 24
              else:
                slowprint(' ')
                print('Selection must be whole number between 1 and',menu_count)
                slowprint(' ')
        if car == 1:
          if mailbox == 0:
              if choice == 1:
                mailbox = Mailbox(0)
                continue
              elif choice == 2:
                houseIntroDone = house(choice)
              elif choice == 3: 
                walk_midder = walk_down(0)
                if walk_midder == 1:
                  walker_counter = walker_counter+1
                elif walk_midder == 0:
                  walker_counter = walker_counter
                elif walk_midder == 2:
                  if walker_counter == 0:
                    walker_counter = walker_counter
                  elif walker_counter > 0:
                    walker_counter = walker_counter-1
        if mailbox == 1 and car == 1:
            if choice == 1:
              houseIntroDone = house(choice)
            elif choice == 2: 
              walk_midder = walk_down(0)
              if walk_midder == 1:
                walker_counter = walker_counter+1
              elif walk_midder == 0:
                walker_counter = walker_counter
              elif walk_midder == 2:
                if walker_counter == 0:
                  walker_counter = walker_counter
                elif walker_counter > 0:
                  walker_counter = walker_counter-1
      
      elif walker_counter == 24:
            if choice == 1: 
              walk_midder = walk_down(0)
              if walk_midder == 1:
                walker_counter = walker_counter+1
              elif walk_midder == 0:
                walker_counter = walker_counter
              elif walk_midder == 2:
                if walker_counter == 0:
                  walker_counter = walker_counter
                elif walker_counter > 0:
                  walker_counter = walker_counter
            elif choice == 2:
              walker_counter = walker_counter-1
              walked_back = 1

      elif walker_counter > 0:
        if car == 0:
            if mailbox == 1:
              if choice == 1:
                car = Car(0)
                continue
              elif choice == 2:
                houseIntroDone = house(choice)
              elif choice == 3: 
                walk_midder = walk_down(0)
                if walk_midder == 1:
                  walker_counter = walker_counter+1
                elif walk_midder == 0:
                  walker_counter = walker_counter
                elif walk_midder == 2:
                  if walker_counter == 0:
                    walker_counter = walker_counter
                  elif walker_counter > 0:
                    walker_counter = walker_counter
              elif choice == 4:
                walker_counter = walker_counter-1
                walked_back = 1
            elif mailbox == 0:
              if choice == 1:
                mailbox = Mailbox(0)
                continue
              elif choice == 2:
                car = Car(0)
                continue
              elif choice == 3:
                houseIntroDone = house(choice)
              elif choice == 4: 
                walk_midder = walk_down(0)
                if walk_midder == 1:
                  walker_counter = walker_counter+1
                elif walk_midder == 0:
                  walker_counter = walker_counter
                elif walk_midder == 2:
                  if walker_counter == 0:
                    walker_counter = walker_counter
                  elif walker_counter > 0:
                    walker_counter = walker_counter
              elif choice == 5:
                walker_counter = walker_counter-1
                walked_back = 1
        if car == 1:
          if mailbox == 0:
              if choice == 1:
                mailbox = Mailbox(0)
                continue
              elif choice == 2:
                houseIntroDone = house(choice)
              elif choice == 3: 
                walk_midder = walk_down(0)
                if walk_midder == 1:
                  walker_counter = walker_counter+1
                elif walk_midder == 0:
                  walker_counter = walker_counter
                elif walk_midder == 2:
                  if walker_counter == 0:
                    walker_counter = walker_counter
                  elif walker_counter > 0:
                    walker_counter = walker_counter
              elif choice == 4:
                walker_counter = walker_counter-1
                walked_back = 1
        if mailbox == 1 and car == 1:
            if choice == 1:
              houseIntroDone = house(choice)
            elif choice == 2: 
              walk_midder = walk_down(0)
              if walk_midder == 1:
                walker_counter = walker_counter+1
              elif walk_midder == 0:
                walker_counter = walker_counter
              elif walk_midder == 2:
                if walker_counter == 0:
                  walker_counter = walker_counter
                elif walker_counter > 0:
                  walker_counter = walker_counter
            elif choice == 3:
              walker_counter = walker_counter-1
              walked_back = 1
    except Exception:
      if mailbox == 1 or car == 1:
        menu_count = 3
      if mailbox == 1 and car == 1:
        menu_count = 2
      if walker_counter > 0:
        menu_count = 5
        if mailbox == 1 and car == 1:
          menu_count = 3
        elif mailbox == 1 or car == 1:
          menu_count = 4
      slowprint(' ')
      if menu_count == 2:
        menu_count = '2:'
      if menu_count == 3:
        menu_count = '3:'
      if menu_count == 4:
        menu_count = '4:'
      if menu_count == 5:
        menu_count = '5:'
      slowprint(' ')
      print('Selection must be whole number between 1 and',menu_count)
      time.sleep(1)
      continue
    choice = 6
