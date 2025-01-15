import random
import time

#moduł random umozliwia wprowadzenie do programu elementow losowych
#funkcja input() umożliwia użytkownikowi udzielanie odpowiedzi
#pętle while = True, które pojawiają sie w fragmentach kodu, zawierających wybór użytkownika mają na celu powtarzanie danego fragmentu poki uzytkownik nie udzieli odpowiedzi na pytanie, funkcja break wychodzi z pętli
#funkcja time.sleep() zostala przeze mnie wykorzystana w dalszej czesci kodu, aby użytkownik mógł się wczuć w rozgrywkę
#funkcja lower() przy zmiennych podawanych przez uzytkownika gwarantuje ze wielkosc liter podawanych odpowiedzi nie ma znaczenia
#Funkcja print(f"") została użyta aby w wiadomosci tekstowej uwzględnić zmienną podaną przez użytkownika
#konstrukcja \033[1m{imie}\033[0m ma na celu pogrubienie imienia podanego przez użytkownika, tak aby wyróżniało się w drukowanym tekscie

#funkcja animowany_dialog sprawia ze printowane komunikaty wygladaja jak animacja dialogu z gry komputerowej
def animowany_dialog(tekst):
    for znak in tekst: #funkcja wykoncuje operację dla każdej literki i znaku białego w tekście
        print(znak,end ="", flush = True)  #end="" unika drukowania każdego znaku w następnej linijce, flush=True powoduje ze znaki drukuja sie od razu bez opoznienia
        time.sleep(0.05)
    print()  

#Wiadomości startowe
animowany_dialog("\nWitaj użytkowniku!")
time.sleep(1)
animowany_dialog("Na wstępie konieczne jest przeprowadzenie weryfikacji celem uniknięcia udziału niepożądanych osób.")
print("---------------------------------------Naciśnij Enter aby kontynuować---------------------------------------")
input()

#pętla wymuszająca odpowiedź użytkowanika na pytanie startowe
while True:
  animowany_dialog("Czy jesteś studentem Politechniki Gdańskiej?\nOdpowiedz TAK lub NIE:")
  wybor_poczatkowy = input("> ")
  if wybor_poczatkowy.lower() == "tak":
      while True:
        animowany_dialog("Podaj swoje imię: ")
        imie = input("> ")
        if imie.strip(): #jezeli zmienna imie nie jest pusta, program przechodzi dalej
          animowany_dialog("Weryfikacja przebiegła pomyślnie! Generowanie terenu....")
          time.sleep(5)
          print("--------------------------------Naciśnij enter aby kontynuować--------------------------------")
          input()
          break
        else:
            animowany_dialog("Imię nie może być puste!")
      break
  elif wybor_poczatkowy.lower() == "nie":
    animowany_dialog("Odmowa!, program zakończony")
    print("<--------------------------------GAME OVER-------------------------------->")
    exit() #program sie zamyka jeżeli użytkownik nie przeszedł weryfikacji
  else:
     animowany_dialog("Wykonaj polecenie!")

#komunikaty powitalne
animowany_dialog(f"Witaj, \033[1m{imie}\033[0m!")
animowany_dialog("Rozpoczynamy kolejny dzień jako student uczelni, na którą zaaplikowałeś ze względu na to, że albo jest blisko morza, albo masz blisko do domu, albo po prostu jest wysoko w rankingu ")
animowany_dialog("Nieistotne, w każdym razie dzień dobry studencie Politechniki Gdańskiej!")
animowany_dialog("Mamy 17 stycznia rok 2025, przypominam bo jeszcze nie przywykłeś, że 2024 minął bezpowrotnie!\nBudzik wskazuje godzinę 8:10. Zajęcia zaczynają się o 9:00, a do uczelni masz 15 minut na pieszo.\n")

while True:
  animowany_dialog("Czy uważasz, że to pora wstać? Odpowiedz TAK lub NIE: ")
  poranna_decyzja1 = input("> ")
  if poranna_decyzja1.lower() == "tak":
    animowany_dialog("Brawo! To twój pierwszy raz kiedy wstałeś na czas!")
    break
  elif poranna_decyzja1.lower() == "nie":
    komunikaty1 = ["Moje gratulacje! zaspałeś! Jest 8:50!",
                  "Jest 8:30 teraz nie masz wyboru, twoja sumienność nakazuje ci wstać!"]
    wagi1 = [0.7,0.3]
    zdarzenie1 = random.choices(komunikaty1, wagi1 , k=1)[0] #dzieki modułowi random program losuje jeden element z listy uwzgledniajac wagi czy szanse na wylosowanie danej wiadomosci
    animowany_dialog(zdarzenie1)
    break
  else:
    animowany_dialog("Proszę udzielić odpowiedzi na pytanie!")
    
if poranna_decyzja1.lower()== 'nie' and zdarzenie1 == komunikaty1[0]:
  time.sleep(2)
  animowany_dialog("Hehe, nie jest za ciekawie, ale przecież to tylko wykład i to jeszcze z mechaniki, obecność nieobowiązkowa ;)")
  while True:
    animowany_dialog("Śpisz dalej? Odpowiedz TAK lub NIE: ")
    poranna_decyzja2 = input("> ")
    if poranna_decyzja2.lower() == "nie":
      animowany_dialog("*Spóźniony student wstał i od razu pobiegł na zajęcia*\n")
      break
    elif poranna_decyzja2.lower() == "tak":
      animowany_dialog("Budzik dzwoni!")
      while True:
        animowany_dialog("Czy chcesz sprawdzić która jest godzina? Odpowiedz TAK lub NIE")
        poranna_decyzja3 = input("> ")
        if poranna_decyzja3.lower() == "nie":
          animowany_dialog("Halo! Pobudka!")
          time.sleep(2)
          animowany_dialog("Znowu przespałeś cały dzień, na szczęście nic ważnego cię nie ominęło oprócz Technologi Informacyjnych.\nAle nie martw się, jutro też jest dzień!")
          print("<--------------------------------GAME OVER-------------------------------->")
          exit() #program sie zamyka jeżeli użytkownik dokonal niewłaściwego wyboru
        elif poranna_decyzja3.lower() == "tak":
          animowany_dialog("Jest godzina 10:30! Wykład właśnie dobiegł końca, ale za to pewnie się wyspałeś co nie?\nWarto jednak było nieprzychodzić. Przed tobą matematyka za 15 minut!")
          animowany_dialog("*student wstaje i szykuje się do wyjścia na uczelnie*")
          break
        else:
          animowany_dialog("Błąd! Odpowiedz na pytanie")
      break
    else:
      animowany_dialog("Nie rozumiem... Odpowiedz na pytanie!")
elif poranna_decyzja1.lower()== 'nie' and zdarzenie1 == komunikaty1[1]:
  animowany_dialog("*Student wstaje i wychodzi spóźniony na uczelnię*")
elif poranna_decyzja1.lower()== 'tak':
  animowany_dialog("*Student pełen optymizmu i dobrego humoru wstaje i udaje się na uczelnię*")
print("\n")
time.sleep(2)

animowany_dialog("Nic nie zjadłeś przed wyjściem z domu, musisz być głodny!")
while True:
  animowany_dialog("Chcesz wejść do lidla po drodze? Odpowiedz TAK lub NIE: ")
  wyjsciowa_decyzja1 = input("> ")
  if wyjsciowa_decyzja1.lower() == "tak":
    komunikaty2 = ["Standardowo przy wejściu do lidla ktoś stoi i zbiera na coś pieniądze, ale tym razem jest ich dwóch! \nPo jednej stronie drzwi bezdomny przekonuje ludzi, że zbiera na chleb a po drugiej stronie chłopiec z jakiejś organizacji charytatywnej zbiera na chore dziecko.\nChcąc ominąć niewygodną interakcje, rezygnujesz z zakupów i idziesz na uczelnię",
                  "W lidlu kupiłeś jedyną sensowną opcję aby się najeść i zapłaciłeś za to całe 7zł! \nNiesmak pozostaje, w końcu miałbyś za to conajmniej 3 trunki procentowe dolnych lotów, albo dołożyłbyś 4 razy tyle i miał kebaba!"]
    zdarzenie2 = random.choice(komunikaty2) #dzieli modulowi random program lostuje jedną z dwóch opcji z listy, obie opcje mają takie samo prawdopodobieństwo na wylosowanie
    animowany_dialog(zdarzenie2)
    break
  elif wyjsciowa_decyzja1.lower() == "nie":
    animowany_dialog("*Student zmierza prosto na uczelnię*")
    break
  else:
    animowany_dialog("Odpowiedz na pytanie!")
time.sleep(2)

print("\n")
animowany_dialog("Oho!")
time.sleep(1)
animowany_dialog("Ludzie na grupie piszą, że na enauczaniu zostały opublikowane wyniki kolokwium z matematyki.")

while True:
  animowany_dialog("Czy chcesz zobaczyć swój wynik? Odpowiedz TAK lub NIE: ")
  wyjsciowa_decyzja2 = input("> ")
  if wyjsciowa_decyzja2.lower() == "nie":
    animowany_dialog("Może i lepiej! Nie ma co ryzykować zepsuciem sobie piątku!")
    animowany_dialog("*Niczego nieświadomy student wchodzi na uczelnię*")
    break
  elif wyjsciowa_decyzja2.lower() == "tak":
    wynik_kolokwium = random.randint(0,20) #program dzieki modulowi random generuje losowa liczbe z zakresu od 0 do 20
    if wynik_kolokwium < 10:
      animowany_dialog(f"Gratulacje! Ilość uzyskanych punktów: {wynik_kolokwium}. To oznacza, że nie zdałeś matematyki.\nMoże zamiast ciągle wychodzić na miasto ze znajomymi i grać w gry do późna trzeba było przysiąść nad ksiązkami.")
      animowany_dialog("*Załamany student wchodzi na uczelnię*")
      time.sleep(2)
    else:
      animowany_dialog(f"Brawo! Liczba uzyskanych punktów to: {wynik_kolokwium}, co oznacza, że udało ci się przebrnąc przez matematykę w I semestrze!")
      animowany_dialog("*Szczęsliwy student wchodzi na uczelnię*")
      time.sleep(2)
    break
  else:
    animowany_dialog("Błąd! Podaj poprawną odpowiedź!")
animowany_dialog("\nNa zajęciach, znajomi ku twojemu niezadowoleniu poinformowali cię, że we wtorek jest kolowkium z elektrotechniki.\nTrochę cię przybiła ta wiadomość, prawda?")
animowany_dialog("\nŻeby tego było mało, pomimo że starałeś sie słuchać na wykładzie, chwilowo odpłynąłeś i zacząłeś przeglądać telefon.\nProwadzący to zauważył i chcąc przywrócić twoją koncenstrację zapytał cię o to co trzeba zrobić dalej w zadaniu.")
animowany_dialog("Niestety nie masz absolutnie pojęcia co się dzieje, ponieważ zbyt długo nie sluchałeś.\nCałe szczęscie prowadzący ułatwił ci zadanie i zapytał wprost czy trzeba wykonać czynność A czy B.\n")

while True:
    animowany_dialog("Wybierz opcję A lub B: ")
    wybor_wykladowy1 = input("> ")
    if wybor_wykladowy1.lower() == "a":
      animowany_dialog("Udało ci się! Wykładowca odpuścił a ty wybrnąłeś z niewygodniej sytuacji.\nNieźle cię to zestrestowało i dalej już na pewno będziesz uważny.\n*Student odetchnał z ulgą i zaczął słuchać na wykładzie\n*")
      break
    elif wybor_wykladowy1.lower() == "b":
      animowany_dialog("Niestety, nie udało ci się! Załamany wykładowca pokiwał głową i dał ci spokój.\nInni studenci, czyli równe 130 osób, cię wyśmiali bo pytanie było trywialne. \nTo tylko dodatkowo cię zdołowało.\n*Wciąż jeszcze zestresowany studnent skupia się na wykładzie*\n")
      break
    else:
      animowany_dialog("Wykładowca się niecierpliwi! Odpowiedz na pytanie!")
time.sleep(2)
animowany_dialog("Brawo! Przeżyłeś wykład! To nie takie straszne prawda?\nMoże i było trochę nudno, trochę ekscytująco... w każdym razie następne zajęcia przed tobą.\nDelikatnie mówiąc nie masz ochoty dalej siedzieć na zajęciach.")
time.sleep(2)
animowany_dialog("A może by tak... ")
time.sleep(3)
print("<--------------------------------Naciśnij enter aby kontynuować-------------------------------->")
input()
animowany_dialog("Pora podjąć niezwykle istotną decyzję jako student!")

while True:
  animowany_dialog("Czy chcesz iść na następne zajęcia? Odpowiedz TAK lub NIE: ")
  studencki_wybor1 = input("> ")
  if studencki_wybor1.lower() == "tak":
    while True:
      animowany_dialog("Czy jesteś tego pewien? Odpowiedz TAK lub NIE: ")
      studencki_wybor2 = input("> ")
      if studencki_wybor1.lower() == "tak" and studencki_wybor2.lower() == "nie":
        animowany_dialog("*Student rezygnuje z udziału w wykładach i wraca do pokoju w akademiku*\n")
        time.sleep(2)
        szansa_na_wiadomosc = random.randint(1,100) #dzieki modułowi random program losuje liczbę z zakresu od 1 do 100
        if szansa_na_wiadomosc <= 50:
          animowany_dialog("To nie był dobry wybór! Wykładowca pierwszy raz od początku roku sprawdził obecność akurat wtedy kiedy zdecydowałeś się nie iść!\nPonadto każdy nieobecny dzisiaj dostał karne obowiązkowe do przesłania zadanie domowe!\nSzczęście dzisiaj nie jest po twojej stronie!")
           time.sleep(2) 
          break
        else:
          continue #jezeli funkcja random.randint() wylosuje liczbe wieksza niz 50, program przechodzi dalej
          break
      elif studencki_wybor1.lower() =="tak" and studencki_wybor2.lower() == "tak":
          animowany_dialog("Mądra decyzja! Warto zostać i posłuchać co wykładowca ma do powiedzenia!")
          animowany_dialog("*Niepewny swojego wyboru student udał się na wykład*")
          time.sleep(2)
          animowany_dialog("Zajęcia minęły wyjątkowo szybko.\nO dziwo nawet zapamiętałeś parę istotnych rzeczy.\nCzyli jednak było warto przyjść posłuchać!\n")
          break
      else:
        animowany_dialog("Potraktuj to poważnie! Odpowiedz na pytanie!")
    break
  elif studencki_wybor1.lower() == "nie":
    animowany_dialog("*Student rezygnuje z udziału w wykładach i wraca do pokoju w akademiku*\n")
    time.sleep(2)
    break
  else:
    animowany_dialog("To nie jest moment na żarty! Czas ucieka! Proszę podjąć decyzję")

animowany_dialog("Przydałoby się zrobić jakieś zakupy. W końcu słoiki od mamy już się skończyły!\n")
while True:
  animowany_dialog("Czy chcesz wejść do lidla zrobić zakupy? Wybierz TAK lub NIE: ")
  wybor_posiłku1 = input("> ")
  if wybor_posiłku1.lower() == "tak":
    animowany_dialog("Świetnie! Dobra dieta to fundament prawidłowego funkcjonowania organizmu człowieka!")
    time.sleep(2)
    print("<--------------------------------Naciśnij enter aby wylosować co ugotować do jedzenia-------------------------------->")
    input()
    wybory_jedzenia = ["Kurczak z ryżem i grilowanymi ważywami",
                       "Spaghetti bolognese",
                       "Serowe rizotto",
                       "Parówki z ketchupem"]
    animowany_dialog(f"Dzisiaj padło na: {random.choice(wybory_jedzenia)}. Niezły wybór! Zapowiada się wyborna wieczerza!\n*Student udaje się do pokoju*\n") #dzieki modulowi random program wybiera i drukuje losowy element z listy
    break
  elif wybor_posiłku1.lower() == "nie":
    animowany_dialog("No cóz, może innym razem zjesz zdrowo.\nDzisiaj do jedzenia dla odmiany tosty - piąty dzień pod rząd!\n*Student udaje się do pokoju*\n")
    break
  else:
    animowany_dialog("Człowiek głodny, człowiekiem niebezpiecznym! Podejmij dezycję!")

time.sleep(2)
if wybor_posiłku1.lower() == "tak":
  animowany_dialog("Po walce w kuchni z garnkami nareszcie udało ci się przyżądzić jedzenie!\nPachnie zaskakująco dobrze! To chyba znak, że jest zjadliwe.")
  animowany_dialog("*Student rozpoczyna ucztę*\n")
else:
    animowany_dialog("Cóż tosty z pasztetem i parówkami 2zł za 3kg nie są wcale takie złe!\n*Student z lekkimi łzami w oczach bierze się za pyszny i odżywczy posiłek*\n")
time.sleep(2)

animowany_dialog("Najedzony człowiek to szczęsliwy człowiek! A przynajmniej tak sie mówi.")
time.sleep(2)
animowany_dialog("Chociaż czy można być szczęśliwym ze świadomością, że we wtorek czeka cię kolokwium z elektrotechniki?")
animowany_dialog("Jest godzina 18:00, chyba wypadałoby się trochę pouczyć. W końcu czasu za dużo nie masz! Ale jednocześnie po jedzeniu zrobiłeś się troche senny...\n")
animowany_dialog("Wybierz co zamierzasz zrobić! To nie może być pochopna decyzja:\nA) Położyć się spać\nB) Zabrać się za naukę\nC) Pograć w gry ze znajomymi\n")

while True:
  animowany_dialog("Wybierz opcję A, B lub C: ")
  wybor_wieczorny = input("> ")
  if wybor_wieczorny.lower() == "a":
    animowany_dialog("Hmm... ")
    time.sleep(2)
    animowany_dialog("Dobry wybór! Sen jest niesamowicie ważny w życiu studenta! Mózg musi cały czas pracować na najwyższych obrotach, aby nadążyć z nauką ;)\nPytanie czy nie bedziesz żałował tej decyzji we wtorek...")
    animowany_dialog("*Student kładzie się do łóżka i niemal natychmiast zasypia*\n")
    break
  elif wybor_wieczorny.lower() == "b":
    animowany_dialog("Możesz być z siebie dumny!\nGwarantuje ci, że nie pożałujesz tej decyzji, a efekty twojej pracy zaowocują dobrym wynikiem z egzaminu!\nPod warunkiem, że się przyłożysz do tej nauki...")
    animowany_dialog("*Student, mimo lekkiego zmęczenia robi sobie kawę i bierze się do pracy*\n")
    break
  elif wybor_wieczorny.lower() == "c":
    animowany_dialog("Hmm...")
    time.sleep(2)
    animowany_dialog("Świetny wybór!\nPrzecież w życiu nie chodzi o to, żeby ciągle się uczyć!\nTrochę rozrywki też jest potrzebne, aby sobie trochę urozmaicić czas!\nSwoją drogą, ciekawe czy granie z kolegami pomoże ci na kolokwium z elektrotechniki we wtorek.\nBaw się dobrze ;)")
    animowany_dialog("*Student odpala laptopa i dzwoni do znajomych z uczelni*\n")
    break
  else:
    animowany_dialog("Co prawda mamy mnóstwo czasu, ale podejmij decyzję!")
time.sleep(2)

animowany_dialog("Dzień dobiegł końca, wykorzystałeś go najlepiej jak umiałeś!\nTo czy podjąłeś słuszne decyzje zostawiam do oceny tobie użytkowniku!")
animowany_dialog(f"Jutro czeka cię kolejny dzień pełen trudnych wyborów i niezliczonych prób \033[1m{imie}\033[0m!\nNajważniejsze to nie dać się zwieść na złą drogę i znaleźć w życiu umiar :)\n")
time.sleep(2)
animowany_dialog("Student kończy dzisiejszy dzień, nie zdając sobie sprawy, że glos w jego głowie kierujący jego wyborami...")
time.sleep(3)
animowany_dialog("Nie należy do niego...\n")
time.sleep(2)
print("<--------------------------------GAME COMPLETED-------------------------------->")
time.sleep(2)
animowany_dialog("Zamykanie symulacji...")
time.sleep(2)
exit() #Program się zamyka po zakończeniu rozgrywki

      
      

