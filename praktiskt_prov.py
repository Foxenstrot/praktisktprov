multiply_list = list()
input_list = list()

try:
    input_list = input("Vilka tabeller vill du beräkna? ")
    input_list = input_list.split(" ")

    length = len(input_list)

    for i in range(length):
        multiply_list.append(int(input_list[i]))
        
        for j in range(10):
            print(f'{multiply_list[i]} * {j+1} = {multiply_list[i]*(j+1)}')
        print('')
        
except ValueError:
    print(f'No values entered. Shutting down')