from django.shortcuts import render
import random

# Create your views here.
def name(request):
    return render(request, 'name.html')

def result(request):
    name = request.POST['name']
    season = request.POST['season']
    month = request.POST['month']

    
    Jan=('Ganet', 'Love', 'Truth', 'chastity', 'eternal', 'lovely', '1', 'jan', '11', 'first')
    Feb=('chastity', 'peace', '2', 'feb','22','222', 'second')
    Mar=('Aquamarine', 'Calm', 'intelligent', 'brave', 'sincere', 'virtuous', '3', 'mar','fresh')
    Apr=('Diamond', 'Love', 'Happiness', 'Compassion', 'apr', '4','44', 'mid')
    May=('Emerald', 'Happiness', 'Luck', 'Patience', 'Integrity', '5', 'may', 'child', 'family')
    Jun=('Pearl', 'Health', 'Success', 'Prosperit', '6', 'jun', 'final')
    Jul=('Ruby', 'Passion', 'Life', 'jul', '7', '77' '777', 'lucky')
    Aug=('Peridot', 'Wisdom', 'Happiness', 'aug', '8','88','888', 'summer')
    Sep=('sapphire', 'benevolence', 'sincerity', 'virtue', '9','99','999', 'sep')
    Oct=('Opal', 'Love', 'Truth', 'chastity', '10', 'oct','1010', 'mid', 'korean')
    Nov=('Topaz', 'Friendship', 'patience', 'innocence', 'nov', '11','1111', 'enter')
    Dec=('Turqoise', 'Luck', 'Success', 'Prosperity', '12', 'dec','1212', 'end', 'goodbye')
    months=[Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
    bbb = months[int(month)-1]
    mymonth1 = random.choice(bbb)
    mymonth2 = random.choice(bbb)
    mymonth3 = random.choice(bbb)

    Spring = ('flowers', 'blossoms', 'shoots', 'mask', 'dust', 'festival', 'new','spring', 'mar', '345')  
    Summer = ('sea', 'sunflowers', 'swim', 'hot', 'Rain', 'rainy', 'lightning', 'valley', 'watermelon', 'blue', 'sky', 'vacation', 'surfing')
    Fall = ('Book', 'maple', 'maple', 'leaves', 'brown', 'khaki', 'calm', 'lonely', 'quiet', 'supersolo') 
    Winter = ('snow', 'Ulaf', 'camellia', 'xmas', 'snowman', 'ice', 'Gloves', 'boots', 'white', 'snowboard', 'wind', 'cold')
    seasons = [Spring, Summer, Fall, Winter]
    ccc = seasons[int(season)-1]
    myseason1 = random.choice(ccc)
    myseason2 = random.choice(ccc)
    myseason3 = random.choice(ccc)


    nic1 = mymonth1+'_'+myseason1
    nic2 = mymonth2+'_'+myseason2
    nic3 = mymonth3+'_'+myseason3


    return render(request, 'result.html', {'name':name, 'nic1':nic1, 'nic2':nic2, 'nic3':nic3})