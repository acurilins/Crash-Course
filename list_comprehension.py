# multiples = []
# for x in range (1, 11):
#   multiples.append(x*7)
  
# print(multiples)

# EASIER WAY: 

multiples = [ x*7 for x in range (1, 11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Java", "Go", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)
