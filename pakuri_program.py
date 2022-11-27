from pakudex import *


def print_menu():
    print('Pakudex Main Menu')
    print('-----------------')
    print('1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit')
    print('')


if __name__ == '__main__':


    print('Welcome to Pakudex: Tracker Extraordinaire!')

    #This loop makes sure that the maxCapacity variable is a number and possitive
    loop = True
    while loop == True:

        try:
            maxCapacity = int(input('Enter max capacity of the Pakudex: '))
            if maxCapacity < 0:
                raise ValueError
            loop = False

        except ValueError:
            print('Please enter a valid size.')

    print(f'The Pakudex can hold {maxCapacity} species of Pakuri.')




    game = True
    Species = Pakudex(maxCapacity)
    size = 0


    while game == True:
        print('')
        print_menu()

        userChoice = input('What would you like to do? ')


        if userChoice == '1':
            List = Species.get_species_array()
            if List == None:
                print('No Pakuri in Pakudex yet!')
                continue
            print('Pakuri In Pakudex:')
            for i in range(0,len(List)):
                print(f'{i+1}. {List[i]}')
            continue

        if userChoice == '2':
            specie = input('Enter the name of the species to display: ')
            listOfStats = Species.get_stats(specie)
            if listOfStats == None:
                print('Error: No such Pakuri!')
                continue
            #If the Pakuri is in the list of self.pakuri, it will print out the attack, defense, and speed.
            print(f'\nSpecies: {specie}')
            print(f'Attack: {Species.get_stats(specie)[0]}')
            print(f'Defense: {Species.get_stats(specie)[1]}')
            print(f'Speed: {Species.get_stats(specie)[2]}')
            continue


        if userChoice == '3':
            if maxCapacity == size:
                print('Error: Pakudex is full!')
                continue
            speciesName = input('Enter the name of the species to add: ')
            Bollean = Species.add_pakuri(speciesName)

            if Bollean == True:
                print(f'Pakuri species {speciesName} successfully added!')
                size += 1
            if Bollean == False:
                print('Error: Pakudex already contains this species!')
            continue



        if userChoice == '4':
            specieEvolved = input('Enter the name of the species to evolve: ')
            Bollean = Species.evolve_species(specieEvolved)

            if Bollean == True:
                print(f'{specieEvolved} has evolved!')

            if Bollean == False:
                print('Error: No such Pakuri!')
            continue


        if userChoice == '5':
            #Sorts list
            Species.sort_pakuri()
            print('Pakuri have been sorted!')
            continue

        if userChoice == '6':
            print('Thanks for using Pakudex! Bye!')
            game = False

        else:
            print('Unrecognized menu selection!')

















