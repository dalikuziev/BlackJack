import random
from emoji import logo

i = 1
while True:
  user_card = []
  computer_card = []
  def one_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  def play():
    for n in range(2):
      user_card.append(one_card())
      computer_card.append(one_card())
    if sum(user_card) == 22:
      user_card[1] = 1
    if sum(computer_card) == 22:
      computer_card[1] = 1
    return f"sizning kartalaringiz {user_card[0]} va {user_card[1]} jami {sum(user_card)}, mening 1-kartam {computer_card[0]}, 2-si noma'lum"
  print(f"{i}-o'yiningiz")
  print(logo)
  print(play())
  while True:
    add_card = input("yana karta olasizmi? ha/yo'q: ")
    if add_card == "ha":
      new_user_card = one_card()
      user_card.append(new_user_card)
    else:
      break
    if sum(user_card) > 21:
      print(f"siz {new_user_card} ni oldingiz jami: {sum(user_card)} 😢")
      break
    print(f"siz {new_user_card} ni oldingiz va jami: {sum(user_card)} 🙂")
  print(f"meniki {computer_card[0]} va {computer_card[1]} jami: {sum(computer_card)} 🙂")
  def compare(user_card, computer_card):
    if sum(user_card) > 21:
      return "siz yutqazdingiz 😭😭😭"
    elif sum(computer_card) > 21:
      return "siz yutdingiz 😎😎😎"
    elif sum(user_card) < sum(computer_card):
      return "siz yutqazdingiz 😭😭😭"
    elif sum(user_card) == sum(computer_card):
      return "durrang 😐😐😐"
    else:
      return "siz yutdingiz 😎😎😎"
  while sum(user_card) > sum(computer_card):
    if sum(user_card) > 21:
      break
    new_computer_card = one_card()
    computer_card.append(new_computer_card)
    if sum(computer_card) > 21:
      print(f"men olgan yangi karta {new_computer_card} jami: {sum(computer_card)} 😢")
    else:
      print(f"men olgan yangi karta {new_computer_card} jami: {sum(computer_card)} 🙂")
  print(compare(user_card, computer_card))
  play_continue = input("yana o'ynisizmi? ha/yo'q: ")
  if play_continue == "ha":
    i += 1
  else:
    break
