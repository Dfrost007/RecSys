from math import sqrt


critics={'Lisa Rose': {
        'Lady in the water' : 2.5, 
        'Snakes on the Plane' : 3.5, 
        'Just my Luck' : 3.0, 
        'Superman Returns' : 3.5, 
        'You me Dupree' : 2.5, 
        'The Night Listener': 3.0 },
    'Gene Seymour' :   {
        'Lady in the water' : 3.0, 
        'Snakes on the Plane' : 3.5, 
        'Just my Luck' : 1.5, 
        'Superman Returns' : 5.0, 
        'You me Dupree' : 3.5, 
        'The Night Listener': 3.0 },
    'Michael Philips' : {
        'Lady in the water' : 2.5, 
        'Snakes on the Plane' : 3.0, 
        'Superman Returns' : 3.5, 
        'The Night Listener': 4.0 },
    'Claudia Puig' :  {
        'Snakes on the Plane' : 3.5, 
        'Just my Luck' : 3.0, 
        'Superman Returns' : 4.0, 
        'You me Dupree' : 2.5, 
        'The Night Listener': 4.5 },
    'Mick LaSalle' : {
        'Lady in the water' : 3.0, 
        'Snakes on the Plane' : 4.0, 
        'Just my Luck' : 2.0, 
        'Superman Returns' : 3.0, 
        'You me Dupree' : 2.0, 
        'The Night Listener': 3.0 },
    'Jack Matthews' : {
        'Lady in the water' : 3.0, 
        'Snakes on the Plane' : 4.0, 
        'Superman Returns' : 5.0, 
        'You me Dupree' : 3.5, 
        'The Night Listener': 3.0 },
    'Toby' : {      
        'Snakes on the Plane' : 4.5, 
        'Superman Returns' : 4.0, 
        'You me Dupree' : 1.0},
 }

def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:return 0

    Sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sqrt(Sum_of_squares))

def sim_pearson(pref,p1,p2):
    si={}
    for item in pref[p1]:
        if item in pref[p2]:
            si[item]=1
    n=len(si)
    if n==0:return 0
    sum1=sum([pref[p1][item] for item in si])
    sum2=sum([pref[p2][item] for item in si])
    sum1sq=sum([pow(pref[p1][item],2) for item in si])
    sum2sq=sum([pow(pref[p2][item],2) for item in si])
    psum=sum([pref[p1][item]*pref[p2][item] for item in si])
    num=n*psum-(sum1*sum2)
    den=sqrt(n*sum1sq-pow(sum1,2))*sqrt(n*sum2sq-pow(sum2,2))
    r=num/den

    return r

def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
        for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


 
