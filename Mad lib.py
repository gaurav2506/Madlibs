
story = '''
{}.But!{} only if  you be {} of valor!
For {} is guarded by a {} so {},so {},that no {} yet has {} with it...
and {} !
'''



def main ():
    command = input ('Enter a command (Eg:-Eat):')          #brackets inside the string are used for examples
    plural_noun = input('Enter a plural noun(Eg:-trees):')
    animal = input('Enter an animal (Eg:-Cat):')
    location= input('Enter a location(Eg:-Playground):')
    singular_noun= input('Enter a singualar noun (Eg:-Tree):')
    
    adjectives = []
    adjectives.append(input('Enter an adjective(Eg:-Big):'))
    adjectives.append(input('Enter another adjective():'))
    
    past_participles = []
    past_participles.append(input('Enter a past participle(Eg:-played):'))
    past_participles.append(input('Enter another past paticiple:'))
    
    mad_lib = story.format(command,command,plural_noun,location,animal,adjectives[0],adjectives[1],singular_noun,past_participles[0],past_participles[1])
    print(mad_lib)

main()
                            

