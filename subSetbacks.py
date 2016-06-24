#! python3

##Part I: Builds database of subdivision setbacks
##Part II: Uses subdivision database to check setback requirements on new home building plans

import pprint,shelve

subsShelf=shelve.open('subs', writeback=True)


zones={
    'A':{'frontLiving':60,'frontGarage':60,'rear':30,'side':0,'side1':30,'side2':35,'streetSide':45,'lotCov':.1,'acc':'no','maxHeight':60,'minLot':20,'notes':'none'},
    'A-R':{'frontLiving':60,'frontGarage':60,'rear':30,'side':0,'side1':30,'side2':35,'streetSide':45,'lotCov':.1,'acc':'no','maxHeight':35,'minLot':4.7,'notes':'none'},
    'R-E':{'frontLiving':50,'frontGarage':50,'rear':30,'side':0,'side1':20,'side2':25,'streetSide':35,'lotCov':.15,'acc':'no','maxHeight':35,'minLot':1.8,'notes':'none'},
    'R-1':{'frontLiving':30,'frontGarage':30,'rear':30,'side':0,'side1':15,'side2':20,'streetSide':30,'lotCov':.35,'acc':'no','maxHeight':35,'minLot': 37000/43560,'notes':'none'},
    'R-2':{'frontLiving':30,'frontGarage':30,'rear':30,'side':0,'side1':10,'side2':15,'streetSide':20,'lotCov':.4,'acc':'no','maxHeight':35,'minLot': 17000/43560,'notes':'none'},
    'R-3':{'frontLiving':30,'frontGarage':30,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.4,'acc':'no','maxHeight':35,'minLot': 10000/43560,'notes':'none'},
    'R-4':{'frontLiving':20,'frontGarage':20,'rear':20,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.4,'acc':'no','maxHeight':35,'minLot': 8000/43560,'notes':'none'},
    'R-5':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.4,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-6':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-7':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-8':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-9':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-10':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-11':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-12':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-13':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-14':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-15':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-16':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-17':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-18':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-19':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-20':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-21':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-22':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-23':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-24':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'R-25':{'frontLiving':20,'frontGarage':20,'rear':25,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 7000/43560,'notes':'none'},
    'L-O':{'frontLiving':20,'frontGarage':20,'rear':20,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.6,'acc':'no','maxHeight':35,'minLot': 2000/43560,'notes':'none'},
    'C-1':{'frontLiving':15,'frontGarage':15,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':10,'lotCov':.5,'acc':'no','maxHeight':35,'minLot': 2000/43560,'notes':'none'},
    'C-2':{'frontLiving':0,'frontGarage':0,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':0,'lotCov':.92,'acc':'no','maxHeight':35,'minLot': 1300/43560,'notes':'none'},
    'C-3':{'frontLiving':0,'frontGarage':0,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':0,'lotCov':.92,'acc':'no','maxHeight':35,'minLot': 1300/43560,'notes':'none'},
    'CBD':{'frontLiving':0,'frontGarage':0,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':0,'lotCov':.92,'acc':'no','maxHeight':35,'minLot': 500/43560,'notes':'none'},
    'M-1':{'frontLiving':0,'frontGarage':0,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':0,'lotCov':.92,'acc':'no','maxHeight':35,'minLot': 0,'notes':'none'},
    'BP':{'frontLiving':20,'frontGarage':20,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':20,'lotCov':.5,'acc':'no','maxHeight':35,'minLot': 0,'notes':'none'},
    'M-2':{'frontLiving':0,'frontGarage':0,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':0,'lotCov':.92,'acc':'no','maxHeight':35,'minLot': 0,'notes':'none'},
    'M-3':{'frontLiving':0,'frontGarage':0,'rear':0,'side':0,'side1':0,'side2':0,'streetSide':0,'lotCov':.92,'acc':'no','maxHeight':35,'minLot': 0,'notes':'none'},
    'MU':{'frontLiving':20,'frontGarage':20,'rear':20,'side':0,'side1':7.5,'side2':12.5,'streetSide':20,'lotCov':.5,'acc':'no','maxHeight':35,'minLot': 5000/43560,'notes':'none'}}

while True:
    print('Enter Subdivision Name (ENTER to continue to plan review).\n For a list of subdivisions in the database, type \'list subs\'.')
    nameOfSub=input()
    nameOfSub=nameOfSub.lower()
    if nameOfSub=='list subs':
        for k in subsShelf.keys():
            pprint.pprint(k)
        print('\n')
    elif nameOfSub=='' or nameOfSub=='list subs':
        break
    subsShelf['name']=nameOfSub
    if nameOfSub in subsShelf:
        pprint.pprint(subsShelf[nameOfSub])
        print('Would you like to edit this?')
        edit=input()
        if edit=='yes':
##            print('Enter zone')
##            zone=input()
##            subsShelf[nameOfSub]=zones[zone]
            print('Is the front living setback ' +str(subsShelf[nameOfSub]['frontLiving'])+ ' feet? (type yes or no)')
            frontLivingQuestion=input()
            if frontLivingQuestion=='no':
                print('What is the front living setback?')
                subsShelf[nameOfSub]['frontLiving']=float(input())
                print('Is the front garage setback ' +str(subsShelf[nameOfSub]['frontGarage'])+ ' feet? (type yes or no)')
            else:
                print('Is the front garage setback ' +str(subsShelf[nameOfSub]['frontGarage'])+ ' feet? (type yes or no)')
            frontGarageQuestion=input()
            if frontGarageQuestion=='no':
                print('What is the front garage setback?')
                subsShelf[nameOfSub]['frontGarage']=float(input())
                print('Is the rear setback ' +str(subsShelf[nameOfSub]['rear'])+ ' feet? (type yes or no)')
            else:
                print('Is the rear setback ' +str(subsShelf[nameOfSub]['rear'])+ ' feet? (type yes or no)')
            rearQuestion=input()
            if rearQuestion=='no':
                print('What is the rear setback?')
                subsShelf[nameOfSub]['rear']=float(input())
                print('Is the single story side setback ' + str(subsShelf[nameOfSub]['side1'])+ ' feet? (type yes or no)')
            else:
                print('Is the single story side setback ' + str(subsShelf[nameOfSub]['side1'])+ ' feet? (type yes or no)')
            side1Question=input()
            if side1Question=='no':
                print('What is the single story side setback?')
                subsShelf[nameOfSub]['side1']=float(input())
                print('Is the multi-story side setback ' + str(subsShelf[nameOfSub]['side2']) + ' feet? (type yes or no)')
            else:
                print('Is the multi-story side setback ' + str(subsShelf[nameOfSub]['side2']) + ' feet? (type yes or no)')
            side2Question=input()
            if side2Question=='no':
                print('What is the multi-story side setback?')
                subsShelf[nameOfSub]['side2']=float(input())
                print('Is the street side setback ' + str(subsShelf[nameOfSub]['streetSide']) + ' feet? (type yes or no)')
            else:
                print('Is the street side setback ' + str(subsShelf[nameOfSub]['streetSide']) + ' feet? (type yes or no)')
            streetSideQuestion=input()
            if streetSideQuestion=='no':
                print('What is the street side setback?')
                subsShelf[nameOfSub]['streetSide']=input()
                print('Is the maximum lot coverage ' +str(subsShelf[nameOfSub]['lotCov']*100)+ '%? (type yes or no)')
            else:
                print('Is the maximum lot coverage ' +str(subsShelf[nameOfSub]['lotCov']*100)+ '%? (type yes or no)')
            lotCovQuestion=input()
            if lotCovQuestion=='no':
                print('What is the maximum lot coverage (in percent)?')
                subsShelf[nameOfSub]['lotCov']=float(input())/100
                print('Is an ACC Letter Required?')
            else:
                print('Is an ACC Letter Required?')
                subsShelf[nameOfSub]['acc']=input()
                print('Is the minimum lot size ' +str(int((subsShelf[nameOfSub]['minLot']*43560)))+ ' square feet? (type yes or no)')
            minLotQuestion=input()
            if minLotQuestion=='no':
                print('What is the minimum lot size in square feet?')
                subsShelf[nameOfSub]['minLot']=float(input())/43560
            print('Is the maximum height ' +str(subsShelf[nameOfSub]['maxHeight'])+ ' feet? (type yes or no)')
            maxHeightQuestion=input()
            if maxHeightQuestion=='no':
                print('What is the maximum height?')
                subsShelf[nameOfSub]['maxHeight']=input()
                print('Please type any additional notes')
            else:
                print('Please type any additional notes')
            subsShelf[nameOfSub]['notes']=input()
            subsShelf[nameOfSub]=subsShelf[nameOfSub]
    elif nameOfSub!='list subs':
        print('I don\'t know about that subdivision. Please tell me about it. \n')
        print('Enter zone')
        zone=input()
        zone=zone.upper()
        subsShelf[nameOfSub]=zones[zone]
        print('Is the front living setback ' +str(zones[zone]['frontLiving'])+ ' feet? (type yes or no)')
        frontLivingQuestion=input()
        if frontLivingQuestion=='no':
            print('What is the front living setback?')
            subsShelf[nameOfSub]['frontLiving']=float(input())
            print('Is the front garage setback ' +str(zones[zone]['frontGarage'])+ ' feet? (type yes or no)')
        else:
            print('Is the front garage setback ' +str(zones[zone]['frontGarage'])+ ' feet? (type yes or no)')
        frontGarageQuestion=input()
        if frontGarageQuestion=='no':
            print('What is the front garage setback?')
            subsShelf[nameOfSub]['frontGarage']=float(input())
            print('Is the rear setback ' +str(zones[zone]['rear'])+ ' feet? (type yes or no)')
        else:
            print('Is the rear setback ' +str(zones[zone]['rear'])+ ' feet? (type yes or no)')
        rearQuestion=input()
        if rearQuestion=='no':
            print('What is the rear setback?')
            subsShelf[nameOfSub]['rear']=float(input())
            print('Is the single story side setback ' + str(zones[zone]['side1'])+ ' feet? (type yes or no)')
        else:
            print('Is the single story side setback ' + str(zones[zone]['side1'])+ ' feet? (type yes or no)')
        side1Question=input()
        if side1Question=='no':
            print('What is the single story side setback?')
            subsShelf[nameOfSub]['side1']=float(input())
            print('Is the multi-story side setback ' + str(zones[zone]['side2']) + ' feet? (type yes or no)')
        else:
            print('Is the multi-story side setback ' + str(zones[zone]['side2']) + ' feet? (type yes or no)')
        side2Question=input()
        if side2Question=='no':
            print('What is the multi-story side setback?')
            subsShelf[nameOfSub]['side2']=float(input())
            print('Is the street side setback ' + str(zones[zone]['streetSide']) + ' feet? (type yes or no)')
        else:
            print('Is the street side setback ' + str(zones[zone]['streetSide']) + ' feet? (type yes or no)')
        streetSideQuestion=input()
        if streetSideQuestion=='no':
            print('What is the street side setback?')
            subsShelf[nameOfSub]['streetSide']=input()
            print('Is the maximum lot coverage ' +str(zones[zone]['lotCov']*100)+ '%? (type yes or no)')
        else:
            print('Is the maximum lot coverage ' +str(zones[zone]['lotCov']*100)+ '%? (type yes or no)')
        lotCovQuestion=input()
        if lotCovQuestion=='no':
            print('What is the maximum lot coverage (in percent)?')
            subsShelf[nameOfSub]['lotCov']=float(input())/100
            print('Is an ACC Letter Required?')
        else:
            print('Is an ACC Letter Required?')
        subsShelf[nameOfSub]['acc']=input()
        print('Is the maximum height ' +str(zones[zone]['maxHeight'])+ ' feet? (type yes or no)')
        maxHeightQuestion=input()
        if maxHeightQuestion=='no':
            print('What is the maximum height?')
            subsShelf[nameOfSub]['maxHeight']=input()
            print('Is the minimum lot size ' +str(int((zones[zone]['minLot']*43560)))+ ' square feet? (type yes or no)')
        else:
            print('Is the minimum lot size ' +str(int((zones[zone]['minLot']*43560)))+ ' square feet? (type yes or no)')
        minLotQuestion=input()
        if minLotQuestion=='no':
            print('What is the minimum lot size in square feet?')
            subsShelf[nameOfSub]['minLot']=float(input())/43560
            print('Please type any additional notes')
        else:
            print('Please type any additional notes')
        subsShelf[nameOfSub]['notes']=input()
        if nameOfSub!='':
            subsShelf['name']=subsShelf[nameOfSub]

if nameOfSub !='':
    subsShelf['name']=subsShelf[nameOfSub]

print('Let\'s review some plans. Enter Subdivision name, or ENTER to exit')
subOfInterest=input()
subOfInterest=subOfInterest.lower()
while subOfInterest !='':
    if subOfInterest in subsShelf:
        print('Enter distance to front living area')
        livingAreaOfInterest=float(input())
        print('Enter distance to garage')
        garageOfInterest=float(input())
        print('Which way does the garage face? Type \'front\' or \'side\'.')
        garageFace=input()
        print('Enter distance to rear')
        rearOfInterest=float(input())
        print('Enter distance to side')
        sideOfInterest=float(input())
        print('Enter distance to other side')
        sideOfInterest2=float(input())
        print('Enter number of stories')
        numberOfStories=int(input())
        print('Is this a corner lot? Type \'yes\' or \'no\'.')
        cornerLot=input()
        print('What is the acreage of the lot?')
        lotAcre=float(input())
        lotSize=lotAcre*43650
        print('What is the square footage of the first floor?')
        firstFloor=float(input())
        print('What is the square footage of the garage?')
        garageSize=float(input())
        print('Enter building height')
        buildingHeight=float(input())
        if garageFace=='side':
            subsShelf[subOfInterest]['frontGarage']=float(subsShelf[subOfInterest]['frontGarage'])-5
        else:
            subsShelf[subOfInterest]['frontGarage']=float(subsShelf[subOfInterest]['frontGarage'])
        if cornerLot=='yes':
            subsShelf[subOfInterest]['side']=subsShelf[subOfInterest]['streetSide']
    ##    else:
    ##        subsShelf[subOfInterest]['side']=subsShelf[subOfInterest]['side1']
        elif numberOfStories > 1:
            subsShelf[subOfInterest]['side']=subsShelf[subOfInterest]['side2']
        else:
            subsShelf[subOfInterest]['side']=subsShelf[subOfInterest]['side1']
        frontLivingCheck=livingAreaOfInterest-float(subsShelf[subOfInterest]['frontLiving'])
        frontGarageCheck=garageOfInterest-subsShelf[subOfInterest]['frontGarage']
        rearCheck=rearOfInterest-float(subsShelf[subOfInterest]['rear'])
        sideCheck=sideOfInterest-float(subsShelf[subOfInterest]['side1'])
        sideCheck2=sideOfInterest2-float(subsShelf[subOfInterest]['side'])
        enclosedRatio=(firstFloor+garageSize)/lotSize
        lotCheck=enclosedRatio-float(subsShelf[subOfInterest]['lotCov'])
        heightCheck=buildingHeight-float(subsShelf[subOfInterest]['maxHeight'])
        print('\nHere is how this plan stacks up:')
        if frontLivingCheck>=0:
            print('Living Area Setback:'.ljust(25)+ 'APPROVED'.ljust(20)+str(subsShelf[subOfInterest]['frontLiving'])+'\''.ljust(10)+str(livingAreaOfInterest)+'\''.ljust(10))
        else:
            print('Living Area Setback:'.ljust(25) + 'DENIED'.ljust(20)+str(subsShelf[subOfInterest]['frontLiving'])+'\''.ljust(10)+str(livingAreaOfInterest)+'\''.ljust(10))
        if frontGarageCheck>=0:
            print('Garage setback:'.ljust(25) + 'APPROVED'.ljust(20)+str(subsShelf[subOfInterest]['frontGarage'])+'\''.ljust(10)+str(garageOfInterest)+'\''.ljust(10))
        else:
            print('Garage setback:'.ljust(25)+'DENIED'.ljust(20)+str(subsShelf[subOfInterest]['frontGarage'])+'\''.ljust(10)+str(garageOfInterest)+'\''.ljust(10))
        if rearCheck>=0:
            print('Rear setback:'.ljust(25)+'APPROVED'.ljust(20)+str(subsShelf[subOfInterest]['rear'])+'\''.ljust(10)+str(rearOfInterest)+'\''.ljust(10))
        else:
            print('Rear setback:'.ljust(25)+'DENIED'.ljust(20)+str(subsShelf[subOfInterest]['rear'])+'\''.ljust(10)+str(rearOfInterest)+'\''.ljust(10))
        if sideCheck>=0:
            print('Side setback:'.ljust(25)+'APPROVED'.ljust(20)+str(subsShelf[subOfInterest]['side1'])+'\''.ljust(10)+str(sideOfInterest)+'\''.ljust(10))
        else:
            print('Side setback:'.ljust(25)+'DENIED'.ljust(20)+str(subsShelf[subOfInterest]['side'])+'\''.ljust(10)+str(sideOfInterest)+'\''.ljust(10))
        if sideCheck2>=0:
            print('Side setback:'.ljust(25)+'APPROVED'.ljust(20)+str(subsShelf[subOfInterest]['side'])+'\''.ljust(10)+str(sideOfInterest2)+'\''.ljust(10))
        else:
            print('Side setback:'.ljust(25)+'DENIED'.ljust(20)+str(subsShelf[subOfInterest]['side'])+'\''.ljust(10)+str(sideOfInterest2)+'\''.ljust(10))
        if buildingHeight<=35:
            print('Buiding Height:'.ljust(25)+'APPROVED'.ljust(20)+str(subsShelf[subOfInterest]['maxHeight'])+'\''.ljust(10)+str(buildingHeight)+'\''.ljust(10))
        else:
            print('Building Height:'.ljust(25)+'DENIED'.ljust(20)+str(subsShelf[subOfInterest]['maxHeight'])+'\''.ljust(10)+str(buildingHeight)+'\''.ljust(10))
        if lotCheck<=0:
            print('Lot Coverage:'.ljust(25)+'APPROVED'.ljust(20)+str(subsShelf[subOfInterest]['lotCov']*100)+'%'.ljust(10)+str(round(enclosedRatio*100,1))+'%'.ljust(10))
        else:
            print('Lot Coverage:'.ljust(25)+'DENIED'.ljust(20)+str(subsShelf[subOfInterest]['lotCov']*100)+'%'.ljust(10)+str(round(enclosedRatio*100,1))+'%'.ljust(10))
        print('Architectural Style:'.ljust(25)+str(subsShelf[subOfInterest]['acc']))
        print('NOTES'.center(65,'-'))
        print(str(subsShelf[subOfInterest]['notes']))
        if garageFace=='side':
            subsShelf[subOfInterest]['frontGarage']=float(subsShelf[subOfInterest]['frontGarage'])+5
        subOfInterest=''
    else:
        print('I don\'t know about that subdivision. Please tell me about it. \n')
        print('Enter zone')
        zone=input()
        zone=zone.upper()
        subsShelf[subOfInterest]=zones[zone]
        print('Is the front living setback ' +str(zones[zone]['frontLiving'])+ ' feet? (type yes or no)')
        frontLivingQuestion=input()
        if frontLivingQuestion=='no':
            print('What is the front living setback?')
            subsShelf[subOfInterest]['frontLiving']=float(input())
            print('Is the front garage setback ' +str(zones[zone]['frontGarage'])+ ' feet? (type yes or no)')
        else:
            print('Is the front garage setback ' +str(zones[zone]['frontGarage'])+ ' feet? (type yes or no)')
        frontGarageQuestion=input()
        if frontGarageQuestion=='no':
            print('What is the front garage setback?')
            subsShelf[subOfInterest]['frontGarage']=float(input())
            print('Is the rear setback ' +str(zones[zone]['rear'])+ ' feet? (type yes or no)')
        else:
            print('Is the rear setback ' +str(zones[zone]['rear'])+ ' feet? (type yes or no)')
        rearQuestion=input()
        if rearQuestion=='no':
            print('What is the rear setback?')
            subsShelf[subOfInterest]['rear']=float(input())
            print('Is the single story side setback ' + str(zones[zone]['side1'])+ ' feet? (type yes or no)')
        else:
            print('Is the single story side setback ' + str(zones[zone]['side1'])+ ' feet? (type yes or no)')
        side1Question=input()
        if side1Question=='no':
            print('What is the single story side setback?')
            subsShelf[subOfInterest]['side1']=float(input())
            print('Is the multi-story side setback ' + str(zones[zone]['side2']) + ' feet? (type yes or no)')
        else:
            print('Is the multi-story side setback ' + str(zones[zone]['side2']) + ' feet? (type yes or no)')
        side2Question=input()
        if side2Question=='no':
            print('What is the multi-story side setback?')
            subsShelf[subOfInterest]['side2']=float(input())
            print('Is the street side setback ' + str(zones[zone]['streetSide']) + ' feet? (type yes or no)')
        else:
            print('Is the street side setback ' + str(zones[zone]['streetSide']) + ' feet? (type yes or no)')
        streetSideQuestion=input()
        if streetSideQuestion=='no':
            print('What is the street side setback?')
            subsShelf[subOfInterest]['streetSide']=input()
            print('Is the maximum lot coverage ' +str(zones[zone]['lotCov']*100)+ '%? (type yes or no)')
        else:
            print('Is the maximum lot coverage ' +str(zones[zone]['lotCov']*100)+ '%? (type yes or no)')
        lotCovQuestion=input()
        if lotCovQuestion=='no':
            print('What is the maximum lot coverage (in percent)?')
            subsShelf[subOfInterest]['lotCov']=float(input())/100
            print('Is an ACC Letter Required?')
        else:
            print('Is an ACC Letter Required?')
        subsShelf[subOfInterest]['acc']=input()
        print('Is the maximum height ' +str(zones[zone]['maxHeight'])+ ' feet? (type yes or no)')
        maxHeightQuestion=input()
        if maxHeightQuestion=='no':
            print('What is the maximum height?')
            subsShelf[subOfInterest]['maxHeight']=input()
            print('Is the minimum lot size ' +str(int((zones[zone]['minLot']*43560)+1))+ ' square feet? (type yes or no)')
        else:
            print('Is the minimum lot size ' +str(int((zones[zone]['minLot']*43560))+1)+ ' square feet? (type yes or no)')
        minLotQuestion=input()
        if minLotQuestion=='no':
            print('What is the minimum lot size in square feet?')
            subsShelf[subOfInterest]['minLot']=float(input())/43560
            print('Please type any additional notes')
        else:
            print('Please type any additional notes')
        subsShelf[subOfInterest]['notes']=input()
        pprint.pprint(subsShelf[subOfInterest])
        print('Would you like to edit this?')
        edit=input()
        if edit=='yes':
##            print('Enter zone')
##            zone=input()
##            subsShelf[subOfInterest]=zones[zone]
            print('Is the front living setback ' +str(subsShelf[subOfInterest]['frontLiving'])+ ' feet? (type yes or no)')
            frontLivingQuestion=input()
            if frontLivingQuestion=='no':
                print('What is the front living setback?')
                subsShelf[subOfInterest]['frontLiving']=float(input())
                print('Is the front garage setback ' +str(subsShelf[subOfInterest]['frontGarage'])+ ' feet? (type yes or no)')
            else:
                print('Is the front garage setback ' +str(subsShelf[subOfInterest]['frontGarage'])+ ' feet? (type yes or no)')
            frontGarageQuestion=input()
            if frontGarageQuestion=='no':
                print('What is the front garage setback?')
                subsShelf[subOfInterest]['frontGarage']=float(input())
                print('Is the rear setback ' +str(subsShelf[subOfInterest]['rear'])+ ' feet? (type yes or no)')
            else:
                print('Is the rear setback ' +str(subsShelf[subOfInterest]['rear'])+ ' feet? (type yes or no)')
            rearQuestion=input()
            if rearQuestion=='no':
                print('What is the rear setback?')
                subsShelf[subOfInterest]['rear']=float(input())
                print('Is the single story side setback ' + str(subsShelf[subOfInterest]['side1'])+ ' feet? (type yes or no)')
            else:
                print('Is the single story side setback ' + str(subsShelf[subOfInterest]['side1'])+ ' feet? (type yes or no)')
            side1Question=input()
            if side1Question=='no':
                print('What is the single story side setback?')
                subsShelf[subOfInterest]['side1']=float(input())
                print('Is the multi-story side setback ' + str(subsShelf[subOfInterest]['side2']) + ' feet? (type yes or no)')
            else:
                print('Is the multi-story side setback ' + str(subsShelf[subOfInterest]['side2']) + ' feet? (type yes or no)')
            side2Question=input()
            if side2Question=='no':
                print('What is the multi-story side setback?')
                subsShelf[subOfInterest]['side2']=float(input())
                print('Is the street side setback ' + str(subsShelf[subOfInterest]['streetSide']) + ' feet? (type yes or no)')
            else:
                print('Is the street side setback ' + str(subsShelf[subOfInterest]['streetSide']) + ' feet? (type yes or no)')
            streetSideQuestion=input()
            if streetSideQuestion=='no':
                print('What is the street side setback?')
                subsShelf[subOfInterest]['streetSide']=input()
                print('Is the maximum lot coverage ' +str(subsShelf[subOfInterest]['lotCov']*100)+ '%? (type yes or no)')
            else:
                print('Is the maximum lot coverage ' +str(subsShelf[subOfInterest]['lotCov']*100)+ '%? (type yes or no)')
            lotCovQuestion=input()
            if lotCovQuestion=='no':
                print('What is the maximum lot coverage (in percent)?')
                subsShelf[subOfInterest]['lotCov']=input()/100
                print('Is an ACC Letter Required?')
            else:
                print('Is an ACC Letter Required?')
                subsShelf[subOfInterest]['acc']=input()
                print('Is the minimum lot size ' +str(int((subsShelf[subOfInterest]['minLot']*43560)))+ ' square feet? (type yes or no)')
            minLotQuestion=input()
            if minLotQuestion=='no':
                print('What is the minimum lot size in square feet?')
            print('Is the maximum height ' +str(subsShelf[subOfInterest]['maxHeight'])+ ' feet? (type yes or no)')
            maxHeightQuestion=input()
            if maxHeightQuestion=='no':
                print('What is the maximum height?')
                subsShelf[subOfInterest]['maxHeight']=input()
                print('Please type any additional notes')
            else:
                print('Please type any additional notes')
            subsShelf[subOfInterest]['notes']=input()
            subsShelf[subOfInterest]=subsShelf[subOfInterest]
        print('Subdivision Database Updated.\n Let\'s review this thing.')
        if subOfInterest!='':
            subsShelf['name']=subsShelf[subOfInterest]
    if subOfInterest!='':
        subsShelf['name']=subsShelf[subOfInterest]
subsShelf.close()
input('Press ENTER to exit.')
