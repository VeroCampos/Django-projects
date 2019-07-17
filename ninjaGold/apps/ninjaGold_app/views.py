from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    #keep player's rec in session
    if not "totalGold" in request.session:
        request.session['totalGold'] = 0
        request.session['gold_list']= []
   
    return render(request, 'ninjaGold/index.html')


def processGold(request):
    totalGold = random.randint(1, 100)
    
    totalGold = 0
   
    if request.POST['building'] == 'farm':
        currentFarm = random.randint(10, 21)
        print(f"farm {currentFarm}")
        totalGold += currentFarm
        gold=f"<p class='gold'>You are in the farm, gain {currentFarm} gold</p>"
        request.session['gold_list'].append(gold)
        
    if request.POST['building'] == 'cave':
        currentCave = random.randint(5, 10)
        print(f"cave {currentCave}")
        totalGold += currentCave
        gold=f"<p class='gold'>You are inside of the cave, gain {currentCave} gold</p>"
        request.session['gold_list'].append(gold) 
        

    if request.POST['building'] == 'house':
        currentHouse = random.randint(1, 5)
        print(f"house {currentHouse}")
        totalGold += currentHouse
        gold=f"<p class='gold'>You are in house {currentHouse}</p>"
        request.session['gold_list'].append(gold)

    if request.POST['building'] == 'casino':
        currentCasino = random.randint(1, 50)
        print(currentCasino)
        if currentCasino < 25:
            currentCasino = currentCasino + totalGold
            gold=f"<p class='gold'>You have enter the casino, gain {currentCasino} gold</p>"
            request.session['gold_list'].append(gold)
        elif currentCasino >=30:
            currentCasino = currentCasino - 50
            loss=f"<p class ='red'>You have enter the casino, loss {currentCasino} gold</p>"
            request.session['gold_list'].append(loss)
        print(f"casino {currentCasino}") 
        totalGold += currentCasino
 
    request.session['totalGold'] += totalGold
    
    return redirect('/')

     
def reset(request):
    #Removes all keys in section
    request.session.clear()

    return redirect('/')